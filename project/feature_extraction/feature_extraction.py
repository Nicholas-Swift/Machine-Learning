from word_sentiment import build_trie
import itertools

trie = build_trie()

def get_features(tokens):
    """Return a dictionary of features from the given tokens"""
    all_words = list(itertools.chain.from_iterable(tokens))

    number_of_sentences = len(tokens)
    number_of_words = len(all_words)

    number_of_negative_words = average_negative_score(all_words)
    number_of_positive_words = average_positive_score(all_words)
    number_of_negating_words = num_negating_words(all_words)

    contains_bad = "bad" in all_words
    contains_worst = "worst" in all_words
    contains_stupid = "stupid" in all_words
    contains_waste = "waste" in all_words
    contains_boring = "boring" in all_words

    contains_love = "love" in all_words
    contains_wonderful = "wonderful" in all_words
    contains_best = "best" in all_words
    contains_great = "great" in all_words
    contains_superb = "superb" in all_words
    contains_beautiful = "beautiful" in all_words

    return_dict = {
        "number_of_sentences": number_of_sentences,
        "number_of_words": number_of_words,
        "average_negative_score": number_of_negative_words,
        "average_positive_score": number_of_positive_words,
        "number_of_negating_words": number_of_negating_words,
        "contains_bad": contains_bad,
        "contains_worst": contains_worst,
        "contains_stupid": contains_stupid,
        "contains_waste": contains_waste,
        "contains_boring": contains_boring,
        "contains_love": contains_love,
        "contains_wonderful": contains_wonderful,
        "contains_best": contains_best,
        "contains_great": contains_great,
        "contains_superb": contains_superb,
        "contains_beautiful": contains_beautiful
    }

    return return_dict

def average_negative_score(words):
    """Return a list of words classified as negative from the given words"""
    if len(words) == 0:
        return 0

    avg = 0
    for word in words:
        data = trie.retreive(word)
        if data is not None:
            avg += float(data[2])

    return avg

def average_positive_score(words):
    """Return a list of words classified as positive from the given words"""
    if len(words) == 0:
        return 0

    avg = 0
    for word in words:
        data = trie.retreive(word)
        if data is not None:
            avg += float(data[3])

    return avg

def num_negating_words(words):
    """Return a list of negating words from the given words"""
    negating_words = words.count("not") + words.count("none") + words.count("no") + words.count("never") + words.count("nothing")
    return negating_words


if __name__ == '__main__':
    print("Please use this as a module")
