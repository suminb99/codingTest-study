def isBalanced(text):
    stack = []

    for ch in text:
        if (ch not in "()[]"): continue

        if (ch in "(["):
            stack.append(ch)

        else:
            if not stack: return False
            elif (ch == ')' and stack[-1] == '('): stack.pop()
            elif (ch == ']' and stack[-1] == '['): stack.pop()
            else: return False

    return not stack


while True:
    text = input()
    if (text == '.'): break

    if (isBalanced(text)): print("yes")
    else: print("no")