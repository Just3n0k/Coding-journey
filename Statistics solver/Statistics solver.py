from math import *

print("Statistics solver\n")

Data = open("Datafile.txt", "r")
d = Data.readlines()

stats = []

for line in d:
    stats.append(line.strip()) #removes "\n"

stats.sort()

print(f"Data:{stats}\n") 

total_stats = 0

for num in stats:
    total_stats += int(num) #adds all the numbers in list
   
mean = round(total_stats/len(stats),2)

median_pos = round((len(stats))/2,1)

if not median_pos  %2 == 0: #checks for any remainders
    index_1 = int(stats[round(median_pos )]) + int(stats[round(median_pos )+1])#adds the two indexs 
    index_1 = index_1 // 2
else:
    index_1 = int(stats[round(median_pos )]) + int(stats[round(median_pos )-1])
    index_1 = index_1 // 2

median = index_1

def find_mode(stats):
    max_count = (0,0)
    for num in stats:
       occurrences = stats.count(num)
       if occurrences == 1:
           pass    
       elif occurrences > max_count[0]:
                max_count = (occurrences, num)
    return max_count[1]

mode = find_mode(stats)

max = stats[-1]
min = stats[0]

RANGE= int(max) - int(min)

#Mean

mean_q = input("Check the mean [Y/N]: ")

while mean_q == "":
    print("ERROR: Field cannot be empty.")
    mean_q = input("Check the mean [Y/N]: ")

while not (mean_q == "Y" or mean_q == "N"):
    print("ERROR: invalid response.")
    mean_q = input("Check the mean [Y/N]: ")

if mean_q == "Y":
    print(mean)
else:
    pass
             
#Mode

mode_q = input("Check the mode [Y/N]: ")

while mode_q == "":
    print("ERROR: Field cannot be empty.")
    mode_q = input("Check the mode [Y/N]: ")

while not (mode_q == "Y" or mode_q == "N"):
    print("ERROR: invalid response.")
    mode_q = input("Check the mode [Y/N]: ")   

if mode_q == "Y":
    print(mode)
else:
    pass
                              
#Median    
                
median_q = input("Check the median [Y/N]: ")

while median_q == "":
    print("ERROR: Field cannot be empty.")
    median_q = input("Check the median [Y/N]: ")

while not (median_q == "Y" or median_q == "N"):
    print("ERROR: invalid response.")
    median_q = input("Check the median [Y/N]: ")             
if median_q == "Y":
    print(median)
else:
    pass    
    
#Range
              
range_q = input("Check the range [Y/N]: ")

while range_q == "":
    print("ERROR: Field cannot be empty.")
    range_q = input("Check the range [Y/N]: ")
    
while not (range_q == "Y" or range_q == "N"):
    print("ERROR: invalid response.")
    range_q = input("Check the range [Y/N]: ")

if range_q == "Y":
    print(RANGE)
else:
    pass

