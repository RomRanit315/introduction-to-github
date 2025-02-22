from flask import Flask, request, render_template, send_file
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_link = request.form['video_link']
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'videos/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])
    
    return "Video downloaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)