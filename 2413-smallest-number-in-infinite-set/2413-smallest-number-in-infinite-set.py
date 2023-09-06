class SmallestInfiniteSet:
    def __init__(self):
        self.loss = []

    def popSmallest(self) -> int:
        if len(self.loss) == 0:
            self.loss.append(1)
            return 1

        for index in range(len(self.loss)):
            if self.loss[index] != index + 1:
                self.loss.insert(index, index + 1)
                return index + 1
        
        self.loss.append(len(self.loss) + 1)
        return len(self.loss)

    def addBack(self, num: int) -> None:
        if len(self.loss) > 0:
            self.loss = list(filter(lambda n: n != num, self.loss))


        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)