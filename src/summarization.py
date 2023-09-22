from transformers import pipeline

class Summarizer:
    """Wrapper class for the HuggingFace pipeline"""
    def __init__(self, task:str ="summarization", model_name:str="philschmid/bart-large-cnn-samsum"):
        self.summarizer = pipeline(task, model=model_name)

    def summarize(self, text:str, min_length:int=20, max_length:int=100):
        """Summarize text using the HuggingFace pipeline"""
        return self.summarizer(text, min_length=min_length, max_length=max_length)[0]['summary_text']
