
def sanitize_text(text):
    """Return a sanitized version of the given text"""

    # Remove <br, />, ...
    text = text.replace('<br', ' ').replace('/>', ' ').replace('...', ' ').replace('..', ' ')

    # Remove other characters
    text = _remove_extraneous_characters(text)

    # Fix contractions
    text = _fix_contractions(text)

    # Lowecase all
    text = text.lower()

    # Remove over 2 spaces
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
        "amn't": "am not",
        "aren't": "are not",
        "can’t": "cannot",
        "could’ve": "could have",
        "couldn’t": "could not",
        "didn’t": "did not",
        "doesn’t": "does not",
        "don’t": "do not[4]",
        "gonna": "going to",
        "gotta": "got to",
        "hadn’t": "had not",
        "hadn’t": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he’d": "he had",
        "wouldn't": "would not",
        "would've": "he would have",
        "he’ll": "he will",
        "he’s": "he is",
        "isn't": "is not",
        "how’d": "how did",
        "how’ll": "how will",
        "how’s": "how is",
        "I’d": "I would",
        "I’ll": "I will",
        "I’m": "I am",
        "I’ve": "I have",
        "isn’t": "is not",
        "it’d": "it would",
        "it’ll": "it will",
        "it’s": "it is",
        # "mightn’t    might not"
        # "might’ve    might have"
        # "mustn’t must not"
        # "mustn't have    must not have"
        # "must’ve must have"
        # "needn't need not"
        # "o’clock of the clock"
        # "ol’ old"
        # "oughtn’t    ought not"
        # "shan’t  shall not"
        # "she’d   she had / she would"
        # "she hadn't  she had not"
        # "she wouldn't have   she would not have"
        # "she would've    she would have"
        # "she’ll  she shall / she will"
        # "she’s   she has / she is"
        # "she isn't   she is not"
        # "should’ve   should have"
        # "shouldn’t   should not"
        # "shouldn’t have  should not have"
        # "somebody would've   somebody would have"
        # "somebody wouldn't have  somebody would not have"
        # "somebody’s  somebody is"
        # "someone’d   someone had / someone would"
        # "someone hadn't  someone had not"
        # "someone wouldn't have   someone would not have"
        # "someone would've    someone would have"
        # "someone’ll  someone shall / someone will"
        # "someone’s   someone has / someone is"
        # "something’d something had / something would"
        # "something'dn't  something had not / something would not"
        # "something'dn't've   something had not have / something would not have"
        # "something’d’ve  something would have"
        # "something’ll    something shall / something will"
        # "something’s something has / something is"
        # "that’ll that will"
        # "that’s  that has / that is"
        # "that’d  that would / that had"
        # "there’d there had / there would"
        # "there'dn't  there had not / there would not"
        # "there'dn't've   there had not have / there would not have"
        # "there’d’ve  there would have"
        # "there’re    there are"
        # "there’s there has / there is"
        # "they’d  they had / they would"
        # "they’dn’t   they had not / they would not"
        # "they’dn’t’ve    they had not have / they would not have"
        # "they’d’ve   they would have"
        # "they’d’ven’t    they would have not"
        # "they’ll they shall / they will"
        # "they won't have they will not have"
        # "they’re they are"
        # "they’ve they have"
        # "they haven't    they have not"
        # "wasn’t  was not"
        # "we’d    we had / we would"
        # "we would've we would have"
        # "we wouldn't we would not"
        # "we wouldn't have    we would not have"
        # "we’ll   we will"
        # "we won't have   we will not have"
        # "we’re   we are"
        # "we’ve   we have"
        # "weren’t were not"
        # "what'd  what did"
        # "what’ll what shall / what will"
        # "what’re what are"
        # "what’s  what has / what is / what does"
        # "what’ve what have"
        # "when’s  when has / when is"
        # "where’d where did"
        # "where’s where has / where is / where does"
        # "where’ve    where have"
        # "who’d   who would / who had / who did"
        # "who’d’ve    who would have"
        # "who’ll  who shall / who will"
        # "who’re  who are"
        # "who’s   who has / who is / who does"
        # "who’ve  who have"
        # "why'd   why did"
        # "why’re  why are"
        # "why’s   why has / why is / why does"
        # "won’t   will not"
        # "won’t’ve    will not have"
        # "would’ve    would have"
        # "wouldn’t    would not"
        # "wouldn’t’ve would not have"
        # "y’all / ya'll   you all, literally, "ya all""
        # "y’all’d’ve  you all would have"
        # "y’all’dn’t’ve   you all would not have"
        # "y’all’ll    you all will"
        # "y’all’on’t  you all will not"
        # "y’all’ll’ve you all will have"
        # "y'all're    you all are"
        # "y’all’ll’ven’t  you all will have not"
        # "y’ain't you are not"
        # "you’d   you had / you would"
        # "you’d’ve    you would have"
        # "you’ll  you shall / you will"
        # "you’re  you are"
        # "you aren’t  you are not"
        # "you’ve  you have"
        # "you haven't you have not"
    }

    for key, value in contractions_dict.items():
        text = text.replace(key, value)

    return text


if __name__ == '__main__':
    print("Please use this as a module")

    