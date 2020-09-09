#Code Challenge - Take input as a string. If the input are balanced symbol pairs E.G. {}()[], return true
#if the symbols are not balanced, return false. The solution should use a stack
from stack import Stack



def is_balanced(input):
    opener_symbols = ["(", "{", "["]
    closer_symbols = [")", "}", "]"]
    symbol_stack = Stack()
    for symbol in input:
        if symbol in opener_symbols:
            symbol_stack.push(symbol)
        elif symbol in closer_symbols:
            closer_index = closer_symbols.index(symbol)
            opener_index = opener_symbols.index(symbol_stack.peek())
            if closer_index == opener_index:
                symbol_stack.pop()
    if symbol_stack.is_empty():
        return True
    else:
        return False
            
user_input = input("Please input symbols (E.G. (){[]} ) to check if they are pairs: ")
print(is_balanced(user_input))