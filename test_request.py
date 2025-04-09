import requests

url = "https://aichatbot4755917070.openai.azure.com/openai/deployments/DeepSeek-V3/chat/completions?api-version=2024-05-01-preview"
headers = {
    "Content-Type": "application/json",
    "api-key": "2uRvDxd3yZLjWMT8SXj6hcKPpB8JCp2RRGPw52yLJqLjxI5gylvNJQQJ99BDACHYHv6XJ3w3AAAAACOGVxdl"
}
data = {
    "messages": [
        {"role": "user", "content": "Hello"}
    ],
    "temperature": 0.7,
    "max_tokens": 1000
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)
