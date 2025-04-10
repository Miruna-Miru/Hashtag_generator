from keybert import KeyBERT

kw_model = KeyBERT()

def generate_hashtags(text):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=5
    )
    hashtags = ['#' + k[0].replace(' ', '').capitalize() for k in keywords]
    return hashtags
