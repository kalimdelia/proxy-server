from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['POST'])
def proxy():
    try:
        data = request.json
        url = data.get("url")
        headers = data.get("headers", {})
        
        # Proxy credentials
        proxy = {
            "http": "http://8Hw2oh:z5mE0v@46.161.23.108:8000",
            "https": "http://8Hw2oh:z5mE0v@46.161.23.108:8000",
        }
        
        # Forward the request through the proxy
        response = requests.get(url, headers=headers, proxies=proxy)
        return jsonify({
            "status_code": response.status_code,
            "body": response.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
