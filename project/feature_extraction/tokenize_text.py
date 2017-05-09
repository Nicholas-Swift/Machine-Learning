import re


def tokenize_text(text):
    """Return a tokenized version of text by an array of array of words"""
    sentences = _get_sentences(text)
    tokens = []
    for sentence in sentences:
        tokens.append(sentence.split(' '))
    return tokens

def _get_sentences(text):
    """Return a list of sentences from the given text"""
    sentenceRegex = re.compile("[^.](.*?)[!.;?]")
    matches = sentenceRegex.findall(text)
    return matches
    # sentences = []
    # for match in matches:
    #     sentences.append(match)
    # return sentences

if __name__ == '__main__':
    print("Please use this as a module")
    