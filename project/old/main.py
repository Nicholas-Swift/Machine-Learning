from nltk.tokenize import TweetTokenizer
from sanitize_text import sanitize_text
from tokenize_text import tokenize_text
from markov_model import MarkovModel

import os

text = ['This', 'is', 'a', 'terribe', 'movie']

negative_markov_model = MarkovModel(order=1)
path = "./aclImdb/train/neg"
for filename in os.listdir(path)[:1000]:

    # Get file
    file = open(path + "/" + filename, 'r')
    text = file.read()
    file.close()

    # Add to model
    sanitized_text = sanitize_text(text)
    tokens = tokenize_text(sanitized_text)
    negative_markov_model.update(tokens)
print(negative_markov_model.sentence_average_count(text))

positive_markov_model = MarkovModel(order=1)
path = "./aclImdb/train/pos"
for filename in os.listdir(path)[:1000]:

    # Get file
    file = open(path + "/" + filename, 'r')
    text = file.read()
    file.close()

    # Add to model
    sanitized_text = sanitize_text(text)
    tokens = tokenize_text(sanitized_text)
    positive_markov_model.update(tokens)
print(positive_markov_model.sentence_average_count(text))

# Test negative
print("Negative test")
all_unknown = 0
all_positives = 0
all_negatives = 0
path = "./aclImdb/test/neg"
for filename in os.listdir(path)[:1000]:

    # Get file
    file = open(path + "/" + filename, 'r')
    text = file.read()
    file.close()

    # Check against model
    sanitized_text = sanitize_text(text)
    tokens = tokenize_text(sanitized_text)

    if len(tokens) <= 0:
        continue

    neg_avg = 0
    for sentence in tokens:
        neg_avg += negative_markov_model.sentence_average_count(sentence)
    neg_avg = neg_avg / len(tokens)

    pos_avg = 0
    for sentence in tokens:
        pos_avg += positive_markov_model.sentence_average_count(sentence)
    pos_avg = pos_avg / len(tokens)

    # Add to all
    if pos_avg > neg_avg:
        all_positives += 1
    elif neg_avg > pos_avg:
        all_negatives += 1
    else:
        all_unknown += 1
print("pos:")
print(all_positives)
print("neg:")
print(all_negatives)
print("unkown:")
print(all_unknown)

# Test Positive
print("Positive test")
all_unknown = 0
all_positives = 0
all_negatives = 0
path = "./aclImdb/test/pos"
for filename in os.listdir(path)[:1000]:

    # Get file
    file = open(path + "/" + filename, 'r')
    text = file.read()
    file.close()

    # Check against model
    sanitized_text = sanitize_text(text)
    tokens = tokenize_text(sanitized_text)

    if len(tokens) <= 0:
        continue

    neg_avg = 0
    for sentence in tokens:
        neg_avg += negative_markov_model.sentence_average(sentence)
    neg_avg = neg_avg / len(tokens)

    pos_avg = 0
    for sentence in tokens:
        pos_avg += positive_markov_model.sentence_average(sentence)
    pos_avg = pos_avg / len(tokens)

    # Add to all
    if pos_avg > neg_avg:
        all_positives += 1
    elif neg_avg > pos_avg:
        all_negatives += 1
    else:
        all_unknown += 1
print("pos:")
print(all_positives)
print("neg:")
print(all_negatives)
print("unkown:")
print(all_unknown)




# s0 = """This is really a new low in entertainment. This is really a new low in entertainment. Even though there are a lot worse movies out.<br /><br />In the Gangster / Drug scene genre it is hard to have a convincing storyline (this movies does not, i mean Sebastians motives for example couldn't be more far fetched and worn out cliché.) Then you would also need a setting of character relationships that is believable (this movie does not.) <br /><br />Sure Tristan is drawn away from his family but why was that again? what's the deal with his father again that he has to ask permission to go out at his age? interesting picture though to ask about the lack and need of rebellious behavior of kids in upper class family. But this movie does not go in this direction. Even though there would be the potential judging by the random Backflashes. Wasn't he already down and out, why does he do it again? <br /><br />So there are some interesting questions brought up here for a solid socially critic drama (but then again, this movie is just not, because of focusing on "cool" production techniques and special effects an not giving the characters a moment to reflect and most of all forcing the story along the path where they want it to be and not paying attention to let the story breath and naturally evolve.) <br /><br />It wants to be a drama to not glorify abuse of substances and violence (would be political incorrect these days, wouldn't it?) but on the other hand it is nothing more then a cheap action movie (like there are so so many out there) with an average set of actors and a Vinnie Jones who is managing to not totally ruin what's left of his reputation by doing what he always does.<br /><br />So all in all i .. just ... can't recommend it.<br /><br />1 for Vinnie and 2 for the editing."""

# sanitized_text = sanitize_text(s0)
# tokens = tokenize_text(sanitized_text)
# markov_model = MarkovModel(tokens, order=1)
# print(markov_model.sentence_average(['This', 'is', 'a', 'terribe', 'movie']))
