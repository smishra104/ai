import streamlit as st
import openai
from openai import OpenAI
qanda_session= {}

def get_answer(client, past_qanda, question, system_prompt):
    context = []
    for past_question in past_qanda:
        context.append({'role': 'user', 'content': past_question})
        context.append({'role': 'assistant', 'content': past_qanda[past_question]})
    context.append({'role': 'user', 'content': question})

    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = context,
        temperature = 0
    )
    print(response)
    return response.choices[0].message.content

def setup_openai():
    with open('.env', 'r') as f:
        api_key = f.read().strip('\n')
        assert api_key.startswith('sk-'), 'Error reading API key'
        return OpenAI(api_key=api_key)

def test_openai_communication():
    client = setup_openai()
    choices = 'positive, negative, uncomfortable, sad, lost, tired, happy'
    ch = get_sentiment(client, "It is very very hot day today", choices)
    print("It is very very hot day today" + ' --> ' + ch)

# test_openai_communication()

def qanda(questions, system_prompt):
    client = setup_openai()
    for question in questions:
        response = get_answer(client, qanda_session, question, system_prompt)
        qanda_session[question] = response
    print(qanda_session)

def test_qanda():
    questions = ['What is the capital of France?', 'What is its longest river?', 'Convert that into miles', 'What is the population?']
    qanda(questions, 'You are a geography assistant. You give concise answers.')

test_qanda()
