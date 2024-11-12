from openai import OpenAI
from openai_connector import setup_openai
import pandas as pd
import numpy as np

def get_embeddings(input):
    client = setup_openai()
    input = input.replace('\n', '')
    return client.embeddings.create(model="text-embedding-ada-002", input=input)

def add_embeddings(input_filepath, text_column, embeddings_column, output_filepath):
    df = pd.read_csv(input_filepath)
    df[embeddings_column] = df[text_column].apply(lambda x: get_embeddings(x).data[0].embedding)
    df.to_csv(output_filepath, index=False)

