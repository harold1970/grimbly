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
    def __str__(self):
        self._value = str(self._value)
        return self.Value
    def __repr__(self):
        self._value = int(self._value)
        return self.Value
    def __add__(self, rhs):
       if self.Type is int:
           return int(self.Value) + int(rhs.Value)
       if self.Type is str:
           raise f"{self.Value} + {rhs.Value}"

class UserFunction:
    def __init__(self, name, startPc, endPc, _return):
        self.StartPc = startPc
        self.Name = name
        self.EndPc = endPc
        self.ReturnTo = _return


commands = {
"print": False,
"add": False,
"sub": False,
"if": False, 
"exit": False, 
"ld": False,
"scan": False,
"/": False,
"mul": False,
"div": False,
"ifexit":False,
"import": False,
"while": True,
"function": False,
"import": False,
"mov": False
}
pc = 0
a = None
b = None
x = int(0)
j = int(0)
lx = 0
endPc = 0
userVars = {}
userFunctions = {}
store = None
first = None
second = None
if len(sys.argv) != 2:
    print("Usage: python3 compiler.py <filename>")
    sys.exit(1)

filename = sys.argv[1]


def custom_import(libraryname):
    if library_name == "additional_functions":
        print("Library imported successfully!")
    else:
        print("Library not found!")


try:
    with open(filename, 'r') as f:
        script = json.load(f)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    sys.exit(1)
if "exit" not in script:
    print("___ERROR___ no exit command")
 
while True:     
    
     
    if pc == endPc:
        pc = lx
          
    instruction = script[pc]
    components = instruction.split('|')
    if components[0] not in commands and not userFunctions:
        print(f"___ERROR___ line:{pc} instruction:{instruction} invaled command")
        break
   
    if components[0] == int:
        print(components[0])
    


    
    # print command   
    if components[0] == "print":
        if components[1] == "char":
            print(components[2])
        elif components[1] == "var":
            print(userVars[components[2]])
        else:
            print(f"___ERROR___ line:{pc} instruction:{instruction} invaled component: {components[1]}")
  # exit command
    if components[0] == "exit":
        break
            
    # load command		
    if components[0] == "ld":
                
        if components[1] == "int":
            userVars[components[2]] = UserVar(components[2],components[3], int)  
    
        elif components[1] == "char":
            userVars[components[2]] = UserVar(components[2],components[3], str)  
    
    if components[0] == "mov":
        if components[1] in userVars and components[2] in userVars:
            userVars[components[1]] = userVars[components[2]]
           
        
        
        
    # add command
    if components[0] == "add":
        right = userVars[components[2]]
        left = userVars[components[3]]
        store = left + right
        userVars[components[1]] = store
        

    if components[0] == "div":
        right = userVars[components[1]]
        left = userVars[components[3]]
        store = left / right
        userVars[components[1]] = store
    
    if components[0] == "sub":
        right = userVars[components[2]]
        left = userVars[components[3]]
        store = left - right
        userVars[components[1]] = store
        # if command     
    # 1 = type 2 = first 3 = function 4 = pc 5 = pc if false
    if components[0] == "if":
        if components[1] == "int":
            if components[2] not in userVars:
                first = int(components[2])
            else:
                first = userVars[components[2]]
            if components[4] not in userVars:
                second = int(components[4])
            else:
                second = userVars[components[4]]      
        
        if components[1] == "char":
            if components[2] not in userVars:
                first = str(components[2])
            else:
                first = userVars[components[2]]
            if components[4] not in userVars:
                second = str(components[4])
            else:
                second = userVars[components[4]]
            
        if components[3] == "==":
            if first == second:
                pc = int(components[5])
        elif components[3] == "<<":
            if first < second:    
                pc = int(components[5])
        elif components[3] == ">>":
            if first > second:    
                pc = int(components[5])
        elif components[3] == "<=":
            if first <= second:   
                pc = int(components[5]) 
        elif components[3] == ">=":
            if first >= second:    
                pc = int(components[5])
        elif components[3] == "!=":
            if first != second:
                pc = int(components[5])
        else:                     
            print(f"___ERROR___ line: {pc} instruction: {instruction} | invaled operator: {components[2]}")
            break

	# scan command
    if components[0] == "scan":
        if components[1] == "int": 
            userVars[components[2]] = UserVar(components[2], input(components[3]), int)  
        if components[1] == "char":
            userVars[components[2]] = UserVar(components[2], input(components[3]), str)
        else:
            print(f"___ERROR___ unkown type {components[1]}, line: {pc}")

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
       
    if components[0] == "function":
        if components[1] in commands:
            print(f"___ERROR___ line: {pc}, name of function must be differant then a prexsiting command, {commands}")
        else:
            userFunctions[components[1]] = UserFunction(components[1],components[2],components[3],components[4])
    
    if components[0] in userFunctions:
        lx = int(userFunctions[components[0]].ReturnTo)
        endPc = int(userFunctions[components[0]].EndPc)
        pc = int(userFunctions[components[0]].StartPc)   
          
    

    pc = int(pc) + 1
