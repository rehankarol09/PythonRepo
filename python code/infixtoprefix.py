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
def infixtoprefix(inf):
    prefix=" "
    st=Stack()
    rev = ''
    for i in range(len(inf) - 1, -1, -1):
        ch = inf[i]
        if ch == '(':
            ch = ')'
        elif ch == ')':
            ch = '('
        rev += ch
    print("Before operation", rev)
    inf=rev
    for i in inf:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            prefix=prefix+i
        elif i == '(':
            st.push(i)
        elif i == ')':
            while not st.is_empty() and st.peek() !='(':
                prefix=prefix+st.peek()
                st.pop()
            if st.peek() == '(':
                st.pop()
        elif isopeartor(i):
            if st.is_empty():
                st.push(i)
            elif precdence(i) > precdence(st.peek()):
                st.push(i)
            elif precdence(i) == precdence(st.peek()) and i == '^':
                while precdence(i) == precdence(st.peek()) and i == '^':
                    prefix=prefix+st.peek()
                    st.pop()
                st.push(i)
            elif precdence(i)==precdence(st.peek()):
                st.push(i)
            else:
                while not st.is_empty() and precdence(i)<precdence(st.peek()):
                    prefix = prefix + st.peek()
                    st.pop()
                st.push(i)
    while not st.is_empty():
        prefix=prefix+st.peek()
        st.pop()
    prefix=prefix[::-1]
    return prefix
print("Enter your infix expression")
exp=str(input())
print("Infix expression", exp)
r=infixtoprefix(exp)
print("Prefix Expression", r)