#FirstProgram.py
#Name: Alexa Falkner
#Date: 8/31/2025
#Assignment:Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello")
  #Ask for the user's name
  name = input ("What is your name? ")
  #Use the user's name in the program.
  print("Hello " + name)
  #Ask the user for their age.
  age = int(input("What is your age? "))
  import datetime
  curryr = datetime.date.today().year
  birthyr = curryr-age
  print("You were born in year: ")
  print(birthyr)
  print("Or you were born in :")
  print(birthyr + 1)
  print("if you haven't had your birthday yet! ")
  #Assume that they have not had their birthday yet this year.
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
