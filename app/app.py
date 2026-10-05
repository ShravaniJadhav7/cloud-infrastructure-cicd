from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud Infrastructure & CI/CD Platform</h1>
    <p>Application Status: Running</p>
    <p>Environment: AWS EC2</p>
    <p>Container: Docker</p>
    <p>CI/CD: GitHub Actions</p>
    <p>Infrastructure: Terraform</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)