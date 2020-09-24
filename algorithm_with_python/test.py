import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\1. 가장 큰 수\in1.txt")

input_int, m = input().split()
m = int(m)
input_list = []
for i in range(len(input_int)):
    
    input_list.append(int(input_int[i]))

def find_maximum(m, input_list):
    
    count = 0
    stack = []
    picked_number = input_list.pop(0)
    stack.append(picked_number)
    for i in range(0, len(input_list)):
        
        picked_number = input_list.pop(0)
        while True:
            
            if len(stack) == 0:
                
                stack.append(picked_number)
                break
                
            elif stack[-1] < picked_number:
                
                stack.pop()
                count = count + 1
                
            elif stack[-1] >= picked_number:
                
                stack.append(picked_number)
                break
            
            if count == m :
                
                stack.append(picked_number)
                break
        
        if count == m :
            
            break
        
    if count != m:
        
        for i in range(m - count):
            
            stack.pop()
        
    if len(input_list) != 0:
        
        for i in input_list:
            
            stack.append(i)
        
    result = ""
    for i in stack:
        
        result = result + str(i)
        
    print(result)
    
find_maximum(m, input_list)