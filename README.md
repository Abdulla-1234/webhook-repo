# GitHub Webhook Receiver

A Flask-based server that listens for GitHub push webhook events and extracts commit details.

---

## Features

- Accepts POST webhook requests at `/webhook`
- Displays repo name, author, message, timestamp, and commit URL
- Filters out duplicate commit events using hashing
- Formats timestamps into human-readable form

---

## Run Locally

### Prerequisites:
- Python 3.7+
- pip
- (Optional) ngrok

### Steps:

```bash
# Clone the repo
git clone https://github.com/Abdulla-1234/webhook-repo.git
cd webhook-repo

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
