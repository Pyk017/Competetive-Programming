import string

def evaluate(exp):
    st = []
    for i in exp:
        if i in string.digits:
            st.append(i)
        else:
            right = st.pop()
            left = st.pop()
            temp = int(eval(left + i + right))  # if input is 08/
            st.append(str(temp))

    return st[-1]



for _ in range(int(input())):
    exp = input()
    result = evaluate(exp)
    print(result)