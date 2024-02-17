import json

commands = ["print","add","sub","if","for","exit","ld","scan","/","mul","div"]
pc = 0
a = None
b = None
x = int(0)
j = int(0)

with open('script.grimbly', 'r') as f:
    script = json.load(f)
while True:
    # print(a)
    instruction = script[pc]
    components = instruction.split('|')
    if components[0] not in commands:
        print(f"___ERROR___ line:{pc} instruction:{instruction} invaled command")
        break
    if components[0] == int:
        print(components[0])
    
    if components[0] == "print":
        # print comp 1
        if components[1] == "a":
            if a == None:
                print(f"Null")
            else:
                print(f"{a}")
        elif components[1] == "b":
            if b == None:
                print("Null")
            else:
                print(f"{b}")
        else:
            print(component[1])

    if components[0] == "exit":
        break

    if components[0] == "ld":
        
        if components[1] == "int":
            
            if components[2] == "a":
                a = int(components[3])
            elif components[2] == "b":
                b = int(components[3])
            elif components[2] == "x":
                x = int(components[3])
            elif components[2] == "j":
                j = int(components[3])
            else:
                print("___ERROR___ line: {pc} instruction: {instruction} | unknow variable: '{components[2]}'")
                break
        elif components[1] == "char":
            if components[2] == "a":
                a = str(components[3])
            elif components[2] == "b":
                b = str(components[3])
            
            elif components[2] == "j":
                print("___ERROR___ line: {pc} instruction: {instruction} | value must be numarical: '{components[3]}'")
                break
            elif components[2] == "x":
                print("___ERROR___ line: {pc} instruction: {instruction} | value must be numarical: '{components[3]}'")
                break
            
            else:
                print("___ERROR___ line: {pc} instruction: {instruction} | unknow variable: '{components[2]}'")
                break 
        else:
            print("___ERROR___ line: {pc} instruction: {instruction} | unknow variable: '{components[2]}'")
    if components[0] == "add":
        if components[1] == "a":     
            a = int(b) + int(a)
        elif components[1] =="b":
            b = int(b) + int(a)
    
    if components[0] == "mul":
        if components[1] == "a":     
            a = int(b) * int(a)
        elif components[1] =="b":
            b = int(b) * int(a)
    

    if components[0] == "div":
        if components[1] == "a":
            if components[2] == "b":    
                b = b / a
            elif components[2] == "a":
                a = b / a
        elif components[1] == "b":
            if components[2] == "a":
                a = a / b
            if components[2] == "b":
                b = a / b

        else:
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled variable: {components[1]}")
            break
    if components[0] == "sub":
        if components[1] == "a":
            if components[2] == "b":    
                b = b - a
            elif components[2] == "a":
                a = b - a
        elif components == "b":
            if components[2] == "a":
                a = a - b
            if components[2] == "b":
                b = a - b
        
        else:
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled variable: {instruction[1]}")
            break
    
    if components[0] == "if":
        if components[1] == "a":
            first = a
            second = b
        elif components[1] == "b":
            first = b
            second = a
        
        if components[2] == "==":
            if first == second:
                pc = int(components[3])
        elif components[2] == "<<":
            if first < second:    
                pc = int(components[3])
                print("hello world")
        elif components[2] == ">>":
            if first > second:    
                pc = int(components[3])
        elif components[2] == "<=":
            if first <= second:   
                pc = int(components[3]) 
        elif components[2] == ">=":
           if first >= second:    
                pc = int(components[3])
        else:                     
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled operator: {components[2]}")
            break
    # c1 = x c2 = j c3 = op c4 = jmp to
    if components[0] == "for":
       # variables ############
        if components[1] == "a":
            x = int(a)
        elif components[1] == "b":
            x = int(b)
        ########################
        # number
        else:    
            x = int(components[1])
        ########################## x    
        if components[2] == "a":
            j = int(a)

        elif components[2] == "b":
            j = int(b)

        else: #j
            j = int(components[2])
        
        while x <= (j):
            print(f"loop j: {j} x: {x}")
            if components[3] == "+":
                x = x + 1
            
            elif components[3] == "-":
                x = x - 1
            else:
                print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled operator: {components[2]}")
                break 
            if j != x:
                pc = int(components[4]) 
                 


    if components[0] == "scan":
        if components[1] == "a":  
            a = input(components[2])
        
        if componenets[1] == "b":
            b = input(components[2])
        
        if componenets[1] == "j":
            j = int(input(componenets[2]))
        
        if componenets[1] == "x":
            x = int(input(componenets[2]))
        
        else:
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled variable: {componenets[2]}")
            break
    
    
    pc = pc + 1
