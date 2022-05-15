# Algorithm.py
# Author: Conor McCaffrey
# Computational Thinking with Algorithms 2022 Project
# Write an application which will be used to benchmark five different sorting algorithms

#____________________________________________________________________________________
# Import the required modules

import time   # https://docs.python.org/3/library/time.html
import random # https://docs.python.org/3/library/random.html
import pandas as pd # https://pandas.pydata.org/
import numpy as np # https://numpy.org/
import seaborn as sns # https://seaborn.pydata.org/
import matplotlib.pyplot as plt # https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.html


#____________________________________________________________________________________

# A simple comparison-based sort: Bubble Sort
# References: 
# https://runestone.academy/ns/books/published/pythonds/SortSearch/TheBubbleSort.html (adapted)
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/  (adapted)
# https://www.guru99.com/bubble-sort.html (adapted)
# https://learnonline.gmit.ie/pluginfile.php/579167/mod_resource/content/0/Sorting.py (adapted)

# take in an input array and run BubbleSort function
def bubbleSort(arr): 
    # Looping from size of array from final index to first index, decreasing each iteration by 1 
    for outer in range(len(arr)-1,0,-1):
        # iterate through the array
        for inner in range(outer):
            # conditional to determine if first element is greater than second element
            if arr[inner]>arr[inner+1]:
                # define temp variable to hold our original arr[inner] element
                temp = arr[inner]
                # swap our two elements as arr[inner] is greater than arr[inner+1]
                arr[inner] = arr[inner+1]
                # complete the swap. 
                arr[inner+1] = temp

#____________________________________________________________________________________
#____________________________________________________________________________________
# An effeicient comparison-based sort: QuickSort
# References: 
# https://runestone.academy/ns/books/published/pythonds/SortSearch/TheQuickSort.html (adapted)
# https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python (adapted)
# https://www.geeksforgeeks.org/quick-sort/ (adapted)


# Take in an input array and run QuickSort function
def QuickSort(arr):
    # This is a recursive function, so if the length of the array is less than two,
    # then just return it as the result of the function.
    # This is considered the 'Base Case'
    if len(arr) < 2:
        return arr
    # Define empty arrays to hold our elements
    less, equal, higher = [], [], []

    # Select our pivot element and store this in a pivot variable
    pivot = arr[random.randint(0, len(arr) - 1)]

    # Traverse through each element in our array
    for element in arr:
        # Comparison of our element with the pivot element.
        # We will append our element to a previously defined list depending on it's value.
        # Elements that have a lower value to our pivot element will be appended to the 'less' list
        # Elements that have an equal value to our pivot element will be appended to the 'equal' list
        # Elements that have a higher value to our pivot element will be appended to the 'higher' list
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)

        elif element > pivot:
            higher.append(element)

    # Let's now 'append' our three lists for the output
    return QuickSort(less) + equal + QuickSort(higher)

#____________________________________________________________________________________
#____________________________________________________________________________________
# A non-comparison sort: CountingSort
# References: 
# https://www.geeksforgeeks.org/counting-sort/ (adapted)
# https://python.plainenglish.io/sorting-algorithms-explained-using-python-counting-sort-32b87a0f3011 (adapted)

# Take in an input array and run CountingSort function
def count_sort(arr):
    # let's find the max and min values of our input array
    max_a = int(max(arr))
    min_a = int(min(arr))
    
    # Intialise an array count which will be used to store 
    # the count of number of times each value appears in input
    # initialise it's elements to 0 to begin with.
    count_arr = [0 for i in range(max_a - min_a +1)]
    # We will store our output here
    output_arr = [0 for i in range(len(arr))]
 
    # Store count of each character after its occurrence
    for j in range(0, len(arr)):
        count_arr[arr[j]-min_a] += 1
 
    # Count of sum of occurrences
    for j in range(1, len(count_arr)):
        count_arr[j] += count_arr[j-1]
 
    # Construction of defined output array
    for j in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[j] - min_a] - 1] = arr[j]
        count_arr[arr[j] - min_a] -= 1
 
    # Simple copy of our output array defined earlier into our array so that it 
    # now contains our sorted elements
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    return arr

#____________________________________________________________________________________
#____________________________________________________________________________________
# Any other sorting algorithm: Selection Sort
# References: 
# https://runestone.academy/ns/books/published/pythonds/SortSearch/TheSelectionSort.html (adapted)
# https://learnonline.gmit.ie/pluginfile.php/579165/mod_resource/content/0/08%20Sorting%20Algorithms%20Part%202.pdf

# Take in an input array and run SelectionSort function
def selection_sort(arr):
    n = len(arr)
    # for loop for range of length of input array, incrementing 1 each time
    for outer in range(0,n,1):
        # set a default min value to do the comparisons
        min = outer

        # for loop in range of all elements to right of where we currently are
        for inner in range(outer+1,n,1):
            # if selected element is greater than the min value
            if arr[inner] < arr[min]:
                # assign arr[inner] as the new min value
                min = inner;
        # define temp variable to hold arr[outer] element
        temp = arr[outer]
        # swap our two elements
        arr[outer] = arr[min]
        # complete the swap
        arr[min] = temp
    
