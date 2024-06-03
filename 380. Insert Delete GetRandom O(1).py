class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            self.list[idx], self.list[len(self.list) - 1] = self.list[len(self.list) - 1], self.list[idx]
            self.dict[self.list[idx]] = idx
            del self.dict[val] 
            self.list.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
