while(True):
    sentence = input()  # 사용자로부터 문장을 입력받음
    if(sentence == "."):  # 입력받은 문장이 "."이면 반복문 종료
        break
    stack = []  # 괄호를 저장할 스택 초기화

    for i in sentence:  # 문장의 각 문자에 대해 반복
        if(i == "(" or i == "["):  # 여는 괄호인 경우
            stack.append(i)  # 스택에 추가
        if(i == ")"):  # 닫는 소괄호인 경우
            if(len(stack) != 0 and stack[-1] == "("):  # 스택이 비어있지 않고, 마지막 요소가 여는 소괄호인 경우
                stack.pop()  # 스택에서 마지막 요소 제거 (짝이 맞는 경우)
            else:
                stack.append(")")  # 짝이 맞지 않는 경우 스택에 추가하고 반복문 종료
                break
        if(i == "]"):  # 닫는 대괄호인 경우
            if(len(stack) != 0 and stack[-1] == "["):  # 스택이 비어있지 않고, 마지막 요소가 여는 대괄호인 경우
                stack.pop()  # 스택에서 마지막 요소 제거 (짝이 맞는 경우)
            else:
                stack.append("]")  # 짝이 맞지 않는 경우 스택에 추가하고 반복문 종료
                break

    if(len(stack) == 0):  # 스택이 비어있으면 (모든 괄호가 짝이 맞는 경우)
        print("yes")  # "yes" 출력
    else:
        print("no")  # 그렇지 않으면 "no" 출력
