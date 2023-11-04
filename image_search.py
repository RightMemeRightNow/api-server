from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def search_images(tags, df, top_n=10):
    query = tags_to_query(tags, df)
    return find_similar_images(query, df, top_n)


# Define a function to find the top N most similar images
def find_similar_images(query, df, top_n=5):
    # Create a DataFrame with the query
    query_df = pd.DataFrame([query], columns=df.columns[1:])

    # Calculate cosine similarities between the query and all rows in the DataFrame
    similarities = cosine_similarity(df.iloc[:, 1:], query_df)

    # Find the indices of the top N most similar rows
    top_n_indices = similarities.argsort(axis=None)[-top_n:][::-1]

    # Get the image IDs of the top N most similar rows
    similar_image_ids = df.loc[top_n_indices, 'image'].values.tolist()

    return similar_image_ids


def tags_to_query(query, df):
    binary_query = [0] * len(df.columns[1:])

    for item in query:
        if item in df.columns[1:]:
            binary_query[df.columns.get_loc(item) - 1] = 1

    return binary_query
