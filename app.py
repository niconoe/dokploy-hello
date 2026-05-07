import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("VISITOR_NAME", "stranger")
    host = socket.gethostname()
    return f"""
    <html>
      <head><title>Hello from Dokploy</title></head>
      <body style="font-family: sans-serif; max-width: 600px; margin: 4em auto;">
        <h1>Hello, {name} 👋</h1>
        <p>Served from container <code>{host}</code></p>
        <p>If you see this over HTTPS with your own domain, Dokploy is working.</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
