# GLOBAL SEQUENCE ALIGNMENT
#
# Anand.M.P
# B120361CS
# S8, BTech CSE

# DESCRIPTION
# This algorithm takes two inputs; two DNA sequences, and the scoring matrix values, and returns one of the plausible alignment
# along with the alignment score.

# SAMPLE INPUT:
# Enter Sequence 1 : AGCATGC
# Enter Sequence 2 : ACAATCC
# Enter the SCORING matrix values
# Enter score for match : 2
# Enter score for mismatch : -1
# Enter score for insertion : -1
# Enter score for deletion : -1

# SAMPLE OUTPUT:
# Best Alignment :
# AGC_ATGC
# A_CAATCC
# Alignment Score:  7

seq1 = input('Enter Sequence 1 : ')
seq2 = input('Enter Sequence 2 : ')

print("Enter the SCORING matrix values")
MATCH = int(input("Enter score for match : "))
MISMATCH = int(input("Enter score for mismatch : "))
INSERTION = int(input("Enter score for insertion : "))
DELETION = int(input("Enter score for deletion : "))

gap = '_'
seq1 = gap + seq1
seq2 = gap + seq2

seqLength1 = len(seq1)
seqLength2 = len(seq2)

# Intializing  the DP and backTrack matrices to zero
DP = [[0 for x in range(seqLength1)] for x in range(seqLength2)]
backTrack = [[0 for x in range(seqLength1)] for x in range(seqLength2)]

for row in range(seqLength2):
    if row == 0:
        continue
    DP[row][0] = DP[row - 1][0] + INSERTION  # Gap against all other characters, row wise
    backTrack[row][0] = backTrack[row - 1][0] + INSERTION

for col in range(seqLength1):
    if col == 0:
        continue
    DP[0][col] = DP[0][col - 1] + DELETION  # Gap against all other characters, column wise
    backTrack[0][col] = backTrack[0][col - 1] + DELETION

for col in range(1, seqLength1):
    for row in range(1, seqLength2):
        if seq1[col] == seq2[row]:
            matchOrMismatch = DP[row - 1][col - 1] + MATCH  # If the characters are a match
        else:
            matchOrMismatch = DP[row - 1][col - 1] + MISMATCH  # If the characters are a mismatch

        insertion = DP[row - 1][col] + INSERTION
        deletion = DP[row][col - 1] + DELETION

        DP[row][col] = max(matchOrMismatch, insertion, deletion)  # Finds the maximum and saves it

        if matchOrMismatch == DP[row][col]:  # For backtracking and finding the plausible alignment
            backTrack[row][col] = 'd'  # For diagonal : match or mismatch
        elif insertion == DP[row][col]:
            backTrack[row][col] = 'i'  # For insertion
        else:
            backTrack[row][col] = 'dl'  # For deletion

# for x in DP:
#     print(x, '\n')
#
# # for x in backTrack:
# #     print(x, '\n')

seq1Alignment = ''
seq2Alignment = ''

print("Best Alignment : ")

while col > 0:
    while row > 0:
        if backTrack[row][col] == 'd':
            seq1Alignment = seq1[col] + seq1Alignment
            seq2Alignment = seq2[row] + seq2Alignment
            row -= 1
            col -= 1
        elif backTrack[row][col] == 'i':
            seq1Alignment = '_' + seq1Alignment
            seq2Alignment = seq2[row] + seq2Alignment
            row -= 1
        else:
            seq1Alignment = seq1[col] + seq1Alignment
            seq2Alignment = '_' + seq2Alignment
            col -= 1

print(seq1Alignment)
print(seq2Alignment)
print("Alignment Score: ", DP[seqLength2 - 1][seqLength1 - 1])
