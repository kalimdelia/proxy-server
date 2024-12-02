from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['POST', 'GET'])
def proxy():
    try:
        # Extract incoming data from the request
        data = request.json
        url = data.get("url")
        headers = data.get("headers", {})
        body = data.get("body", {})
        
        # Proxy credentials
        proxy = {
            "http": "http://8Hw2oh:z5mE0v@46.161.23.108:8000",
            "https": "http://8Hw2oh:z5mE0v@46.161.23.108:8000",
        }

        # Determine if the request method should be GET or POST
        if request.method == 'POST':
            response = requests.post(url, headers=headers, json=body, proxies=proxy)
        elif request.method == 'GET':
            response = requests.get(url, headers=headers, proxies=proxy)

        # Return the status code and the body of the response from the target API
        return jsonify({
            "status_code": response.status_code,
            "body": response.text
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
