class SmallestInfiniteSet:
    def __init__(self):
        self.loss = []

    def popSmallest(self) -> int:
        length = len(self.loss)
        if length == 0:
            self.loss.append(1)
            return 1

        for index in range(length):
            if self.loss[index] != index + 1:
                self.loss.insert(index, index + 1)
                return index + 1
        
        self.loss.append(length + 1)
        return length + 1

    def addBack(self, num: int) -> None:
        if num in self.loss:
            self.loss.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)