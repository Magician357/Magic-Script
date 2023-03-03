# python3 Magic-Script/compile.py Magic-Script/text.masc

import sys

class argumentError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def parse_var(text):
    text=text.replace("\n","")
    variables = {}
    line_number = 0
    for line in text.split(";"):
        if line.startswith("let "):
            temp = line[4:].replace(" ", "").split(":")
            variables[temp[1].split("=")[0]] = (temp[0], temp[1].split("=")[1], line_number)
        line_number += 1
    return variables

def parse_funcs(text):
    pass

if __name__ == "__main__":
    arguments=sys.argv
    if len(arguments) < 2:
        raise argumentError("Not enough arguments")
    with open(arguments[1],"r") as f:
        text=f.read()
    print("File retrieved")
    print("Beginning compiling...")
    variables=parse_var(text)
    print("Done")
    print(variables)