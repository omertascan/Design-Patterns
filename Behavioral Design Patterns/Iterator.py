from collections.abc import Iterable, Iterator

# Iterator 
class MyIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        if self.index < len(self.collection):
            result = self.collection[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Aggregate 
class MyIterable(Iterable):
    def __init__(self):
        self.my_list = []

    def add_item(self, item):
        self.my_list.append(item)

    def __iter__(self):
        return MyIterator(self.my_list)

if __name__ == "__main__":
    my_iterable = MyIterable()
    my_iterable.add_item("Eleman 1")
    my_iterable.add_item("Eleman 2")
    my_iterable.add_item("Eleman 3")

 
    for item in my_iterable:
        print(item)
