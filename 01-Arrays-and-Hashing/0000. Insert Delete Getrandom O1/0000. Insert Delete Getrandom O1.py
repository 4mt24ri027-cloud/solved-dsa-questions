1import random
2class RandomizedSet:
3
4    def __init__(self):
5        self.val_index = {}
6        self.values = []
7
8    def insert(self, val: int) -> bool:
9        if val in  self.values:
10            return False
11
12        self.val_index[val] = len(self.values)
13        self.values.append(val)
14        return True
15
16    def remove(self, val: int) -> bool:
17        if val not in self.values:
18            return False 
19
20        index_remove = self.val_index[val]
21        last_val = self.values[-1]
22
23        self.values[index_remove] = last_val
24        self.val_index[last_val] = index_remove
25
26        self.values.pop()
27        del self.val_index[val]
28        
29        return True
30
31    def getRandom(self) -> int:
32        return random.choice(self.values)
33        
34
35
36# Your RandomizedSet object will be instantiated and called as such:
37# obj = RandomizedSet()
38# param_1 = obj.insert(val)
39# param_2 = obj.remove(val)
40# param_3 = obj.getRandom()