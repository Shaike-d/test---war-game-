


class Card:

    def __init__(self,num,kind):
        self.num = num
        self.kind = kind
    def to_propose(self):
        return str(self.num) + self.kind
    def __str__(self):
        return f"{self.num}{self,self.kind}"