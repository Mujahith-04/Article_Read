
from newspaper import Article
from newspaper import Article
import nltk

from gtts import gTTS
import os

from gtts import gTTS
import os

from gtts import gTTS
import os

article_url=input("Enter a Article URL:")
art=Article(url=article_url)

art.download()

art.parse()

print("Title", art.title)

print("Authors", art.authors)

print('Publication Date',art.publish_date)

print("Text:",art.text)

print("Top Image URL:", art.top_image)

print('Movies:',art.movies)

nltk.download('punkt_tab')

art.nlp()

mytxt=art.text

language='en'

myobj=gTTS(text=mytxt,lang=language,slow=False)

myobj.save('voice.mp3')

os.system('start voice.mp3')

text = "Hello how are you today?"
tts = gTTS(text=text, lang='en')
tts.save("sample.mp3")
os.system("sample.mp3")
