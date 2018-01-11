cases = int(raw_input())

for x in range(0, cases):

    rawInfo = raw_input()
    info = list(rawInfo)
    length = len(info)
    #print length,

    slist = []

    for i in range(0, length):
        if info[i] == '(' or info[i] == '{' or info[i] == '[' or info[i] == '<':
            slist.append(info[i])
        elif info[i] == ')':
            if not slist:
                answer = 0
                break
            if slist.pop() == '(':
                answer = 1
            else:
                answer = 0
                break
        elif info[i] == '}':
            if not slist:
                answer = 0
                break
            if slist.pop() == '{':
                answer = 1
            else:
                answer = 0
                break
        elif info[i] == ']':
            if not slist:
                answer = 0
                break
            if slist.pop() == '[':
                answer = 1
            else:
                answer = 0
                break            
        elif info[i] == '>':
            if not slist:
                answer = 0
                break
            if slist.pop() == '<':
                answer = 1
            else:
                answer = 0
                break
        else:
            pass

    if slist:
        answer = 0
    print(answer),