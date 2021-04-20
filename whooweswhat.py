# Class with color codes
class color:
  GREEN = '\033[92m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  END = '\033[0m'

import numpy as np
import math

print("Hello, here you can add your individual expenses from a trip \nand see who owes what to the group!\n")

N = int(input("How many people participated: "))

if N > 10:
  print("\nWow, big group. Fun!")
print("\nNow each person can add their expenses")

# Arrays to store information about names and expenses
names = ['']
expenses = [0]
sum = 0

# Looping to get participants names and expenses 
for i in range(1,N+1):
  
  # Get each persons name
  while True:
    try: 
      names[i-1] = str(input("What is your name: "))
      names.append(names[i-1])
    except ValueError:
      print("Please use text!")
      continue
    else:
        break
    
  # Get each persons expenses 
  while True:
    try:
      expenses[i-1] = float(input("What was your expense, {}: ".format(names[i-1])))
      expenses.append(expenses[i-1])
      sum = sum + expenses[i-1]
    except ValueError:
      print("Please type in a number.")
      continue
    else:
        break

# Calculating the total expenses per person
sum_pr_person = float(sum/N)

# Solve for each participants net to the group and store in new array
net = []
for i in range(1,N+1): 
  net.append(expenses[i-1] - sum_pr_person)

# Define function to find the biggest spender, returning the name
def big_spender(e, n):
  max = 0
  for j in range(1, N): 
      if (e[j] > e[max]): 
            max = j
  return n[max]

# Just funny text stating who had the most expenses
print("EY,", color.BOLD + "{}".format(big_spender(expenses, names)) + color.END, "was the big spender!\n")

# Displays what each participant owes to total
for i in range(1, N+1):
  if (expenses[i-1] - sum_pr_person) < 0:
    print(color.RED +"{} is {:.2f} CHF in debt to the group.".format(names[i-1],net[i-1]*-1) + color.END)
  elif (expenses[i-1] - sum_pr_person) > 0:
    print(color.GREEN + "{} is owed {:.2f} CHF from the group.".format(names[i-1],net[i-1]) + color.END)
  else:
    print("{} is all squared".format(names[i-1]))

