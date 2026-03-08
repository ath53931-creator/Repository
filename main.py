import os
from flask import Flask, request, send_file
from flask_cors import CORS
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

app = Flask(__name__)
CORS(app)

@app.route('/edit', methods=['POST'])
def edit():
    file = request.files['video']
    file.save("input.mp4")
    
    # تحميل الفيديو الأصلي
    clip = VideoFileClip("input.mp4")
    
    # 1. إضافة نص احترافي في البداية
    txt = TextClip("تصميم ذكي", fontsize=70, color='white', font='Arial').set_duration(3).set_pos('center').crossfadein(1)
    
    # 2. إضافة مؤثر صوتي (Whoosh) - يجب أن يكون الملف موجوداً في السيرفر
    # sfx = AudioFileClip("whoosh.mp3").set_start(0)
    
    # 3. دمج كل شيء
    final = CompositeVideoClip([clip, txt])
    # final.audio = CompositeAudioClip([clip.audio, sfx])
    
    final.write_videofile("output.mp4", codec="libx264", audio_codec="aac")
    return send_file("output.mp4", as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
