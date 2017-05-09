
def clean_text(text):
    """Return a sanitized version of the given text"""
    text = text.replace('<br', ' ').replace('/>', ' ')
    text = text.replace('...', ' ').replace('..', ' ')

    text = _remove_extraneous_characters(text)
    text = _fix_contractions(text)

    text = text.lower()
    text = ' '.join(text.split())

    return text

def _remove_extraneous_characters(text):
    """Return text with removed extraneous characters"""
    chars_to_delete = ',-"*@#%^()'
    for char in chars_to_delete:
        text = text.replace(char, ' ')
    return text

def _fix_contractions(text):
    """Return text with all contractions made whole"""
    contractions_dict = {
        "amn't":"am not",
        "aren't":"are not",
        "can't":"cannot",
        "could've":"could have",
        "couldn't":"could not",
        "didn't":"did not",
        "doesn't":"does not",
        "don't":"do not[4]",
        "gonna":"going to",
        "gotta":"got to",
        "hadn't":"had not",
        "hadn't":"had not have",
        "hasn't":"has not",
        "haven't":"have not",
        "he'd":"he had",
        "wouldn't":"would not",
        "would've":"he would have",
        "he'll":"he will",
        "he's":"he is",
        "isn't":"is not",
        "how'd":"how did",
        "how'll":"how will",
        "how's":"how is",
        "I'd":"I would",
        "I'll":"I will",
        "I'm":"I am",
        "I've":"I have",
        "isn't":"is not",
        "it'd":"it would",
        "it'll":"it will",
        "it's":"it is",
        "mightn't": "might not",
        "might've":"might have",
        "mustn't":"must not",
        "must've":"must have",
        "needn't":"need not",
        "oughtn't":"ought not",
        "shan't":"shall not",
        "she'd":"she would",
        "she'll":"she will",
        "she's":"she is",
        "should've":"should have",
        "shouldn't":"should not",
        "somebody's":"somebody is",
        "someone'd":"someone had",
        "someone'll":"someone shall / someone will",
        "someone's":"someone has",
        "something's":"something has",
        "that'll":"that will",
        "that's":"that is",
        "that'd":"that would",
        "they'd":"they had",
        "they'dn't":"they had not",
        "they'dn't've":"they had not have",
        "they'd've":"they would have",
        "they'd'ven't":"they would have not",
        "they'll":"they will",
        "they're":"they are",
        "they've":"they have",
        "wasn't":"was not",
        "we'd":"we would",
        "we'll":"we will",
        "we're":"we are",
        "we've":"we have",
        "weren't":"were not",
        "what'd":"what did",
        "what'll":"what will",
        "what're":"what are",
        "what's":"what is",
        "what've":"what have",
        "when's":"when is",
        "where'd":"where did",
        "where's":"where is",
        "where've":"where have",
        "who'd":"who would",
        "who'd've":"who would have",
        "who'll":"who will",
        "who're":"who are",
        "who's":"who is",
        "who've":"who have",
        "why'd":"why did",
        "why're":"why are",
        "why's":"why is",
        "won't":"will not",
        "won't've":"will not have",
        "would've":"would have",
        "wouldn't":"would not",
        "wouldn't've":"would not have",
        "ya'll":"you all",
        "y'all'd've":"you all would have",
        "y'all'dn't've":"you all would not have",
        "y'all'll":"you all will",
        "y'all'on't":"you all will not",
        "y'all'll've":"you all will have",
        "y'all're":"you all are",
        "you'd":"you would",
        "you'd've":"you would have",
        "you'll":"you will",
        "you're":"you are",
        "you've":"you have"}

    for key, value in contractions_dict.items():
        text = text.replace(key, value)

    return text


if __name__ == '__main__':
    print("Please use this as a module")
    