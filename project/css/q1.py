operation=input()
if operation =="push":
    stack=list(map(int,input(.split())))
elif operation=="remove":
    stack.pop()
elif operation=="show":
    print(stack)

