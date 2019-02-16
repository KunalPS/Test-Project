
# Python 3

# raw_input() is used to read textstring form the user in python2 and input() is used to read integer
# In python 3 input is used to read both string and integer from the user(Every input is condidered as string 'Str()')name
name=input("Your name please!!")
age= input("and your age..")
if name!='':
  if int(age)>30:
    print("Hello, "+ name + "You are old")
  else:
    print("Hello, " + name)
else: 
  print("Hello, World")
