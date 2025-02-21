isHotDay = False
isColdDay = True

if isHotDay:
    print("Hot day")
    print("Drink water")
elif isColdDay:
    print("Cold day")
    print("Wear warm clothes")
else:
    print("A lovely day")

# Logical operators
hasMoney = True
hasCriminalRecord = True

if hasMoney and not hasCriminalRecord:
    print("Eligible buyer")
else:
    print("Ineligible buyer")
