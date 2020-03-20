"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

# Test function
def Test(n, a):
    if (a <=1) or (a>=(n-1)):
            print("Your input a = " + str(a) + " is out of range")
            return
    if n == 2 :
        print("Your input number is 2 which is a prime number!")
        return
    if n == 1 :
        print("Your input number is 1! Insert a number greater than 1")
        return
    elif (np.mod(n, 2) == 0) and (n>2) :
        ans = "Composite!"
        return ans
    elif (np.mod(n, 2) == 1) and (n>1) :
        k = 0
        w = n-1
        while np.mod(w, 2) == 0:
            w = w/2
            k += 1
        q = w
# =============================================================================
#         print("q is: " + str(int(q)))
#         print("k is: " + str(k))
# =============================================================================
        a_org = a
        for i in range(int(q-1)):
            a = np.mod((a*a_org), n)
        aq_mod = np.mod(a, n)
        if np.mod(aq_mod, n) == 1 or np.mod(aq_mod, n) == n-1:
            ans = "Inconclusive!"
            return ans
        for i in range(k-1):
            if np.mod(aq_mod*aq_mod, n) == n-1:
                ans = "Inconclusive!"
                return ans
            aq_mod = np.mod(aq_mod*aq_mod, n)
        ans = "Composite!"
        return ans

# Define Miller Rabin function with two modes
def MR(n, *args, **kwargs):
    a = kwargs.get('a', None)
    s = kwargs.get('s', None)
    mode = kwargs.get('mode', None)
    
    # When user inserts a directly
    if mode == "specific witness" :
        print (Test(n, a))

    # When user inserts s as number of random witnesses    
    elif mode == "random witnesses" :
        # Generate s random integers
        a_list = np.random.randint(low=2, high=n-2, size=s)
        t = 0
        for witness in a_list:
            t+=1
            if Test(n, witness) == "Composite!":
                print("Input number: "+str(n))
                print("Number of attempts: "+ str(t) +" out of "+str(len(a_list)))
                print(Test(n, witness))
                break
        if t == len(a_list):
            print("Input number: "+str(n))
            print("Number of attempts: "+ str(t)+" out of "+str(len(a_list)))
            print("Inconclusive!")
        
        
    else : 
        print("'" + str(mode) + "'" + " mode is not defined!")

# Call Miller Rabin function:
MR(n=29, s=11, mode="random witnesses")
# =============================================================================
# x = Test(221, 21)
# print(x)
# =============================================================================
