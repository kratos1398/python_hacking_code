lambda mytuple: mytuple[1]
# everything in line 1, is the same as:
myList = []

def returnSecondValue(mytuple):
    return mytuple[1]

# files.sort(key=lambda filename: filename[1], reverse=True)
# is the same as:
trackingList = []
for i in myList:
    trackingList.append(returnSecondValue(i))
    trackingList.sort(reverse=True)
