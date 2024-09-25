def q1():
  bool1 = True
  print(bool1)

def q2():
  bool1 = input("Input an integer: ")
  print(bool1 > '5')

def q3():
  bool1 = input("Input the letter a:")
  print(bool1 == 'a')

def q4():
  bool1 = input("Input a word earlier in the dictionary than google: ")
  print(bool1 < 'google')

def q5():
  bool1 = int(input("Input an integer: "))
  bool2 = int(input("Input another integer: "))
  print(f"Your numbers multiplied together are greater than 40: {bool1 * bool2 > 40}")

#Do edit the code below
#Comment the lines below when running your tests

q1()
q2()
q3()
q4()
q5()
