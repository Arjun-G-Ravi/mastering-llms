# Data preprocessing
- Common steps:
  - Cleaning: Remove duplicates, irrelevant content, and formatting issues.
  - Tokenization: Convert text into tokens using the model's tokenizer.
  - Normalization: Lowercasing, removing special characters, etc. -> This was very common in traditional NLP, but less so with modern LLMs. But still some LLMs may benefit from specific normalization steps. (Andrej Karpathy recommends not touching the raw data much.)
  - Splitting: Divide data into training, validation, and test sets.

![alt text](image.png)
Note: The model in the image refers to tokenization model, not LLM. 
<!-- image source: https://huggingface.co/datasets/huggingface-course/documentation-images/resolve/main/en/chapter6/tokenization_pipeline-dark.svg -->