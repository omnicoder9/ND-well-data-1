import pandas as pd
from collections import Counter

df = pd.read_csv('Well_Index\WellIndex.csv')
attributes = []
for col in df.columns:
    attributes.append(col)
#print(attributes)

#firstFive = df.head()
#print(firstFive)

#count total number of wells

#count number of distinct operators
active = 0
statuses = df["WellStatus"]
for status in statuses:
    if status == "A":
        active+=1
print("There are " + str(active) + " active wells in ND.")

""" 
distinct_operators = []
op_map = {}
for op in operators:
    if op not in distinct_operators:
        distinct_operators.append(op)
        op_map[op] = 1
    else:
        op_map[op]+=1
print("There are " + str(len(distinct_operators)) + " distinct operators in ND.")
largest_op = max(op_map, key=op_map.get)
largest_op_well_count = max(op_map.values())
print("The largest operatior in ND is " + largest_op + " with " + str(largest_op_well_count) + " wells.")

largest_ops = Counter(op_map).most_common(20)
print("The 20 largest operators in ND are:\n")
for key, value in largest_ops:
    print(key + ": " + str(value) + " wells") """

