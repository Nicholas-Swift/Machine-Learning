import re
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer()

def tokenize_text(text):
    """Return a tokenized version of text by an array of array of words"""
    sentences = _get_sentences(text)
    tokenized_text = _tokenize_sentences(sentences)
    return tokenized_text

def _tokenize_sentences(sentences):
    """Return a tokenized version of the sentences"""
    for i in range(len(sentences)):
        sentences[i] = tokenizer.tokenize(sentences[i])
    return sentences

def _get_sentences(text):
    """Return a list of sentences from the given text"""
    sentenceRegex = re.compile("[^.](.*?)[!.;?]")
    matches = sentenceRegex.findall(text)

    sentences = []
    for match in matches:
        sentences.append(match)

    return sentences

if __name__ == '__main__':
    print("Please use this as a module")

    