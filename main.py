
from transformers import pipeline
genertor = pipeline('text-generation', model='distilgpt2')
result = genertor(
    "AI is the future because",
    max_length=50,
    num_return_sequences=1
)
print(result)