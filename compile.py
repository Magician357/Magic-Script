import sys

class argumentError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def compile(text):
    full=text.split("\n")
    for line in full:
        pass

if __name__ == "__main__":
    arguments=sys.argv
    if len(arguments) < 2:
        raise argumentError("Not enough arguments")
    with open(arguments[1],"r") as f:
        text=f.read()
    print("File retrieved")
    print("Beginning compiling...")