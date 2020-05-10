Open = '{(['
Close = '})]'

def isBalanced(st):
    stack = []
    for i in st:
        if i in Open:
            stack.append(i)
        elif i in Close:
            indexOfExp = Close.index(i)
            if ((len(stack) > 0)  and Open[indexOfExp] == stack[len(stack) - 1]):
               stack.pop()
            else:
               return 'unbalanced'
    if len(stack) == 0:
        return 'balanced'
    else:
        return 'unbalanced'
        
st = input("Enter expression : ")
print(isBalanced(st))


''' If an element is an opening delimeter then it is pushed into the stack.
    When a closing delimeter is encountered there is a removal from the stack top.
'''