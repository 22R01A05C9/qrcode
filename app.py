from flask import Flask,render_template,request
import qrcode.main
from random import randint
from threading import Thread
from time import sleep
import os


app=Flask(__name__)

def del_qr_code(ran):
    sleep(600)
    os.remove(f'static/qr_codes/{ran}.png')

@app.route('/')
def main():
    return render_template("index.html")

@app.route("/generate",methods=['POST'])
def generate():
    ran = randint(1111,9999)
    data = request.form['data']
    fore = request.form['fore']
    back = request.form['back']
    features = qrcode.main.QRCode(version=4,box_size=35,border=2)
    features.add_data(data)
    features.make(fit=True)
    code =  features.make_image(fill_color=fore,back_color=back)
    code.save(f"static/qr_codes/{ran}.png")
    Thread(target=del_qr_code,args=(ran,)).start()
    return str(ran)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True) 