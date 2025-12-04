# Tokenization
- Tokenization is the process of breaking text into smaller pieces called tokens before feeding it to a Large Language Model (LLM).
- It is a crucial step, as LLMs operate on these tokens rather than raw text. If this is wrong, nothing else will pretty much matter.
- Modern LLMs (like GPT) use subword tokenization (e.g., Byte-Pair Encoding, WordPiece).

# <UNK> Token
- The <UNK> (unknown) token is used to represent words or characters that are not in the model's vocabulary.
- It helps the model handle out-of-vocabulary words during inference.
- Byte fallback: This is a method where unknown tokens are broken down into smaller byte-level tokens, allowing the model to process them even if they are not in the vocabulary. This is especially useful for handling rare or misspelled words and is used in many tokenizers.