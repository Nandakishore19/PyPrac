class PassingScoreIterator:
    def __init__(self,lis,passing) -> None:
        self.lis = lis
        self.ind =0
        self.passing = passing
    def __iter__(self):
        return self
    def __next__(self):
        while self.ind< len(self.lis):
            score = self.lis[self.ind]
            if self.lis[self.ind] >= self.passing:
                self.ind+=1
                return score
            else:
                self.ind+=1
        else:
            raise StopIteration


lis = [100,99,98,97,65,66,69,74,75]
passing = 74
iter = PassingScoreIterator(lis,passing)
for n in iter:
    print(n)