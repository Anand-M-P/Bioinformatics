# EXON CHAINING PROBLEM

# Anand.M.P
# B120361CS
# S8, B.Tech Computer Science and Engineering

# DESCRIPTION
# This algorith takea a set of exons in the following format,
# Left Index of the interval
# Right Index of the interval
# Weight of the interval
# It returns the maximum non-overlapping exon chaining value possible

# SAMPLE INPUT
# Enter the number of exons9
# Enter the exon interval in the format:
#  LeftIndex
#  RightIndex
#  Weight
# Exon : 1
# 2
# 3
# 3
# Exon : 2
# 1
# 5
# 5
# Exon : 3
# 4
# 8
# 6
# Exon : 4
# 6
# 12
# 10
# Exon : 5
# 9
# 10
# 1
# Exon : 6
# 7
# 17
# 12
# Exon : 7
# 11
# 15
# 7
# Exon : 8
# 13
# 14
# 0
# Exon : 9
# 16
# 18
# 4

# SAMPLE OUTPUT
# The required Exon Chainging value is : 21


# Variables Intialization
left = []  # To store the left index
right = []  # To store the right index
weight = []  # To store the weight of the interval
DP = []  # DP list to store the result
ordered_vertices = []  # To store the list of ordered vertices in the graph
exonSequence = []  # To store the final exon sequence

# testCases = input("Enter the number of text cases") #Takes the number of text cases
# testCases = int(testCases)

noOfExons = int(input("Enter the number of exons"))  # Takes user input for the number of exons
noOfIntervals = noOfExons

print("Enter the exon interval in the format: \n LeftIndex \n RightIndex \n Weight")

count = 1
while noOfExons:
    print("Exon : " + str(count))
    left.append(int(input()))
    right.append(int(input()))
    weight.append(int(input()))
    noOfExons -= 1
    count += 1

for ele in left:
    ordered_vertices.append(ele)
for ele in right:
    ordered_vertices.append(ele)
ordered_vertices.sort()
# print(ordered_vertices)

noOfIntervals *= 2
for i in range(0, noOfIntervals + 1):
    DP.append(0)
# print(DP)

i = 1

for ele in ordered_vertices:
    if ele in right:
        rightIndex = right.index(ele)
        leftIndexValue = left[rightIndex]  # Get the left index value
        leftIndex = ordered_vertices.index(leftIndexValue) + 1  # To get the real left index from the sorted vertices
        wt = weight[rightIndex]  # Get the weight of the interval
        # print(DP)
        DP[i] = max(DP[leftIndex] + wt, DP[i - 1])
        value1 = DP[leftIndex] + wt
        value2 = DP[i - 1]
        # if value1 > value2:
        #     exonSequence.append((left[rightIndex], right[rightIndex], weight[rightIndex]))

    else:
        DP[i] = DP[i - 1]
    i += 1
    # print(DP)

lastElementIndex = len(DP) - 1
print("The required Exon Chainging value is : " + str(DP[lastElementIndex]))
DP.clear()
