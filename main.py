
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    while(n != 1):
        
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
                      # the last print is 1

def main():
 n = int(input("what number do you want to put?: "))
count = seq3np1(3) 
print("This is the starting number: ", 3)
print("Number of iterations:", count)
