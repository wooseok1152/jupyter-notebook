#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Stack:
    def __init__(self):
        self.s = []
        
    def push(self, item):
        self.s.append(item)
        
    def pop(self):
        if self.isEmpty() == False: 
            return self.s.pop(-1)
        else:
            return None
        
    def peek(self):
        if self.isEmpty() == False: 
            return self.s[-1]
        else:
            return None
    
    def isEmpty(self):
        if len(self.s) > 0:
            return False
        else:
            return True
        
    def size(self):
        return len(self.s)
    
    def print(self):
        print(self.s)
        

