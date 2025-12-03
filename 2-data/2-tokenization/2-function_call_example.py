from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased") # using bert's tokenizer
text = "The cats are inside the superduper house"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)
print('These are the tokens and their ids:')
print(tokens)
print(token_ids) 