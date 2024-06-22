'''
Write a function in python that takes input an array of distinct integers ,
and returns the length of highest mountain. 

A mountain is defined as adjacent integers that are strictly increasing 
until they reach a peak , at which they become strictly decreasing. 

At least 3 numbers are required to form a mountain.

'''

def mountain(array):
    if len(array) < 3:
        return 0

    ans = 0
    i = 1

    while i < len(array) - 1:
        isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
        
        if isPeak:
            left = i - 1
            right = i + 1
            
            # Go backward
            while left > 0 and array[left] > array[left - 1]:
                left -= 1
            
            # Go forward
            while right < len(array) - 1 and array[right] > array[right + 1]:
                right += 1
            
            # Calculate the breadth of the mountain
            current_length = right - left + 1
            ans = max(ans, current_length)
            
            # Move i to the end of the current mountain
            i = right
        else:
            i += 1

    return ans

if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2, 0, 11, 13, 15, 17, 19, 21, 13, 0]
    print(mountain(array))  # Output should be 16 for the given array

'''
#Initialization and Edge Case Check: Added a check to immediately return 0 if the array length is less than 3.

#Improved Index Management: Correctly track the left and right pointers (left and right) 
around the peak to find the entire span of the mountain.

#Backward and Forward Traversal: Used while loops to expand left backward and right forward 
until the mountain property breaks (i.e., the sequence stops being strictly increasing or decreasing).

#Breadth Calculation:Calculated the breadth of the mountain as right - left + 1 and 
updated the answer if this breadth is larger than the current maximum.

#Update Pointer: After processing a peak, i is set to right to skip over the current mountain, 
avoiding unnecessary checks.

'''
