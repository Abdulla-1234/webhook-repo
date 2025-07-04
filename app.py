from flask import Flask, request, jsonify
from utils import format_timestamp
import hashlib

app = Flask(__name__)

# To keep track of seen commits and avoid duplicates
seen_commit_ids = set()

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_json()

    if not payload or 'commits' not in payload:
        return jsonify({'error': 'Invalid webhook payload'}), 400

    repo = payload.get('repository', {}).get('full_name', 'unknown-repo')
    pusher = payload.get('pusher', {}).get('name', 'unknown-user')
    commits = payload['commits']

    received_commits = []

    for commit in commits:
        commit_id = commit.get('id')
        if not commit_id:
            continue

        # Deduplicate using a hash of commit ID
        commit_hash = hashlib.sha256(commit_id.encode()).hexdigest()
        if commit_hash in seen_commit_ids:
            continue

        seen_commit_ids.add(commit_hash)

        commit_data = {
            "repo": repo,
            "author": pusher,
            "message": commit.get('message', ''),
            "url": commit.get('url', ''),
            "time": format_timestamp(commit.get('timestamp', ''))
        }
        received_commits.append(commit_data)

    if not received_commits:
        return jsonify({"message": "No new commits to process"}), 200

    # Print to console (you could log to file/db instead)
    print("📥 New Commits Received:")
    for item in received_commits:
        print(item)

    return jsonify({"status": "success", "data": received_commits}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
