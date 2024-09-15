from flask import Flask, render_template, request, jsonify
from crawler import crawl_url, crawl_domain
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def crawl():
    url = request.form.get('url')
    version = request.form.get('version')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    if version == 'v1':
        external_links = crawl_url(url)
    elif version == 'v2':
        external_links = crawl_domain(url)
    else:
        return jsonify({"error": "Invalid version"}), 400
    
    return jsonify(list(external_links))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)