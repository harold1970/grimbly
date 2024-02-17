import json
commands = ["print","add","sub","if","while","exit","ld","scan","/"]
pc = 0
a = None
b = None
x = int(0)
j = int(0)

with open('script.json', 'r') as f:
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
            if components[2] == "b":
                b = int(components[3])
            if components[2] == "x":
                x = int(components[3])
            if components[2] == "j":
                j = int(components[3])
            else:
                print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled variable: '{components[1]}'")
        if components[1] == "char":
            if components[2] == "a":
                a = str(components[3])
            if components[2] == "b":
                b = str(components[3])
            if components[2] == "j":
                print("___ERROR___ line: {pc} instruction: {instruction} | value must be numarical: '{components[3]}'")
                break
            if components[2] == "x":
                print("___ERROR___ line: {pc} instruction: {instruction} | value must be numarical: '{components[3]}'")
                break
        
        else:
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled variable type: '{components[1]}' ")
            break
    
    if components[0] == "add":
       
        a = int(b) + int(a)
    
    if components[0] == "mul":
        a = int(b) * int(a)

    if components[0] == "div":
        if components[1] == "a":
            b = b % a
        if components[1] == "b":
            a = a % b
        else:
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled variable: {componenets[1]}")

    if components[0] == "sub":
        
        if components[1] == "a":
            b = b - a
        elif components == "b":
            a = a - b
        else:
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled variable: {instruction[1]}")
            break
    
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
        elif components[2] == "<<":
            if first < second:
                pc == components[3] - 1
        elif components[2] == ">>":
            if first > second:
                pc == components[3] - 1
        elif components[2] == "<=":
            if first <= second:
                pc == components[3] - 1
        elif components[2] == ">=":
           if first >= second:
                pc == components[3] - 1
        else:
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled operator: {component[2]}")
            break
    
    if components[0] == "while":
        x = int(components[1])
        j = int(components[2])
        while j < x:
            j = j + 1
            if components[3] == "+":
                a = a + 1
            if components[3] == "-":
                a = a - 1
            if components[3] == "/":
                pc = int(components[4]) 
            else:
                print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled operator: {componenet[3]}")
                break
    
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
