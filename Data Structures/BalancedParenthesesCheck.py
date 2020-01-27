OpenExp = ['{', '(', '[']
ClosedExp = ['}', ')', ']']

def isBalanced(st):
    stack = []
    for i in st:
        if i in OpenExp:
            stack.append(i)
        elif i in ClosedExp:
            indexOfExp = ClosedExp.index(i)
            if ((len(stack) > 0)  and OpenExp[indexOfExp] == stack[len(stack) - 1]):
               stack.pop()
            else:
               return 'unbalanced'
    if len(stack) == 0:
        return 'balanced'
    else:
        return 'unbalanced'
        
st = input("Enter expression : ")
print(isBalanced(st))
