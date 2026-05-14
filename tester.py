



### Python elegant version of fibonacci sequence

# fib = []

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    

# for i in range(20):
#     fib.append(fibo(i))
    
# print(fib)

#################################################################
#################################################################


# d = {"a": 1, "b": 2, "c": 3}

# for i, k in enumerate(d, 1):
#     print(i, k, d[k])


####################################################



# d = {"a": 1, "b": 2, "c": 3}

# for i in enumerate(d, 1):
#     print(i)








####################################################

# x = ('apple', 'banana', 'cherry')

# for i, j in enumerate(x, 1):
#     print(i)

########################################################

# urls = ["url1", "url2", "url3", "url4", "url5", "url6", "url7", "url8", "url9"]
# chunks = []
# chunk_size = 2
# for i in range(0, len(urls), chunk_size):
#     chunk = urls[i:i + chunk_size]
#     chunks.append(chunk)

# print(chunks)


#########################################################

urls = ["url1", "url2", "url3", "url4", "url5", "url6", "url7", "url8", "url9"]

group_of_3 = []
for i in range(0, len(urls), 3):
    group_of_3.append(urls[i:i + 3])
print(group_of_3)