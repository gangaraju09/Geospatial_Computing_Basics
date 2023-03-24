import sys

"""convert DMS to DD
    DMS: a tuple of D,M,S value
    return: decimal degree value of DMS
"""
def DMS2DD(DMS):
    DD = abs(DMS[0]) + float(DMS[1])/60 + float(DMS[2])/3600
    if DMS[0] < 0: DD = -DD
    return DD

"""convert DD to DMS
    DD: the input decimal degree value
    return: a tuple of D,M,S value
"""
# Does not account for sign for DD values between -1 and 0
def DD2DMS(DD):
    D = int(DD)
    DD = abs(DD) # minutes and seconds should be positive
    DD = 60 * (DD - int(DD))
    M = int(DD)
    DD = 60 * (DD - int(DD))
    S = int(round(DD))
    DMS = [D,M,S] # use a list for rounding editing below

    # if minutes or seconds become 60 after rounding
    # round up from seconds to minutes
    # and then from minutes to degrees as necessary
    for j in range(2):
        if DMS[2-j] == 60:
            if DMS[2-j-1] < 0:
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
        print("The input value is in DMS form.")
        DMS = (D,M,S)
        DD = DMS2DD(DMS)
        print("Its DD form is %.4f." % DD)
    else: # invalid input
        print("The input value is invalid!")

# Only call this function if this script is run directly instead of imported.
# This allows this script to be imported as a module for access to the
# functions without running the main function collecting input.
if __name__ == '__main__':
    main()