from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Azure MAAS Endpoint and Config
API_URL = "https://aichatbot4755917070.services.ai.azure.com/models/chat/completions?api-version=2024-05-01-preview"
API_KEY = "2uRvDxd3yZLjWMT8SXj6hcKPpB8JCp2RRGPw52yLJqLjxI5gylvNJQQJ99BDACHYHv6XJ3w3AAAAACOGVxdl"
MODEL_NAME = "DeepSeek-V3-2"  # ✅ Exact model name as configured in Azure MAAS

HEADERS = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
    "x-ms-model-mesh-model-name": MODEL_NAME  # ✅ Required header for MAAS
}

@app.route("/")
def index():
    return render_template("index.html")  # Ensure templates/index.html exists

@app.route("/get_response", methods=["POST"])
def get_response():
    try:
        data = request.get_json()
        user_input = data.get("message", "")
        history = data.get("history", [])

        messages = history + [{"role": "user", "content": user_input}]

        payload = {
            "messages": messages,
            "temperature": 0.7,
            "top_p": 0.95,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "max_tokens": 1000
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except requests.exceptions.HTTPError as err:
        return jsonify({"reply": f"⚠️ HTTP Error: {err.response.status_code} - {err.response.text}"}), err.response.status_code
    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
