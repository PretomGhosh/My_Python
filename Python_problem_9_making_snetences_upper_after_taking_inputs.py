sentence = []
while True:
    s = input()
    if s:
        sentence.append(s.upper())
    else:
        break
for item in sentence:
    print(item)
