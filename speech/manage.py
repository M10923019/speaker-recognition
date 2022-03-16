#! /usr/bin/env python
# -*-coding:utf-8-*-
from flask import Flask, render_template
from flask import request
import time

from Speaker_Recognition import register, speakerrecog 

app = Flask(__name__)

# 首頁
@app.route("/")
def index():
	return render_template("index.html")

# 聲紋註冊
@app.route("/speech",methods=['GET', 'POST'])
def beginRecorder():
	# printName = request.form["printNames"]
	printName = request.form.get('printNames')
	begin  = time.time()
	register.train_model(printName)
	# speechRecorder.run()
	return "200"

# 結束錄音
@app.route("/stopSpeech", methods=["GET", "POST"])
def stopRecorder():
	print("停止錄音......")
	# speechRecorder.stop()
	end = time.time()
	return "200"

# 聲紋辨識
@app.route("/recognize", methods=['GET', 'POST'])
def recognize():
	return speakerrecog.speakerRecog()

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port=3000, threaded = True)
