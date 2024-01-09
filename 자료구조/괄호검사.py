def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ('{' , '[' ,'('): #열리는 괄호 스택에 삽입
            stack.push(ch)
        elif ch in ('}',']',')'): # 닫히는 괄호시 스택 비어있으면...
            if stack.isEmpty() :
                return False
            else : #쌍이 맞지 않을때
                left = stack.pop()
                if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "(") :
                       return False
    return stack.isEmpty()               