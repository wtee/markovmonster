import random

def eat(text_file):
    """Reads a file. Returns an array of words with punctuation."""
    with open(text_file, 'r') as f:
        words = f.read().split()
    return words
        
def chew(words, length=3):
    """Reads an array of strings. Returns a generator of tuples."""
    wc = len(words)
    if wc < length:
        return
    for i in range(wc - length -1):
        yield tuple(words[i:i + length])

def digest(cud):
    """Reads tuples. Returns a dictionary."""
    corpus = {}
    for i in cud:
        corpus.setdefault(i[:-1], []).append(i[-1])
    return corpus

def vomit(corpus, length=20):
    """Reads dictionary. Returns a generated text string."""
    out_text = []
    seed = random.choice(list(corpus.keys()))
    for i in range(length):
        out_text.append(seed[0])
        seed = seed[1:] + (random.choice(corpus[seed]),)
    out_text.append(seed[-1])
    return ' '.join(out_text)
