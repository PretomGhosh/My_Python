import math
C = 50
H = 30
D_list = list(input("Enter a sequence of numbers with comma separated values : ").split(","))
results = []
for item in D_list:
    D = int(item)
    Q = int(round(math.sqrt((2*C*D)/H),0))
    Q = str(Q)
    results.append(Q)
final_results = ','.join(results)
print(final_results)