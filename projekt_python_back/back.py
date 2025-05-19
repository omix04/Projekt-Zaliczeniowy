from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="db",  # <--- db = name of the service in docker-compose.yml
    user="root",
    password="",
    database="projectdb"
)
cursor = db.cursor()

# create routes that let us easly switch between pages using flask instead of
# statically linked htmls, this let us just use url_for('index')
# to easly find the address of the page without changing in in every place
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/pictures')
def pictures():
    return render_template('pictures.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/reviews')
def reviews():
    return render_template('Reviews.html')

@app.route('/appointment')
def appointment():
    return render_template('Appointment.html')

@app.route('/testingpage')
def testingpage():
    return render_template('testingpage.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

# post method to insert review into database
# this method expects request body to have rating, 
# opinion and username
@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = data.get('rating')
    opinion = data.get('opinion')
    username = data.get('username')

    if not rating or not opinion or not username:
        return jsonify({'error': 'Missing fields'}), 400
    # insert into DB
    query = "INSERT INTO reviews (rating, opinion, username) VALUES (%s, %s, %s)"
    cursor.execute(query, (rating, opinion, username))
    db.commit()

    return jsonify({'message': 'Review added successfully'}), 200

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    cursor.execute("SELECT rating, opinion, username, DATE_FORMAT(created_at, '%Y-%m-%d') as date FROM reviews ORDER BY created_at DESC")
    reviews = cursor.fetchall()
    return jsonify(reviews)


@app.route('/api/images/examples', methods=['GET'])
def get_images():
    cursor.execute("SELECT file_name, file_location FROM images")
    reviews = cursor.fetchall()
    image_data = [{'file_name': r[0], 'file_location': r[1]} for r in reviews if r[1] == ("resources/examples/")]

    return jsonify(image_data)

@app.route('/api/videos/examples', methods=['GET'])
def get_videos():
    cursor.execute("SELECT file_name, file_location FROM videos")
    reviews = cursor.fetchall()
    video_data = [{'file_name': r[0], 'file_location': r[1]} for r in reviews if r[1] == ("resources/examples/videos/")]

    return jsonify(video_data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)