class ListManipulator:
    def __init__(self):
        self.internal_list = []

    def add_elements(self, elements):
        self.internal_list.extend(elements)

    def remove_duplicates(self):
        self.internal_list = list(set(self.internal_list))

    def reverse_list(self):
        self.internal_list.reverse()

    def sort_list(self):
        self.internal_list.sort()

    def get_unique_elements(self):
        return list(set(self.internal_list))

    def remove_element(self, element):
        if element in self.internal_list:
            self.internal_list.remove(element)

    def get_list(self):
        return self.internal_list


# Example usage:
list_manipulator = ListManipulator()
list_manipulator.add_elements([1, 2, 3, 4, 5, 1, 2, 3])
print("Original List:", list_manipulator.get_list())

list_manipulator.remove_duplicates()
print("List after removing duplicates:", list_manipulator.get_list())

list_manipulator.reverse_list()
print("List after reversing:", list_manipulator.get_list())

list_manipulator.sort_list()
print("List after sorting:", list_manipulator.get_list())

print("Unique elements in the list:", list_manipulator.get_unique_elements())

list_manipulator.remove_element(3)
print("List after removing first occurrence of 3:", list_manipulator.get_list())
