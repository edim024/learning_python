#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

count = 0
sum   = 0 
sd    = 0
med   = 0
numbers = []

for line in fileinput.input():
    if line.startswith( '#' ): continue
    count += 1
    v      = float(line)
    sum   += v
    numbers.append(v) 

numbers.sort()
min     = numbers[0]
max     = numbers[-1]
mean    = sum/count

if (count % 2): median = numbers[floor(count/2)]
else          : median = (numbers[int(count/2)] + numbers[int(count/2)-1])/2

for x in numbers:
    sd += (x - mean)*(x - mean)
    
sd = sqrt(sd/count)
  

print("Count:",count,"\nMinimum:", min,"\nMaximum:", max,"\nMean:", mean,"\nStd. Dev:",'%.3f' % sd,"\nMedian:", median)
   

"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
