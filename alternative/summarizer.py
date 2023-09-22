import sys
from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
    return summarizer(text, min_length=20, max_length=100)[0]['summary_text']

if __name__ == '__main__':
    input_text = sys.argv[1]  # Get the input text from command-line argument
    print(summarize_text(input_text))