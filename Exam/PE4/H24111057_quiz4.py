""" 
author: H244111057 姚博瀚
"""

# User input for sequence
sequence = input("Enter a sequence of intergers separated by whitespace: ")
# Split the sequence by whitespace to create a list
list_sequence = list(sequence.split(' '))

# Convert elements in list_sequence from string to int
sequence2 = []
for i in range(len(list_sequence)):
    a = list_sequence[i]
    sequence2.append(int(a))

# Initialize a list to store the longest increasing subsequence
longest_subsequence = []
# Initialize a list to store the lengths of increasing subsequences
lengths = [1] * len(sequence2)

## Strategy: calculating the LICS for each elements
# Outer loop through each each elements
for i in range(len(sequence2)):
    longest_subsequence_current = [sequence2[i]]
    # Innner loop through each elements on the right of current iterated elements
    for j in range(i+1, len(sequence2)):
        # Chech if larger than the element which outer loop iterates currently
        if sequence2[j] > longest_subsequence_current[-1]:
            lengths[i] += 1
            longest_subsequence_current.append(sequence2[j])
            #print(f'i:{i} , LICS:{longest_subsequence_current}')
    #print(f'i:{i}, LICS:{longest_subsequence_current}')
    
    #### Bug fix: deal with LICS update
    if i == 0:
        longest_subsequence = longest_subsequence_current.copy()
    # Check if the current element's LICS lenghth was larger than current longest subsequence's lenghth
    elif i > 0 and lengths[i] > len(longest_subsequence):
        longest_subsequence = longest_subsequence_current.copy()

#### Bug fix: deal with all length are 1
# Check if all length are 1, then make longest subsequence be the first element in input sequence
if sum(lengths) == len(sequence2):
    longest_subsequence = sequence2[0]         

# print result
print(f'Length: {max(lengths)}')
#print(f'{lengths}')
print("LICS: ", longest_subsequence)