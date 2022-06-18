import os
import sys

# Flask utils
from flask import Flask, request, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './backend')))


# Instantiate nft class
nft = createNFT()

# Define a flask app
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes



@app.route('/', methods=['GET'])
def index():
    # Main page
    return {
        "status": "sucess",
        "message": "web3 dapps",
    }

@app.route('/nft', methods=['GET', 'POST'])
def handle_upload():
    if request.method == 'POST':
        return prediction.handle_df_upload(request, secure_filename, app)
    elif request.method == 'GET':
        return {"status": "fail", "error": "No Get Route Supported in /nft endpoint"}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True, port=port)
