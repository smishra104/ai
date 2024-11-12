from embeddings import add_embeddings, get_embeddings
import pandas as pd
import numpy as np

def get_similarities(df, input_column, output_column, search_term_embeddings):
    df[output_column] = df[input_column].apply(lambda x: cosine_similarity(x, search_term_embeddings))
    return df.sort_values(by=output_column, ascending=False)

def cosine_similarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors."""
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

def add_similarities(input_filepath, embeddings_column, similarities_column, output_filepath, search_term):
    df = pd.read_csv(input_filepath)
    df['np'] = df[embeddings_column].apply(eval).apply(np.array)
    search_term_embeddings = get_embeddings(search_term).data[0].embedding
    df = get_similarities(df, 'np', similarities_column, search_term_embeddings)
    df.to_csv(output_filepath, index=False)

def find_similarities(input_filepath, text_column, embeddings_column, similarity_column, output_filepath, search_term):
    add_embeddings(input_filepath, text_column, embeddings_column, output_filepath)
    add_similarities(output_filepath, embeddings_column, similarity_column, output_filepath, search_term)
    df = pd.read_csv(output_filepath)
    print(df)

print(find_similarities('resources/words.csv', 'text', 'embeddings', 'similarity', 'resources/words_with_embeddings.csv', 'human'))
