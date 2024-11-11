from openai import OpenAI
from openai_connector import setup_openai

def summarize_input(input):
    system_prompt = f'''You are a assistant of few words. You answer in 1 sentence only.'''
    prompt = f'''Create a summary of the following text.
    Text: {input}'''
    return ask_question(prompt, system_prompt)

def translate(language, input):
    system_prompt = f'''You are a assistant who can translate the input to other languages.'''
    prompt = f'''Translate the following text into {language}.
    Text: {input}'''
    return ask_question(prompt, system_prompt)

def ask_question(input, system_prompt):
    client = setup_openai()
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': input}
        ],
        temperature = 0
    )
    return response.choices[0].message.content
