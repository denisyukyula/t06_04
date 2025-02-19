class HashTable:
    def __init__(self, size=10007):
        self.size = size
        self.table = [[] for i in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

library = HashTable()

def init():
    global library
    library = HashTable()

def addBook(author, title):
    books = library.search(author)
    if books is None:
        books = set()
    books.add(title)
    library.insert(author, books)

def find(author, title):
    books = library.search(author)
    return books is not None and title in books

def delete(author, title):
    books = library.search(author)
    if books is None or title not in books:
        return
    books.remove(title)
    if books:
        library.insert(author, books)
    else:
        library.delete(author)

def findByAuthor(author):
    books = library.search(author)
    return sorted(books) if books else []
