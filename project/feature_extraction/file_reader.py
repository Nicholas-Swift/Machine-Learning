from sanitize_text import clean_text
from tokenize_text import tokenize_text


def open_and_tokenize(filename):
    """Return tokens from the file with the given filename"""
    file = open(filename, 'r')
    text = file.read()
    file.close()

    text = clean_text(text)
    tokens = tokenize_text(text)

    return tokens


if __name__ == '__main__':
    print("Please use this as a module")
    