# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.cur_idx = 0;
        self.nestedList = nestedList
        self.flatten()
    def flatten(self):
        cnt = 0
        while cnt < len(self.nestedList):
            while not self.nestedList[cnt].isInteger():
                innerList = self.nestedList[cnt].getList()
                for i in range(len(innerList)):  
                    self.nestedList.insert(cnt+i+1, innerList[i])
                del self.nestedList[cnt]
                if cnt >= len(self.nestedList):
                    break
            cnt += 1;
    def next(self) -> int:
        self.cur_idx += 1;
        return self.nestedList[self.cur_idx-1].getInteger()
    def hasNext(self) -> bool:
        if len(self.nestedList) <= self.cur_idx:
            return False
        else:
            return True
                
            
        
            
        
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
