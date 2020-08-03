#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class DeQueue:
    def __init__(self):
        self.dq = []
        
    def insertFirst(self, item):
        self.dq.insert(0, item)
        
    def insertLast(self, item):
        self.dq.append(item)
        
    def isEmpty(self):
        if len(self.dq) > 0:
            return False
        else:
            return True
        
    def popFirst(self):
        _tmp = self.dq[0]
        self.dq = self.dq[1:]
        return _tmp
    
    def popLast(self):
        _tmp = self.dq[-1]
        self.dq = self.dq[:-1]
        return _tmp
    
    def peekFirst(self):
        return self.dq[0]
    
    def peekLast(self):
        return self.dq[-1]    
    
    def print(self):
        print(self.dq)

