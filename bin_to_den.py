print("Welcome to the binary to denary converter.")
#prompt the user for a binary number
bin = input("Please put in a binary number, of any length.\n")
#creates an empty list
list_of_denary = []
#adds the numbers 2 through 9 to the list using a for-loop
for num in range(2,10):
  num = str(num)
  list_of_denary.append(num)
#uses the list to double check that the user didn't put a number other than 1 or 0
while True:
  for item in list_of_denary:
    if item in bin:
      #prompts the user for another input if there is a number other than 1 or 0
      bin = input("Only 1s and 0s, please. Input a binary number. \n")
      #prompts the user for another input if there is a letter or other non-number
    elif bin.isnumeric() == False:
      bin = input("Only 1s and 0s, please. Input a binary number. \n")
  else:
    break
#reverses the binary that the user put in (to help with indexing)
reversed_bin = bin[::-1]
#initialize both sum and i
sum = 0
i=0
#for each digit in the binary given by the user, if there's a 1, add 2 to the power of that digit's index to the running sum
while i < len(reversed_bin):
  if int(reversed_bin[i]) == 1:
    sum = sum + 2**i
  i+=1
print(bin, "in denary is:")
print(sum)
