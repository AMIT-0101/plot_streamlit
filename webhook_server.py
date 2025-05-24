import os
from flask import Flask, request
from dotenv import load_dotenv
import subprocess

load_dotenv()  # Loads from .env file in current dir

app = Flask(__name__)
SECRET_TOKEN = os.getenv("DEPLOY_SECRET")

@app.route('/deploy', methods=['POST'])
def deploy():
    token = request.args.get('token')
    if token != SECRET_TOKEN:
        return 'Unauthorized', 401
    subprocess.Popen(['bash', '/Users/samala2/Documents/test_webapp/plot_streamlit/start_streamlit.sh'])
    return 'Deployment triggered', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
