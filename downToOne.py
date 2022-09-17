# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:33:47 2022

@author: tyler nelson
9/12/22

assignment name: DOWN TO ONE
"""


'''
Write a Python module that computes the number of steps required for the sequence to get 'down to 1.'

Given any positive integer, n at each step do this:

   If n is odd replace n with 3*n+1

  if n is even, replace n with n/2

for example if n =11 the the sequence is  11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 .... it took 14 steps

print out the number of steps required for the integers 5 through 20
'''
#num = int(input("enter a number -> "))
count = []
for num in range (5,21):
    loops = 0;
    while (num!=1):
        if (num % 2) ==0:
            num = num/2
            print(f"step: {num}")
        else:
            num = 3*num+1
            print(f"step: {num}")
        loops+=1
    print(f"the number of steps was {loops}\n")  
    count.append(loops)     
    
print(count)


#for x in range (5,21):