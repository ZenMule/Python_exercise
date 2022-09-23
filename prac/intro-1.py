import numpy as np
sentence = """Thomas Jefferson began building Monticello at the age of 26."""
sentence.split()

token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))
', '.join(vocab)
num_tokens = len(token_sequence)
vocab_size = len(vocab)

onehot_vectors = np.zeros((num_tokens, vocab_size), int)

for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1

' '.join(vocab)

onehot_vectors

import pandas as pd
df = pd.DataFrame(onehot_vectors, columns = vocab)
df[df == 0] = ''
df

sentence_bow = {}
for token in sentence.split():
    sentence_bow[token] = 1
sorted(sentence_bow.items())

pd.DataFrame(pd.Series(dict([(token, 1) for token in sentence.split()])), columns = ['sent']).T

sentences = """Thomas Jefferson began building Monticello at the age of 26.\n"""
sentences += """Construction was done mostly by local masons and carpenters.\n"""
sentences += "He moved into the South Pavilion in 1770.\n"
sentences += """Turning Monticello into a neoclassical masterpice waqs Jefferson's obsession."""
sentences

corpus = {}
for i, sent in enumerate(sentence.split('\n')):
    corpus['sent{}',format(i)] = dict((tok, 1) for tok in sent.split())

df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T
df

