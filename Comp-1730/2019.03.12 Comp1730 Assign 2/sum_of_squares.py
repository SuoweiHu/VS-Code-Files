## COMP1730/6730 S1 2019 - Homework 2
# Submission is due 11:55pm, Sunday the 17th of March, 2019.

## YOUR ANU ID: u6966459
## YOUR NAME: Suowei Hu


def sum_of_squares(n):
    '''
    this function will take a number n, 
    return the value of n:th meneber in the square pyramidal number sequence
    '''
    
    calculate_n_th_menber = (n * (n + 1) * (2 * n + 1))/6
    # calculate the value of the nth menmber in the suqare pyramidal number sequence

    int_n_th_member = int(calculate_n_th_menber)
    # this will make sure type of the returning value is a integer

    return int_n_th_member

## REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
## OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS.
