import os , string, random, csv

def passNew(filenameStr, passGenComplexity):
  # Declaration of vars to ask
  passToGen = input("Number of passwords to generate?: ")
  passToGen = int(passToGen)
  lengthOfPass = input("Length of password?: ")
  lengthOfPass = int(lengthOfPass)
  # name of csv file / field names
  fields = ['value']   
  filename = str(filenameStr + ".csv")
  # writing to csv file  
  with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
    # writing the fields  
    csvwriter.writerow(fields)  
    # loop ammount of passwords / create passwords
    for passW in range(passToGen):
      genPassword = ''
      for passLeng in range(lengthOfPass):
        genPassword += random.choice(passGenComplexity)
      passRow = [{genPassword}]
      csvwriter.writerows(passRow)

def passAskGen():
  easyPass = string.ascii_letters
  mediumPass = string.ascii_letters + string.digits
  hardPass = string.ascii_letters + string.digits + string.punctuation
  print("\n=======================================================\nWhat generator would you like to use? (Enter Number)\n=======================================================")
  typeOfGen = input("\n[ 1 ] Characters Only\n[ 2 ] Characters And Numbers\n[ 3 ] Strong Password ( Charaters / Numbers / Symbols )\n=======================================================\n\nSelect Number: ")
  if typeOfGen == "1":
    filenameStr = input("What would you like to call the file?: ")
    passNew(filenameStr, easyPass)
  elif typeOfGen == "2":
    filenameStr = input("What would you like to call the file?: ")
    passNew(filenameStr, mediumPass)
  elif typeOfGen == "3":
    filenameStr = input("What would you like to call the file?: ")
    passNew(filenameStr, hardPass)
passAskGen()