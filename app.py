import os
from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>Noemi M. Enriquez – Resume</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #f2f2f2;
          margin: 0;
          padding: 0;
        }
        .container {
          max-width: 800px;
          margin: 40px auto;
          background: #ffffff;
          border-radius: 8px;
          box-shadow: 0 0 15px rgba(0,0,0,0.1);
          overflow: hidden;
        }
        .header {
          background: #663399;
          color: white;
          padding: 20px;
          display: flex;
          align-items: center;
        }
        .header img {
          width: 120px;
          height: 120px;
          border-radius: 50%;
          object-fit: cover;
          margin-right: 20px;
          border: solid 4px #fff;
        }
        .header h1 {
          margin: 0;
          font-size: 32px;
        }
        .content {
          padding: 20px;
        }
        .section {
          margin-bottom: 30px;
        }
        .section h2 {
          color: #663399;
          border-bottom: 2px solid #9966CC;
          padding-bottom: 5px;
          margin-bottom: 10px;
        }
        .contact p, .personal p {
          margin: 2px 0;
        }
        ul {
          margin: 0;
          padding-left: 20px;
        }
        ul li {
          margin-bottom: 6px;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <img src="/static/1pic.jpeg" alt="Noemi Photo">
          <h1>Noemi M. Enriquez</h1>
        </div>
        <div class="content">
          <div class="contact section">
            <h2>Contact</h2>
            <p>📱 +63 9092352261</p>
            <p>📧 noeminrqz26@gmail.com</p>
            <p>📍 Marilao, Bulacan</p>
          </div>
          <div class="section">
            <h2>About Me</h2>
            <p>I’m a first-year Computer Engineering student with a strong foundation in programming and electronics. I focus on practical skills through research and hands‑on tech projects.</p>
          </div>
          <div class="section">
            <h2>Skills</h2>
            <ul>
              <li>Eager to learn new things</li>
              <li>Time Management</li>
              <li>Decision-making</li>
              <li>Adaptability</li>
              <li>Responsibility</li>
              <li>Hardworking</li>
              <li>Result-oriented</li>
              <li>Digital Skills</li>
            </ul>
          </div>
          <div class="personal section">
            <h2>Personal Info</h2>
            <p>Birthday: November 26, 2004</p>
            <p>Gender: Female</p>
            <p>Age: 18</p>
            <p>Nationality: Filipino</p>
            <p>Status: Single</p>
          </div>
          <div class="section">
            <h2>Education</h2>
            <p><strong>Senior High School:</strong> STEM, Meycauayan National High School (2022–Present)</p>
            <p><strong>Junior High School:</strong> Meycauayan National High School (2018–2022)</p>
            <p><strong>Elementary School:</strong> Barcelona Academy (2012–2018)</p>
          </div>
        </div>
      </div>
    </body>
    </html>
    ''')

# Serve profile photo from 'static' folder
@app.route('/static/<path:filename>')
def staticfiles(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port)
