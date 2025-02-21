emailText = '''
Dear Sir,
    This is to write you that...

Regards,
ABC
'''
print(emailText)

course = "Python"
print(course[0])
print(course[-1])
print(course[0:3])
print(course[2:])
print(course[:3])

# Template literals
firstName = "Anas"
lastName = "Raza"
name = f"My Name is {firstName} {lastName}"
print(name)

# Methods
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('t'))
print(course.replace("on", "up"))
print("on" in course)
print("On" in course)
