import sys

s = sys.argv
s = s[1:]

dict1 = {}
for i in range(0, len(s) - 1, 2):
    dict1[s[i]] = int(s[i + 1])

dict2 = dict.fromkeys(['1-18', '18-40', '40-65', '65+'])

newvalues018 = []
newvalues1840 = []
newvalues4065 = []
newvalues65 = []
for k, v in dict1.items():
    if 0 < v <= 18:
        newvalues018.append(k)
    elif 18 < v <= 40:
        newvalues1840.append(k)
    elif 40 < v <= 65:
        newvalues4065.append(k)
    elif 65 < v:
        newvalues65.append(k)

dict2 = {'1-18': newvalues018, '18-40': newvalues1840, '40-65': newvalues4065, '65+': newvalues65}
(dict2)


print(dict2)