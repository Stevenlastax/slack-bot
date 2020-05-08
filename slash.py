import os
from flask import Flask, jsonify, request

verification_token = os.environ['SLACK_VERIFICATION_TOKEN']

app = Flask(__name__)

@app.route('/slash', methods=['POST'])
def slash():
    if request.form['token'] == verification_token:
        payload = {'text': 'sla-bot-test Slack slash command is successful! :sunglasses:'}
        return jsonify(payload)


if __name__ == '__main__':
    app.run(port=3000)
