# Python Number Distribution

## Description  
This project implements a simple *number redistribution algorithm* in Python. It starts by generating a list of random numbers and then redistributes values greater than the average to other elements in the list until all numbers are at least equal to the average.

## How It Works  
1. *Generating Random Numbers*: The function rand_num_cr() generates six random integers between 0 and 10.  
2. *Calculating the Average*: The average of the generated numbers is computed.  
3. *Redistributing Values*: If an element is greater than the average, its surplus value is transferred to the next element in the list. This process continues until all numbers in the list are at least equal to the average.  
4. *Completion*: Once redistribution is complete, the program prints Done! and exits.  

## How to Run  
To run this script, execute array.py in a Python environment:

```bash
python array.py

average: 5
Array: [5, 6, 4, 5, 5, 5] -- Cycles counter: 1
Array: [5, 5, 5, 5, 5, 5] -- Cycles counter: 2
Done!
