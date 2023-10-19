from flask import Flask , render_template

app = Flask(__name__)

JOBS= [
  {
    'id':1,
    'title':'Data Analyst',
    'company':'Google',
    'location':'Mumbai, India',
    'salary':'$50,000'
  },
  {
    'id':2,
    'title':'Data Scientist ',
    'company':'Google',
    'location':'Delhi, India',
    'salary':'$80,000'
  },
  {
  'id':3,
  'title':'Data Analyst',
  'company':'Google',
  'location':'Bengaluru, India',
  'salary':'$70,000'
},
  {
    'id':4,
    'title':'Backend Engineer',
    'company':'Microsoft',
    'location':'Mumbai, India',
    'salary':'$150,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug = True)
  