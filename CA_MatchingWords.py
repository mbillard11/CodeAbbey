text = raw_input().split()
text = sorted(text)
password = [0]
for i in range(0, len(text)-1):
    if text[i] == text[i+1]:
        if password[-1] != text[i]:
            password.append(text[i])
for x in password[1:]:
    print x,