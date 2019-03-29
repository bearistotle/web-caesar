from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    form = """
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          form{
              background-color: #eee;
              padding: 20px;
              margin 0 auto;
              width: 540px;
              font:16px sans-serif;
              border-radius: 10px;
          }
          textarea{
              margin: 10px;
              width: 540px;
              height: 120px;
          }
        </style>
      </head>
      <body>
        <form action="/" method="post">
          <label for="rot">Rotate by:
          <input id="rot" type="text" name="rot" value="0"/>
          </label>
         <input type="textarea" name="text"/>
         <input type="submit" name="submit" value="Encrypt Message"/>
      </body>
    </html>

    """
    return form
@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encr_text = rotate_string(text, rot)
    return "<h1>" + encr_text + "</h1>"






app.run()
