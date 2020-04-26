myDict = {}

while True:
    userName = raw_input("Enter a name: ")
    if userName == "":
        break
    else:
        phone = raw_input("Enter a phone number: ")
        dob = raw_input("Enter date of birth: ")
        ssn = raw_input("Enter social security: ")
        
    myDict[userName] = [phone,dob,ssn]
    print "Name,phone,dob,ssn"
    for i in myDict.keys():
        for k in myDict[i]:
         i = i + "," + k
    print i

