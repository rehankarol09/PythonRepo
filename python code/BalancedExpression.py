from definedsizestack import Stack
def is_valid(expr):
    st=Stack()
    for ch in expr:
        if ch in '({[':
            st.push(ch)
        if ch in ')}]':
            if st.is_empty():
                print("Right is more than left")
                return False
            else:
                char=st.pop()
                if not matchmaking(char,ch):
                    print("Invalid Expression not matching")
                    return False
    if st.is_empty():
        print("Valid Expression")
        return True
    else:
        print("Left is more than right paranthesis")
        return False

def matchmaking(a,b):
    if a == '[' and b == ']':
        return True
    if a == '{' and b == '}':
        return True
    if a == '(' and b == ')':
        return True
    return False

while True:
    print("Enter the Expression")
    exp=input()
    if exp=='q':
        break
    if is_valid(exp):
        print("Valid Expression")
    else:
        print("Invalid Expression")

