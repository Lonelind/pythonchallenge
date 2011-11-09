mess = open("02.txt").read()
dict = {}
for ch in mess:
    dict[ch] = dict.get(ch, 0) + 1

res = ""

for ch in mess:
    if dict[ch] == 1:
        res += ch
print res
