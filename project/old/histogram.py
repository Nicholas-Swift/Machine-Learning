# A Histogram structured as a Hash Table

import random
import timeit

class Histogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Histogram, self).__init__()
        
        self.types = 0
        self.tokens = 0

        if iterable:
            self.update(iterable)

    def __repr__(self):
        """Return a string representation of this histogram"""
        items = []
        for item in self:
            items.append(item)
        items_str = " ".join(map(str, items))
        return items_str

    def insert(self, item):
        """Insert a single item to this histogram"""
        old_item = self.get(item)

        if old_item is not None:
            self[item] = old_item + 1
        else:
            self[item] = 1
            self.types += 1
        self.tokens += 1

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            self.insert(item)

    def get_random(self):
        """Return a 'random' item, weighted based on occurance"""
        temp_value = 0
        tuple_list = []
        for key, value in self.items():
            new_tuple = (key, temp_value, temp_value + value - 1)
            tuple_list.append(new_tuple)
            temp_value += value

        random_int = random.randint(0, self.tokens-1)
        for i in tuple_list:
            if random_int >= i[1] and random_int <= i[2]:
                return i[0]

    def get_chance(self, item):
        """Return the chance of the text showing"""

        # If nothing, return 0
        if self.get(item, None) is None:
            return 0

        # Get all values
        all_values = 0
        for value in self.values():
            all_values += value

        # Return the chance
        return self[item] / all_values

    def get_count(self, item):
        if self.get(item, None) is None:
            return 0

        return self[item]

    def remove(self, item):
        """Delete the item from this histogram"""
        self[item] = None

    def count(self, key):
        """Return the count of the item with the given key"""
        value = self.get(key)
        if value is not None:
            return (key, value)
        else:
            return (key, 0)


def test_histogram():
    # Create word string and list
    word_string = "one fish two fish red fish blue fish"
    word_list = word_string.split(' ')

    print("List to add...")
    print(word_string)

    print("\n")

    # Add to DictionaryHistogram
    hist = Histogram(word_list)

    print("types...")
    print(hist.types)

    print("\n")

    print("tokens...")
    print(hist.tokens)

    print("\n")

    print("histogram...")
    print(hist)


if __name__ == '__main__':
    test_histogram()

    