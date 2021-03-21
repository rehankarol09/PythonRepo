from definedsizestack import Stack
def isopeartor(c):
    if c == '+' or c == '-' or c == '/' or c == '*' or c == '^':
        return True
    else:
        return False
def precdence(c):
    if c =='+' or c == '-':
        return 1
    elif c == '/' or c == '*':
        return 2
    elif c == '^':
        return 3
    else:
        return -1

def infixtpostfix(inf):
    postfix=" "
    st=Stack()
    i=0
    for i in inf:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            postfix=postfix+i
        elif i == '(':
            st.push(i)
        elif i == ')':
            while not st.is_empty() and st.peek() !='(':
                postfix=postfix+st.peek()
                st.pop()
            if st.peek() == '(':
                st.pop()
        elif isopeartor(i):
            if st.is_empty():
                st.push(i)
            elif precdence(i) > precdence(st.peek()):
                st.push(i)
            elif precdence(i) == precdence(st.peek()) and st.peek() == '^':
                st.push(i)
            else:
                while not st.is_empty() and precdence(i)<=precdence(st.peek()):
                    postfix = postfix + st.peek()
                    st.pop()
                st.push(i)
    while not st.is_empty():
        postfix=postfix+st.peek()
        st.pop()
    return postfix

print("Enter your infix expression")
exp=str(input())
print("Infix expression", exp)
print("Postfix Expresion")
r=infixtpostfix(exp)
print(r)