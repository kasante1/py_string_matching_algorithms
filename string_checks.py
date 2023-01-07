# c = "acbcabccababcaacbcaabacbbc"

# for g in  enumerate(c):
#     print(g)


# pattern = "abacbbc"
# n = len(pattern)        # length of the pattern
# prefix_fun = ['k']*(n)  
# print(prefix_fun)

# for q in range(2,n):
#     print(q)



def prefix_function(pattern):          # function to generate prefix function for the given pattern
    n = len(pattern)        # length of the pattern
    prefix_fun = [0]*(n)    # initialize all elements of the list to 0
    k = 0
    for q in range(2,n):
        while k>0 and pattern[k+1] != pattern[q]:
            k = prefix_fun[k]
        if pattern[k+1] == pattern[q]:      # If the kth element of the pattern is equal to the qth element
            k += 1                          # update k accordingly
        prefix_fun[q] = k
    return prefix_fun                       # return the prefix function

prefix_function("abacbbcab")

