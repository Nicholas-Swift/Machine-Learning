# A Histogram structured as a Hash Table

from histogram import Histogram

class MarkovModel(dict):

    def __init__(self, iterable=None, order=2):
        """Initialize this histogram as a new list; update with given items"""
        super(MarkovModel, self).__init__()

        self.order = order

        if iterable:
            self.update(iterable)

    def __repr__(self):
        """Return a string representation of this histogram"""
        items = []
        for item in self.items():
            items.append(item)
        items_str = " ".join(map(str, items))
        return items_str

    def _generate_empty_previous_words(self):
        """Generate a start key based on the markov model's order"""
        previous_words = []
        for i in range(0, self.order - 1):
            previous_words.append(None)
        previous_words.append("*START*")
        return previous_words

    def insert(self, item):
        """Insert a single item to this histogram"""
        old_item = self.get(item)

        if old_item is not None:
            self.set(item, old_item + 1)
        else:
            self.set(item, 1)
            self.types += 1
        self.tokens += 1

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for sentence in iterable:

            # First word in sentence (start)
            previous_words = self._generate_empty_previous_words()

            # Run through the sentence
            for index, word in enumerate(sentence):

                current_key = tuple(previous_words)

                if self.get(current_key) is not None:
                    self[current_key].insert(word)
                else:
                    self[current_key] = Histogram()
                    self[current_key].insert(word)

                previous_words.pop(0)
                previous_words.append(word)

            # End of sentence
            current_key = tuple(previous_words)
            if self.get(current_key) is None:
                self[current_key] = Histogram()
            self[current_key].insert("*STOP*")

    def walk(self):
        """Walk through the markov model"""
        words = []

        # Create first key
        previous_words = self._generate_empty_previous_words()
        current_key = tuple(previous_words)

        while True:
            word = self[current_key].get_random()
            if word == "*STOP*":
                break
            words.append(word)

            previous_words.pop(0)
            previous_words.append(word)
            current_key = tuple(previous_words)

        return words

    def sentence_average(self, sentence):
        percents = self._sentence_percents(sentence)
        average = 0
        for percent in percents:
            average += percent
        if len(percents) == 0:
            return 0
        average = average / len(percents)
        return average

    def sentence_average_count(self, sentence):
        counts = self._sentence_counts(sentence)
        average = 0
        for count in counts:
            average += count
        if len(counts) == 0:
            return 0
        average = average / len(counts)
        return average

    def _sentence_percents(self, sentence):
        """Walk the markov model with shit and stuff"""
        percents = []

        previous_words = self._generate_empty_previous_words()
        current_key = tuple(previous_words)

        for word in sentence:

            if self.get(current_key, None) is not None:
                chance = self[current_key].get_chance(word)
                percents.append(chance)
            else:
                percents.append(0)

            previous_words.pop(0)
            previous_words.append(word)
            current_key = tuple(previous_words)

        return percents

    def _sentence_counts(self, sentence):
        percents = []

        previous_words = self._generate_empty_previous_words()
        current_key = tuple(previous_words)

        for word in sentence:

            if self.get(current_key, None) is not None:
                chance = self[current_key].get_count(word)
                percents.append(chance)
            else:
                percents.append(0)

            previous_words.pop(0)
            previous_words.append(word)
            current_key = tuple(previous_words)

        return percents




if __name__ == '__main__':
    print("please use this as a module")
    