from flask import Flask, request, render_template, session, redirect 
import random
import datetime

app = Flask(__name__)
app.secret_key = "twinjuan"

@app.route('/')
def index():
    if not 'total' in session:
        session['total'] = 0
        session["activity"] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building == "farm":
        earned = random.randrange(10,21)
        session["total"] += earned
        session["activity"].append("Earned " + str(earned) + " golds from the Farm! (" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ")")
    elif building == "cave":
        earned = random.randrange(5,11)
        session["total"] += earned
        session["activity"].append("Earned " + str(earned) + " golds from the Cave! (" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ")")
    elif building == "house":
        earned = random.randrange(2,6)
        session["total"] += earned
        session["activity"].append("Earned " + str(earned) + " golds from the House! (" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ")")
    elif building == "casino":
        earned = random.randrange(-50,51)
        session["total"] += earned
        if earned >= 0:
            session["activity"].append("Entered a Casino and earned " + str(earned) + " golds (" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ")")
        else:
            session["activity"].append("Entered a Casino and lost " + str(earned) + " golds... Ouch. (" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ")")
    
    return redirect("/")

app.run(debug=True)
