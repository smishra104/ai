import streamlit as st
import openai
from openai import OpenAI

def get_sentiment(client, input, choices):
    system_prompt = f'''You are good emotional assistant. Evaluate the input and classify it into the appropriate 
    emotion from the following choices: {choices}. Return the emotion only.'''
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': input}
        ],
        temperature = 0
    )
    # print(response)
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

def handle_history(result):
    if 'history' not in st.session_state:
        if result:
            st.session_state.history = [result]
        else:
            st.session_state.history = []
    else:
        st.session_state.history.append(result)

    if st.session_state.history:
        st.text_area(label='History', value=st.session_state.history, height=200)
        
def show_ui():
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.title('Sentiment Analysis')
    with col2:
        st.image('taj.jpg', width=70)
    with st.form('sentiment_form'):
        default_emotions = 'positive, negative, uncomfortable, sad, lost, tired, happy'
        emotions = st.text_input('Enter emotions separated by comma', default_emotions)
        input = st.text_area(label='Enter your input', value='It is very very hot day today', height=100)
        submit_button = st.form_submit_button('Get Sentiment')
        if submit_button:
            ch = get_sentiment(client, input, emotions)
            result = f'{input} --> {ch}'
            # st.write(f'{input} --> {ch}')

            handle_history(result)

# test_openai_communication()
client = setup_openai()

if __name__ == '__main__':
    # client = setup_openai()
    show_ui()