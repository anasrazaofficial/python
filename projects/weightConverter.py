weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'K':
    pounds = float(weight) * 2.205
    print("You are " + str(round(pounds)))
else:
    kgs = float(weight) / 2.205
    print("You are " + str(round(kgs)))
