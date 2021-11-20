from flask import Flask, request, send_from_directory
from app import VideoToAudio
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# to test api 
@app.route('/', methods=['GET'])
def index():
    return {"url" : "https://localhost:5001"}

# main api
@app.route('/api', methods=['GET'])
def main():
    try:
        url = request.args.get('url')

        if (url == None):
            return {"message" : "require url"}
        
        res = VideoToAudio(url).convert()
        
        path = os.curdir
        return send_from_directory(filename=res, as_attachment=True, path=path, directory=path)
        
    except Exception as err:
        print('error = ', err)
        return {"message" : "Something went wrong"},404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)