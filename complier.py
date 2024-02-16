import json
commands = ["print","add","sub","if","while","exit","ld","scan","/"]
pc = 0
a = int(0)
b = int(0)
x = int(0)
j = int(0)

with open('script.json', 'r') as f:
    script = json.load(f)
while True:
    # print(a)
    instruction = script[pc]
    components = instruction.split('|')
    if components[0] not in commands:
        print(f"___ERROR___ line:{pc} instruction:{instruction}")
        break
    if components[0] == int:
        print(components[0])
    
    if components[0] == "print":
        # print comp 1
        if components[1] == "a":
            print(a)
        elif components[1] == "b":
            print(b)
    
        else:
            print(component[1])

    if components[0] == "exit":
        break

    if components[0] == "ld":
        
        if components[1] == "int":
            if components[2] == "a":
                a = int(components[3])
            if components[2] == "b":
                b = int(components[3])
            if components[2] == "x":
                x = int(components[3])
            if components[2] == "j":
                j = int(components[3])
        
        if components[1] == "char":
            if components[2] == "a":
                a = str(components[3])
            if components[2] == "b":
                b = str(components[3])
            if components[2] == "j":
                print("value must be numarical")
            if components[2] == "x":
                print("value must be numarical")

    if components[0] == "add":
        a = int(b) + int(a)
    if components[0] == "sub":
        if components[1] == "a":
            a = b - a
        if components == "b":
            b = a - b
        else:
            print("varible not found")
            
    if components[0] == "if":
        if components[1] == "a":
            first = a
            second = b
        if components[0] == "b":
            first = b
            second = a
        if components[2] == "==":
            if first == second:
                pc == components[3] - 1
        if components[2] == "<<":
            if first < second:
                pc == components[3] - 1
        if components[2] == ">>":
            if first > second:
                pc == components[3] - 1
        if components[2] == "<=":
            if first <= second:
                pc == components[3] - 1
        if components[2] == ">=":
           if first >= second:
                pc == components[3] - 1
        
    if components[0] == "while":
        x = int(components[1])
        j = int(components[2])
        while j < x:
            j = j + 1
            if components[3] == "+":
                a = a + 1
            if components[3] == "-":
                a -= 1
            if components[3] == "/":
                pc = int(components[4]) 

    if components[0] == "scan":
        a = input(components[1])

                
    pc = pc + 1
