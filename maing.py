from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

EXP = [{
    "company": "Career NJNUN Mantra",
    "postion": "Social media marketing intern",
    "location": "Remote",
    "duration": 3
}, {
    "company": "Nex gen media",
    "postion": "SMKJHGM",
    "location": "Remote",
    "duration": 1
}, {
    "company": "Nic",
    "postion": "CNJOL,MNBGHreative marketing lead",
    "location": "Bengaluru",
    "duration ": 26
}]


@app.route('/')
def index():
  return render_template('home123.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
