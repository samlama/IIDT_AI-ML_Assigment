class DataAnalyzer:
    def __init__(self):
        self.data_set = set()
        self.data_dict = {}

    def add_to_set(self, elements):
        self.data_set.update(elements)

    def remove_from_set(self, element):
        if element in self.data_set:
            self.data_set.remove(element)

    def get_set(self):
        return self.data_set

    def create_dictionary(self, keys, values):
        self.data_dict = dict(zip(keys, values))

    def update_dictionary(self, key, value):
        self.data_dict[key] = value

    def get_dictionary(self):
        return self.data_dict

    def search_dictionary(self, key):
        return key in self.data_dict

    def remove_from_dictionary(self, key):
        if key in self.data_dict:
            del self.data_dict[key]


# Example usage:
data_analyzer = DataAnalyzer()
data_analyzer.add_to_set([1, 2, 3, 4, 5])
print("Current state of set:", data_analyzer.get_set())

data_analyzer.remove_from_set(3)
print("Set after removing 3:", data_analyzer.get_set())

data_analyzer.create_dictionary(['a', 'b', 'c'], [1, 2, 3])
print("Current state of dictionary:", data_analyzer.get_dictionary())

data_analyzer.update_dictionary('d', 4)
print("Dictionary after adding key 'd':", data_analyzer.get_dictionary())

print("Is 'b' in the dictionary?", data_analyzer.search_dictionary('b'))

data_analyzer.remove_from_dictionary('c')
print("Dictionary after removing key 'c':", data_analyzer.get_dictionary())
