from openai import OpenAI

def setup_openai():
    with open('.env', 'r') as f:
        api_key = f.read().strip('\n')
        assert api_key.startswith('sk-'), 'Error reading API key'
        return OpenAI(api_key=api_key)

