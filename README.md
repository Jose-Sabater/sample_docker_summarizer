# Containerize a huggingface with 2 methods

## Description
- **Method 1**: flask app that runs a endpoiunt where you just request a summarization. See test_api.py
- **Method 2**: the container runs directly a script to the pipeline class

## Instructions

```bash
docker build -t summarizer_api .

docker run -p 5000:5000 summarizer_api
``` 