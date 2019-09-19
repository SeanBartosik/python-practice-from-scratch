# I learned about Hash Maps or python dictionaries from Mr. Joe James on YouTube
# the link from the explanation can be found here: https://www.youtube.com/watch?time_continue=384&v=9HFbhPscPU0
# Even though this is his code, I understand it well and can rewrite/utilize it from scratch

class HashMap:

    # constructor creates list of 64 cells to add key-value pairs to
    def __init__(self):
        self.size = 64
        self.map = [None] * self.size

    # _get_hash is a simple hash function that returns the index for the key
    # based on the ASCII characters of the key
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value  = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = key_value
        else:
            for pair in self.map[key_value]:
                if pair[0] == key:
                    pair[1] == value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('Elements in Hash Map')
        print('--------------------')
        for item in self.map:
            if item is not None:
                print(str(item))

k = HashMap()

k.add('20580', '1')
k.add('20581', '2')
k.print()
