import sys

s = sys.argv
s = s[1:]
s = [int(elem) for elem in s]

def norepeat(lst):
    for i in range(len(lst)):
        equal = False
        for j in range(len(lst)):

            if i != j:
                z = lst[i] ^ lst[j]
                if z == 0:
                    equal = True
                    break
        if equal == False:
            return lst[i]


result = norepeat(s)
print(result)

#Գիտեմ շատ բարդ ձև եմ մտածել, բայց այլ կերպ չհասկացա, ինչպես օգտագործեմ ^ սիմվոլը ))

# l=[1,2,2,1,3,5,5,1]
# print(min(l,key=l.count))

# Սա ավելի պարզ տարբերակ է, բայց օգնել են )))