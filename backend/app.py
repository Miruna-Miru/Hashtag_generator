from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from keybert import KeyBERT

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class TextInput(BaseModel):
    content: str

# Keyword model
kw_model = KeyBERT()

# Emoji dictionary
emoji_dict = {
    "food": "🍔", "travel": "✈️", "fitness": "💪", "love": "❤️",
    "nature": "🌿", "music": "🎵", "technology": "💻", "sports": "🏅",
    "study": "📚", "fashion": "👗", "photography": "📸", "art": "🎨",
    "celebration":"🥳","birthday":"🍰","happy":"🤗",
    "coding": "👨‍💻", "python": "🐍", "coffee": "☕", "business": "💼", "party": "🎉","good" : "👍","star" :"✨"
}

def add_emoji_to_hashtag(word):
    for keyword, emoji in emoji_dict.items():
        if keyword.lower() in word.lower():
            return emoji
    return ""

def generate_hashtags(text):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=5
    )
    hashtags = []
    for k in keywords:
        keyword_clean = k[0].replace(' ', '')
        emoji = add_emoji_to_hashtag(k[0])
        hashtag = '#' + keyword_clean.capitalize()
        if emoji:
            hashtag += f" {emoji}"
        hashtags.append(hashtag)
    return hashtags

@app.post("/generate")
def generate_keywords(input: TextInput):
    hashtags = generate_hashtags(input.content)
    return {"hashtags": hashtags}
