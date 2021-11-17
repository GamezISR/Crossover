"""Help for the genetic algoritms
https://drive.google.com/file/d/1fwMEkJAYzw7kLqyXGVPrZ_2oi3ogPGWb/view?usp=drive_web&authuser=1
"""
import random

#makes random parent with 8 0s or 1s
def make_random_parent():
  parent = []
  for i in range(8):
    parent.append(random.randrange(2))
  return parent

#picks a single random crossover point and makes offspring
def single_crossover(p1, p2):
  single_crossover = random.randrange(1,8)

  print("Single crossover happens at " + str(single_crossover))

  temp = p1[0:single_crossover] + p2[single_crossover:8]

  temp2 = p2[0:single_crossover] + p1[single_crossover:8]

  return temp, temp2

#picks two random crossover point and makes offspring
def two_point_crossover(p1, p2):

  first_point = random.randrange(1,5)
  second_point = random.randrange(5,8)

  print("Two point crossover happens at " + str(first_point) + " and "+ str(second_point))

  temp = p1[0:first_point] + p2[first_point:second_point] + p1[second_point:8]

  temp2 = p2[0:first_point] + p1[first_point:second_point] + p2[second_point:8]

  return temp, temp2

#makes a random mask and uses it to make offspring
def uniform_crossover(p1,p2):

  mask = make_random_parent()
  count = 0
  temp = []
  temp2 = []

  print("The mask is " + str(mask))

  for parent in mask:
    if parent == 1:
      temp.append(p1[count])
      temp2.append(p2[count])
    else:
      temp.append(p2[count])
      temp2.append(p1[count])
    count += 1

  return temp, temp2

parent1 = make_random_parent()
parent2 = make_random_parent()
print("Parent 1 is " + str(parent1))
print("Parent 2 is " + str(parent2))

#print(single_crossover(parent1,parent2))
#print(two_point_crossover(parent1,parent2))
#print(uniform_crossover(parent1,parent2))
