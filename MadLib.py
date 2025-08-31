#MadLib.py
#Name: Alexa Falkner
#Date: 8/31/2025
#Assignment: MadLib

def main():
  print("Madlib")
  #Ask user for words
  adjective1= input("Enter a adjective: ") 
  pluralnoun1= input("Enter a plural noun: ")
  adjective2= input("Enter another adjective: ")
  noun1= input("Enter a noun:")
  noun2= input("Enter another noun:")
  realtive= input("Enter a realtive you know: ")
  adjective3= input("Enter another adjective: ")
  #Print the story with the user supplied words.
  print("On a dark and " + adjective1 + " Halloween night," + pluralnoun1 + " roamed the streets ")
  print("in search of " + adjective2 + " treats.")
  print("Suddenly, a " + noun1 + " jumped out from behind a " + noun2 + " and startled everyone.")
  print("It turned out to be " + realtive + " in a clever costume, ready to join in the " + adjective3 + " festivities.")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
