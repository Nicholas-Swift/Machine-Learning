
class Trie:

    VALUE_KEY = "*VALUE*"

    def __init__(self):
        self.root = {}

    def insert(self, key, value):
        """Insert an item into a trie"""
        characters = list(key)
        current = self.root

        # Traverse through the trie
        for character in characters:
            if character not in current:
                current[character] = {}
            current = current[character]

        # Add the value
        current[Trie.VALUE_KEY] = value

    def retreive(self, item):
        """Retreive a value from an item or None"""
        characters = list(key)
        current = self.root

        # Traverse through the trie
        for character in characters:
            if character not in current:
                return None
            current = current[character]

        # Get value
        return current.get(VALUE_KEY, None)


def get_lines():
    """Return the lines in a file"""
    file = open("words.txt", "r")
    lines = file.readlines()
    return lines

def clean_line(line):
    """Clean the line and return a list of words"""
    return line.split()

def format_cleaned_line(line):
    """Format the cleaned line and return what we want"""

    # Get scores and info
    try:
        POS = line[0]
        ID = line[1]
        pos_score = line[2]
        neg_score = line[3]
    except:
        return []

    # Get all words
    words = []
    for word in line[4:]:
        if "#" not in word: break
        words.append(word)

    # Format features
    features = list(map(lambda x: {"word": x, "POS": POS, "ID": ID, "pos_score": pos_score, "neg_score": neg_score}, words))
    return features

def build_trie():

    t = Trie()
    all_features = []

    lines = get_lines()
    for line in lines:
        cleaned_line = clean_line(line)
        features = format_cleaned_line(cleaned_line)
        #print(features)
        all_features.extend(features)
    for feature in all_features:
        word = feature["word"].split("#")[0]
        t.insert(word, (feature["POS"], feature["ID"], feature["pos_score"], feature["neg_score"]))

    return t


build_trie()

    