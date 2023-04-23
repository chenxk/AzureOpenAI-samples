
import requests

azure_openai_api_key = 'your api key'
azure_openai_api_base = 'your api base'
deployment_name = 'deployment name'
azure_openai_api_version = '2023-03-15-preview'

# Request URL
api_url = f"{azure_openai_api_base}/openai/deployments/{deployment_name}/chat/completions?api-version={azure_openai_api_version}"

# Json payload
json_data = {
    "messages": [{"role": "user", "content": "hello"}],
    "temperature": 0,
    "model": 'gpt-3.5-turbo',
    "max_tokens": 300
}

print("Question:")
print(json_data)

# Including the api-key in HTTP headers
headers = {"api-key": azure_openai_api_key}

try:
    # Request for creating a completion for the provided prompt and parameters
    response = requests.post(api_url, json=json_data, headers=headers)
    completion = response.json()

    # print the completion
    print("Answer:")
    print(completion['choices'][0]['message']['content'])
except Exception as Argument:
    print(Argument)
    print("An exception has occurred. \n")
    print("Error Message:", completion['error']['message'])

