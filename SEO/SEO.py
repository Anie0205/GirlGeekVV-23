from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("punkt")
nltk.download("stopwords")

app = Flask(__name__)

def generate_sensible_sentences(optimized_text):
    # Tokenize the optimized text into sentences
    sentences = sent_tokenize(optimized_text)
    
    # Initialize an empty list to store sensible sentences
    sensible_sentences = []
    
    for sentence in sentences:
        # Tokenize each sentence into words
        words = word_tokenize(sentence)
        
        # Remove stopwords and punctuation
        stop_words = set(stopwords.words("english"))
        filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
        
        # Create a sensible sentence from the filtered words
        sensible_sentence = " ".join(filtered_words)
        
        sensible_sentences.append(sensible_sentence)
    
    return sensible_sentences

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize_text():
    input_text = request.form['input_text']
    
    # Assume you have a function that optimizes the input_text here
    optimized_text = "journey began back unmet expectations eventually technologies explored introduced summer characterised early emergence machine learning"
    
    # Generate sensible sentences from the optimized text
    sensible_sentences = generate_sensible_sentences(optimized_text)

    return render_template('optimized.html', input_text=input_text, optimized_text=optimized_text, sensible_sentences=sensible_sentences)

if __name__ == '__main__':
    app.run(debug=True)
