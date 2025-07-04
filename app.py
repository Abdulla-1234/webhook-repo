from flask import Flask, request, jsonify
from datetime import datetime
import hashlib

app = Flask(__name__)

# Store seen commits to avoid duplicates
seen = set()

def format_time(ts):
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%b-%Y %H:%M:%S")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if 'commits' not in data:
        return jsonify({'message': 'No commits in payload'}), 400

    repo_name = data['repository']['full_name']
    pusher = data['pusher']['name']
    commits = data['commits']

    output = []

    for commit in commits:
        commit_id = commit['id']
        commit_key = hashlib.sha256(commit_id.encode()).hexdigest()

        if commit_key in seen:
            continue  # skip duplicates
        seen.add(commit_key)

        message = commit['message']
        url = commit['url']
        timestamp = format_time(commit['timestamp'])

        output.append({
            "repo": repo_name,
            "author": pusher,
            "message": message,
            "url": url,
            "time": timestamp
        })

    print("Received Commits:", output)
    return jsonify({"status": "ok", "received": output}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
