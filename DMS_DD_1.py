import sys

"""convert DMS to DD
    DMS: a tuple of D,M,S value
    return: decimal degree value of DMS
"""
# Added additional logic to allow for negative minutes with DMS[0] == 0
# The logic already worked for negative seconds
def DMS2DD(DMS):
    DD = abs(DMS[0]) + abs(float(DMS[1])/60) + float(DMS[2])/3600
    if DMS[0] < 0 or DMS[1] < 0: DD = -DD
    return DD

"""convert DD to DMS
    DD: the input decimal degree value
    return: a tuple of D,M,S value
"""
# This script adds 3 lines to the other solution to only convert
# to absolute value once a nonzero value has been extracted in D or M
# to hold the sign. This way M or S can store sign for -1 < DD < 0
def DD2DMS(DD):
    D = int(DD)
    if D: # minutes and seconds should be positive
        DD = abs(DD)
    DD = 60 * (DD - int(DD))
    M = int(DD)
    if M: # seconds should be positive
        DD = abs(DD)
    DD = 60 * (DD - int(DD))
    S = int(round(DD))
    DMS = [D,M,S] # use a list for rounding editing below

    # if minutes or seconds become 60 after rounding
    # round up from seconds to minutes
    # and then from minutes to degrees as necessary
    for j in range(2):
        if abs(DMS[2-j]) == 60:
            if DMS[2-j-1] < 0 or DMS[2-j] < 0: # added DMS[2-j] here in case we get a -60 minutes
                DMS[2-j-1] -= 1
            else:
                DMS[2-j-1] += 1
            DMS[2-j] = 0

    return tuple(DMS) # convert to tuple after any possible edits


def main():
    # main program
    # input
    inputStr = input("Please enter a latitude or longitude value in DMS or DD format.\n")

    # convert
    coord = inputStr.split(',')
    if len(coord) == 1: # input in DD format
        try:
            DD = float(coord[0])
        except:
            print("DD value should be a valid number.")
            sys.exit()
        print("The input value is in DD form.")
        DMS = DD2DMS(DD)
        print("Its DMS form is %s %s %s." % DMS)
    elif len(coord) == 3: # input in DMS format
        try:
            D = int(coord[0])
            M = int(coord[1])
            S = float(coord[2])
        except:
            print("D,M,S values should be numbers, and D and M integers.")
            sys.exit()
        DMS = (D,M,S)
        print("The input value is in DMS form.")
        DD = DMS2DD(DMS)
        print("Its DD form is %.4f." % DD)
    else: # invalid input
        print("The input value is invalid!")

# Only call this function if this script is run directly instead of imported.
# This allows this script to be imported as a module for access to the
# functions without running the main function collecting input.
if __name__ == '__main__':
    main()