"""
DNA
"""
# F i l e : dna . py

# D e s c r i p t i o n : practice code

# S t u d e n t Name : Alex Smith   

# S t u d e n t UT EID : ams24495   

# P a r t n e r Name : forgot

# P a r t n e r UT EID : 

# C o u r s e Name : CS 313E

# Unique Number : 50183

# D a t e C r e a t e d :

# D a t e L a s t M o d i f i e d :

def longest_subsequence(string_1, string_2):
    """ADD YOUR CODE HERE """
    longest=[]
    if(len(string_1)>=len(string_2)):
        size=len(string_1)
    else:
        size=len(string_2)
    for i in range(0,size):
        for j in range(len(string_1)):
            if(j+i>len(string_1)):
                break
            s1=string_1[j,j+i]
            for k in range(len(string_2)):
                if(k+i>len(string_1)):
                    break
                s2=string_2[k,k+i]
                if(s1==s2):
                    longest.append(s1)
    return longest
            
            


def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
