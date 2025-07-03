
# # measuring time to execute
# import time
# start = time.time()
# i = 1
# while i < 101:
#     print(i)
#     i+=1 
# print(time.time()-start)

# counting operatiions
def c_to_f(c):
    return c*9.0/5 + 32
print(c_to_f)

def mysum(x):

    tatal = 0 
    for i in range (x+1):
        total += i 
        return tatal
print(mysum)

# order of growth
def fact_time (n):
    answer = 1 
    while n > 1 :
        answar *= n 
        n -= 1
        return answer
print(fact_time)
