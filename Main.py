from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return '<body style="background-color:red;" ><h1 style="font-size:55px;font-family:Arial;color: white; text-align: center;">Joe\'s Armory</h1></body>'

@app.route('/login')
def login():
   return 'welcome-to-the-login'

if __name__ == '__main__':
   app.run()