"""
A small Python library to generate Markov chains from text files.
"""
import random


def eat(text_file, unit='word'):
    """
    Take a file and return a list of strings.

    Arguments:
    text_file -- the file to be used to generate the Markov chain.
    unit -- this identifies the amount of granularity with which we wish to
            split the input file. Currently accepted arguments are 'word' to
            split the input file into words, so that a file containing
            'Hello. I am a test.' becomes a list: ['Hello.', 'I', 'am', 'a',
            'test.'], and 'character' so that the same file would produce
            ['H', 'e', 'l', 'l', 'o', '.', ' ', 'I', ' ', 'a', 'm', ' ',
            'a', ' ', 't', 'e', 's', 't', '.'].

    """
    if unit != 'word' and unit != 'character':
        raise ValueError('unit must equal "word" or "character".')

    with open(text_file, 'r') as fh:
        if unit == 'word':
            bits = fh.read().split()
        elif unit == 'character':
            bits = list(fh.read())

    return bits


def chew(links, key_length=2):
    """Reads an array of strings. Returns a generator of tuples."""
    wc = len(links)
    if wc < key_length + 1:
        return
    for i in range(wc - key_length):
        yield tuple(links[i:i + key_length + 1])


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
    for _ in range(length):
        out_text.append(seed[0])
        seed = seed[1:] + (random.choice(corpus[seed]),)
    out_text.append(seed[-1])
    return ' '.join(out_text)
