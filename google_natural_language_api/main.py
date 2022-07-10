# %%
#!export GOOGLE_APPLICATION_CREDENTIALS="/Users/anuj/Desktop/anuj/repo/yt_v2/youtube/google_natural_language_api/key.json"

# %%
#!pip install --upgrade google-cloud-language
# %%
from google.cloud import language_v1
client = language_v1.LanguageServiceClient()

# %%
text = u"""Google, headquartered in 
    Mountain View (1600 Amphitheatre Pkwy, 
    Mountain View, CA 940430), unveiled the new Android phone 
    for $799 at the Consumer Electronic Show. 
    Sundar Pichai said in his keynote that users 
    love their new Android phones."""
        
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)
# %%
# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
# %%
