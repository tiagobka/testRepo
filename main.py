# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def newFunctionBranch1_firstOne(argument):
    print('hello This is a new function', argument)

def newFunctionBranch2_firstOne(argument):
    print('hello This is a new function', argument, "from branch2")

def newFunctionBranch2_secondOne(argument):
    print('hello This is a new function', argument)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    newFunctionBranch1_firstOne("it works")
    newFunctionBranch2_firstOne("Sup")
    newFunctionBranch2_secondOne("dup")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
