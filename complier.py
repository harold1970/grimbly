import json
import sys
import os
class UserVar:
    def __init__(self, name, val=None, target=None):
        self.Type = target
        self.Name = name
        if target == int:
            self._value = int(val)
        else:
            self._value = str(val)
    @property
    def Value(self):
        return self._value
    @Value.setter
    def Value(self, val):
        self._value = self.Type(val)
    
    def __repr__(self):
        return self.Value
    def __add__(self, rhs):
        if self.Type is not rhs.Type:
            raise Exception("Can't add different types")
        if self.Type is int:
            return self.Value + rhs.Value
        if self.Type is str:
            raise f"{self.Value} + {rhs.Value}"
   
commands = {
"print": False,
"add": False,
"sub": False,
"if": True, 
"for": True, 
"exit": False, 
"ld": False ,
"scan": False,
"/": False,
"mul": False,
"div": False,
"ifexit": False,
"jmp": False,
"import": False,
"while": True
			}
pc = 0
a = None
b = None
x = int(0)
j = int(0)
userVars = {}

store = None
first = None
second = None
if len(sys.argv) != 2:
    print("Usage: python3 compiler.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        script = json.load(f)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    sys.exit(1)

if "exit" not in script:
    print("___ERROR___ no exit command")
    exit
while True:     
          
    instruction = script[pc]
    components = instruction.split('|')
    if components[0] not in commands:
        print(f"___ERROR___ line:{pc} instruction:{instruction} invaled command")
        break
   
    if components[0] == int:
        print(components[0])
     
     # print command   
    if components[0] == "print":
        if components[1] not in userVars:
            print(components[1])
        else:
            print(userVars[components[1]])
	
    # exit command
    if components[0] == "exit":
        break
            
                
    # load command		
    if components[0] == "ld":
                
        if components[1] == "int":
            if components[2] not in userVars:
                userVars[components[2]] = UserVar(components[2],components[3], int)
            else:
                userVars[components[2]] = UserVar(components[2],components[3], int)  

        elif components[1] == "char":
            if components[2] not in userVars:
                userVars[components[2]] = UserVar(components[2],components[3], str)  
            else:
                userVars[components[2]] = UserVar(components[2],components[3], str)  
    # add command
    if components[0] == "add":
        right = userVars[components[2]]
        left = userVars[components[3]]
        store = left + right
        userVars[components[1]] = store
        


    # mul command            
    if components[0] == "mul":
        if components[1] == "a":     
            a = int(b) * int(a)
        elif components[1] =="b":
            b = int(b) * int(a)
            
       # div command     
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
    #sub command
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
       # if command     
    if components[0] == "if":
        if components[1] == "a":
            first = a
            second = b
        elif components[1] == "b":
            first = b
            second = a
        elif components[1] == "g":
            h = 1
            g = 1
            first = g
            second = h

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
    # jmp command
    if components[0] == 'jmp':
        
        if components[1] == 'a':
            first = a
        if components[1] == 'b':
        	first = b
        
        if components[3] == 'a':
            second = a
        elif components[3] == 'b':
            second = b

        if components[2] == '==':
            if first == second:
                pc = components[4]
        elif components[2] == '<':
            if first < second:
                pc = components[4]
        elif components[2] == '>':
            if first > second:    
                pc = components[4]
        elif components[2] == '!':
            if first != second:
                pc = components[4]
        elif components[2] == '<=':
            if first <= second:
                pc = components[4]
        elif components[2] == '>=':
            if first >= second:    
                pc = components[4]

    # c1 = x c2 = j c3 = op c4 = jmp to
    # for command
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
                 

	# scan command
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
    # if exit command
    if components[0] == "ifexit":
        if components[1] == "a":
            first = a
            second = b
        elif components[1] == "b":
            first = b
            second = a
        
        if components[2] == "==":
            if first == second:
                break
        elif components[2] == "<<":
            if first < second:    
                break

        elif components[2] == ">>":
            if first > second:    
                break
           
        elif components[2] == "<=":
            if first <= second:   
                break
        elif components[2] == ">=":
           if first >= second:    
                break
        else:                     
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled operator: {components[2]} \n")
            break
          
    
              
    pc = int(pc) + 1
