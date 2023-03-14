print("Welcome to the denary to binary converter.")
num = input("First, please write a number.\n")
num = int(num) * 2
bin_list = []
mod_num =int(num/2)
while mod_num != 0:
  if mod_num % 2 == 0:
    bin_list.append(0)
  elif mod_num % 2 != 0:
    bin_list.append(1)
  mod_num = int(mod_num/2) 
bin_list = bin_list[::-1]
output = ""
for bit in bin_list:
  output = output + str(bit)
while len(output) < 8:
  output = str(0) + output
print(output)
