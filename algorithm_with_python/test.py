input_int = "5276823"
m = 3
input_list = []
for i in input_int:
    
    input_list.append(int(i))
    
count = 0
stack = []

for i in range(len(input_list)):
    
    picked_value = input_list.pop(0)
    while stack and stack[-1] < picked_value :
        
        stack.pop()
        count = count + 1
        if count == m:
            
            break
    
    stack.append(picked_value)
    if count == m:
        
        break
        
if len(input_list) != 0:
    
    for i in input_list:
        
        stack.append(i)
        
if count != m :
    
    for i in range(m - count):
        
        stack.pop()
        
print(stack)