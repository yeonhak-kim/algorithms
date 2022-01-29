# Min Stack (leetcode)

class MinStack:
    
    def __init__(self):
        self.arr = []
        self.arr_min = float('inf')

    def push(self, val: int) -> None:
        self.arr.append(val)
        if val < self.arr_min:
            self.arr_min = val

    def pop(self) -> None:
        element = self.arr.pop()
        if self.arr_min == element:
            update_min = float('inf')
            for num in self.arr:
                update_min = min(update_min, num)
            
            self.arr_min = update_min
        
        return element
        
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        if not self.arr: return None
        
        return self.arr_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()