#____________________________________________________________________________________
#____________________________________________________________________________________
# Any other sorting algorithm: Insertion Sort
# References: https://runestone.academy/ns/books/published/pythonds/SortSearch/TheInsertionSort.html (adapted)
# https://learnonline.gmit.ie/pluginfile.php/579165/mod_resource/content/0/08%20Sorting%20Algorithms%20Part%202.pdf

# Take in input array and run InsertionSort function
def insertionSort(arr):
    
    # for loop in range of index  1 to to length of array
    # the element at index 0 is initially placed in 'sorted' list as no item to it's left to compare with
    for i in range(1,len(arr)):
    # set the 'key' to the element at current index
     currentsortvalue = arr[i]
     position = i

    # if value to left is higher than the value we are currently trying to sort
    # ('position > 0' section is there to prevent negative indexing)
     while position>0 and arr[position-1]>currentsortvalue:
         # then swap them
         arr[position]=arr[position-1]
         position = position-1

     arr[position]=currentsortvalue

#____________________________________________________________________________________
#____________________________________________________________________________________
#BENCHMARKING

# Generation of random integers as per project file 
# https://learnonline.gmit.ie/pluginfile.php/579189/mod_resource/content/0/CTA_Project.pdf
# https://docs.python.org/3/library/time.html

# define array sizes as per CTA Project file example
arraylength = (100,250,500,750,1000,1250,2500,3750,5000,6250,7500,8750,10000)

#Run the timerRun to get the average run time with the defined array size
def timerRun(algo, sz):

    # empty array to contain generated arrays from below loop
    array = []

    # For loop to run 10 times, one for each instance as we need 10 runs as per project decscription
    for arr in range(10):
        #generate random arrays populated with integers ranging from 1-99 for the given array size
        randintArray =[random.randint(0, 100) for i in range(sz)]
        # store the vlaues of random array into array which will be used later on
        array.append(randintArray)

    #start timer as per project file
    start_time = time.time()

    # For loop to initiate sorting algorithm for each stored array in array variable
    for randintArray in array:    
        algo(randintArray)

    #stop the timer as per project file
    end_time = time.time()

    #convert our running times to milliseconds and divide by 10 to get the average (each algo ran 10 times)
    time_taken = ((end_time - start_time)/10)*1000  
    #return running time to 3 decimal places    
    return round(time_taken,3)


#Define running_time function to calculate running times for each sorting algorithm 
def running_times(algo):
    # define empty list to be populated with average running times
    run = []            
    #for loop for length of input array
    for sz in arraylength:
        lengthofRun = timerRun(algo, sz)
        run.append(lengthofRun)
 
    return(run)

# following code will run each sorting algorithm using above running_time function
bubbleSort_RunTime = running_times(bubbleSort)
quickSort_RunTime = running_times(QuickSort)
countingSort_RunTime = running_times(count_sort)
selectionSort_RunTime = running_times(selection_sort)
insertionSort_RunTime = running_times(insertionSort)

#____________________________________________________________________________________
#____________________________________________________________________________________
#Generation of our output file and graphs
#Setup dataframe output

#References:
# https://www.geeksforgeeks.org/python-map-function/
# https://stackoverflow.com/questions/27156278/index-pandas-dataframe-by-column-numbers-when-column-names-are-integers



sortingAlgo = ["Bubble Sort", "Quick Sort", "Counting Sort", "Selection Sort","Insertion Sort"]
# Reference 2 for this solution
arrayinputsize = list(map(str,arraylength))

datatoanalyse = np.array([bubbleSort_RunTime, quickSort_RunTime, countingSort_RunTime, selectionSort_RunTime, insertionSort_RunTime])
end_result = pd.DataFrame(columns= [arrayinputsize], data = datatoanalyse, index = [sortingAlgo])
print(end_result)

# Plot our results


def plot():
    ax = plt.axes()

    plt.plot(arraylength, bubbleSort_RunTime, marker = 'D', label = 'BubbleSort')
    plt.plot(arraylength, quickSort_RunTime, marker = 'D', label = 'QuickSort')
    plt.plot(arraylength, countingSort_RunTime, marker = 'D', label = 'CountingSort')
    plt.plot(arraylength, selectionSort_RunTime, marker = 'D', label = 'SelectionSort')
    plt.plot(arraylength, insertionSort_RunTime, marker = 'D', label = 'InsertionSort')

    plt.xlabel("Array Input Size")
    plt.ylabel("Time in milliseconds (ms)")
    plt.title("Sorting Algorithm Running Times")
    plt.legend(bbox_to_anchor=(1.0,0.5) , loc='center left')

    plt.grid(ls ="--", color = "#BEBEBE")
    plt.savefig("Output Plot.png")
    plt.show()


plot()