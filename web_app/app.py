from flask import Flask, render_template, request, redirect, url_for
from src.packet_capture import start_packet_capture  # Adjust import paths based on your structure
from src.security_report import generate_security_report

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renders the main HTML page

@app.route('/start-capture', methods=['POST'])
def start_capture():
    start_packet_capture()
    return redirect(url_for('index'))

@app.route('/stop-capture', methods=['POST'])
def stop_capture():
    # Add logic to stop packet capture
    return redirect(url_for('index'))

@app.route('/upload-pcap', methods=['POST'])
def upload_pcap():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    # Handle file upload logic
    return redirect(url_for('index'))

@app.route('/generate-report', methods=['POST'])
def generate_report_view():
    generate_security_report()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
