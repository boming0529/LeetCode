class MinStack:

    def __init__(self):
        self.stack = []
        self.__min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.__min:
            self.__min.append(val if self.__min[-1] > val else self.__min[-1])
        else:
            self.__min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.__min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.__min[-1]
    
    # def __TheSplit(self, arr):
    #     if len(arr) < 2:
    #         return arr
    #     mid = len(arr) // 2
    #     L = arr[:mid]
    #     R = arr[mid:]
    #     return self.__merge(self.__TheSplit(L), self.__TheSplit(R))
    
    # def __merge(self, larr, Rarr):
    #     res = []
    #     while larr and Rarr:
    #         res.append(larr.pop(0) if larr[0] < Rarr[0] else Rarr.pop(0))
    #     return res + larr if len(larr) else res + Rarr


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
obj.pop()
param_3 = obj.top()
param_3 = obj.top()
