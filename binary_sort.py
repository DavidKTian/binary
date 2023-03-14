list_to_sort = []
print("Write some integers, please. When done, write \"done\".")
while True:
  number = input("")
  if number == "done" or number.lower() == "done":
    break
  try:
    number = int(number)
  except:
    print("Write integers only, please.")
    continue
  list_to_sort.append(number)
length = len(list_to_sort)
num_of_times = (length - 1) **2 
while num_of_times > 0:
  for i in range(0,length-1):
    if list_to_sort[i]>list_to_sort[i+1]:
      num1 = list_to_sort[i]
      num2 = list_to_sort[i+1]
      list_to_sort[i] = num2
      list_to_sort[i+1] = num1
      num_of_times = num_of_times - 1
    elif list_to_sort[i] < list_to_sort[i+1]:
      num_of_times = num_of_times - 1
      continue 
print(list_to_sort)
