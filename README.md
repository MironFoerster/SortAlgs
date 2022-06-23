# Testing the time efficiency of different Sorting Algorithms

This repo deals with the sorting algorithms **Bubble** Sort, **Insertion** Sort, **Merge** Sort and **Quick** Sort and compares them according to their **execution time** for different sizes of input arrays.

## Bubble Sort

The Bubble Sort algorithm sorts by iteratively swapping consecutive elements if they are not in correct order.

The used implementation stops when the previous iteration over the array did not swap any elements (which is tracked by the "swapped" variable). 
This avoids useless iterating over already sorted arrays.

## Insertion Sort

Insertion Sort works similar to how you would sort playing cards.
Every element of the array gets pushed so far to the left until it is in the correct place in the sorted part of the array which accumulates at the left.

Just like the Bubble Sort Insertion Sort sorts the array in place, which reduces the algorithms memory consumption.

## Merge Sort



## Quick Sort

## Comparison

Time of execution in seconds

| n array elements | 1000 | 10.000 | 100.000 | 1.000.000 |
|--------------|:-----:|-----------:|
| Bubble Sort |  1.99 |        739 |
| Insertion Sort |  1.89 |          6 |
| Merge Sort |  1.89 |          6 |
| Quick Sort |  1.89 |          6 |

## Good to know

Used Python version: 3.8

Machine: Windows, AMD Ryzen 5 4000 Series, 8 GB RAM

All used implementations originate from https://www.geeksforgeeks.org/ (small adjustments were made). You can find a direct link to each implementation in the file itself.
