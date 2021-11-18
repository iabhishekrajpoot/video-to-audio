from flask import Flask, request
from app import VideoToAudio

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return {"url" : "https://localhost:5001"}

@app.route('/api', methods=['POST'])
def main():
    try:
        url = request.get_json(silent=True)['url']
        res = VideoToAudio(url).convert()
        return res

    except Exception as err:
        print('error = ', err)
        return {"message" : "Something went wrong"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)