from flask import Flask

app = Flask()  


@app.route('/my-first-api', method = ['GET'])

def hello():

    return "Hello world!"



if __name__ == '__main__':
    app.run(debug=True, port=8000)