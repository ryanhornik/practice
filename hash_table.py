

class HashTable(object):
    table_size = 10
    table = [None] * table_size

    def __hash_func__(self, key):
        return key % self.table_size

    def __rebuild__(self, new_size=None):
        if new_size is None:
            new_size = self.table_size
        if new_size < self.table_size:
            raise RuntimeError("Cannot shrink hash table.\nPC LOAD LETTER.")
        old_table = self.table
        self.table_size = new_size
        self.table = [None] * self.table_size

        for entry in old_table:
            if entry is None:
                continue
            key, value = entry
            self.insert(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def insert(self, key, value):
        position = self.__hash_func__(key)

        count = 0
        while self.table[position] is not None:
            if self.table[position][0] == key:
                break
            position += 1
            position %= self.table_size
            count += 1
            if count >= self.table_size:
                self.__rebuild__(self.table_size * 2)
                self.insert(key, value)
                return
        self.table[position] = (key, value)

    def get(self, key):
        position = self.__hash_func__(key)

        count = 0
        while self.table[position] is not None and count < self.table_size:
            if self.table[position][0] == key:
                return self.table[position][1]

            position += 1
            position %= self.table_size
            count += 1

        return None

    def __delitem__(self, key):
        self.remove(key)

    def remove(self, key):
        position = self.__hash_func__(key)

        count = 0
        while self.table[position] is not None and count < self.table_size:
            if self.table[position][0] == key:
                self.table[position] = None
                self.__rebuild__()
                return

            position += 1
            position %= self.table_size
            count += 1

t = HashTable()
t[53] = 'Volvo'
t[67] = 'Ford'

print(t[53])

del t[53]

print(t[53])

