# Mountain_Problem
Write a function in Python that takes input from an array of distinct integers, and returns the length of the highest mountain.   A mountain is defined as adjacent integers that are strictly increasing  until they reach a peak, at which they become strictly decreasing.   At least 3 numbers are required to form a mountain.

=============================================
#Initialization and Edge Case Check: Added a check to immediately return 0 if the array length is less than 3.

#Improved Index Management: Correctly track the left and right pointers (left and right) 
around the peak to find the entire span of the mountain.

#Backward and Forward Traversal: Used while loops to expand left backward and right forward 
until the mountain property breaks (i.e., the sequence stops being strictly increasing or decreasing).

#Breadth Calculation: Calculated the breadth of the mountain as right-left + 1 and 
updated the answer if this breadth is larger than the current maximum.

#Update Pointer: After processing a peak, i is set to right to skip over the current mountain, 
avoiding unnecessary checks.
