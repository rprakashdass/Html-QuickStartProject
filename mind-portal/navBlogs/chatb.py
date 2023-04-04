import Flask
from flask import Flask, render_template, request
import numpy as nump
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

f = open('./mlinfotochat.txt','r',errors = 'ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict))) 

GREET_INPUTS = ("hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening")
GREET_RESPONSES = ("Hello there!", "Hi!", "Hey!", "Greetings!", "Good morning/afternoon/evening to you too!")
def greet(sentence):
  for word in sentence.split():
   if word.lower() in GREET_INPUTS:
    return random.choice(GREET_RESPONSES)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_response = request.args.get('msg')
    if(greet(user_response)!=None):
        return str("chatB:  "+greet(user_response))
    else:
        sent_tokens.append(user_response)
        word_tokens=word_tokens+nltk.word_tokenize(user_response)
        final_words=list(set(word_tokens))
        return str("chatB:  "+response(user_response))

def response(user_response):
  robo1_response=''
  TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if(req_tfidf==0):
    robo1_response=robo1_response+"Hey! I apologize, as I am still under development, I can't find anything else you asked for."
    return robo1_response
  else:
    robo1_response = robo1_response+sent_tokens[idx]
    return robo1_response

if __name__ == '__main__':
    app.run(debug=True)