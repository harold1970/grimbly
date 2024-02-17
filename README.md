


The Grimbly interpreter is a program designed to read and execute instructions written in a custom scripting language. It loads a script from a grimbly (renamed json file) file, parses each instruction, and performs corresponding actions based on those instructions.
Key Components:

# Commands: 
The interpreter recognizes several commands, each with specific functionalities. These commands include:
* print: Print the value of a variable.
* add: Perform addition operation.
* sub: Perform subtraction operation.
* if: Conditional branching based on comparison.
* for: Loop execution based on condition. (depricated)
* var: Placeholder for potential future variable handling.
* Placeholder for potential future functionality.
* exit: Terminate the script execution.
* ld: Load a value into a variable.
* scan: Prompt the user for input.

# Variables: 
*   The interpreter supports the use of variables to store and manipulate values. Variables include a, b, x, and j.

# Script Loading:

*    The interpreter loads the script from a JSON file specified as script.json.
*    Each instruction in the script file is represented as a JSON array element.

# Execution Flow:

*   The interpreter reads the script sequentially, executing each instruction one by one.
*  It parses each instruction, identifies the command and its arguments, and performs the corresponding action.
* Execution continues until the end of the script is reached or until a termination command (exit) is encountered.

# Error Handling:

*    The interpreter includes basic error handling to detect and report invalid instructions or unrecognized commands.
*    Error messages provide information about the line number and the nature of the error encountered during script execution.

# Example Script:

json

    [
        "ld|char|a|hello world",
        "print|a",
        "exit"
    ]

# Supported Commands:

*    print: Usage: print|*variable* or *int* or *char*. Prints the value of the specified variable to the output.
*    add: Usage: add. Performs addition operation.
*    sub: Usage: sub. Performs subtraction operation.
*    if: Usage: if|*variable*|*comparison_operator*|*target_instruction*. Conditional branching based on comparison.
*    while: Usage: while|*limit*|*current_value*|*operation*|*target_instruction*. Loop execution based on condition. (deprecated)
*    exit: Usage: exit
*    ld: Usage: ld|*type(*"char"* or *"int"* )*|*variable*|*value*
*    scan: Usage: scan|*prompt_message*
*    /: Usage: /|*comment*  
# Future Enhancements:

*   Support for additional commands and functionalities.
*   Improved error handling and error reporting mechanisms.
*   Optimization of execution speed
*   adding the ability to *if then exit*
