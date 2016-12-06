# --- Part Two ---
#
# Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.
#
# In this modified code, the sender instead transmits what looks like random data, but for each character, the character
# they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the
# letter distributions in each column and choose the least common letter to reconstruct the original message.
#
# In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this
# process for the remaining characters produces the original message, advent.
#
# Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is
# trying to send?



LENGTH = 8
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

values = []
for x in range(LENGTH):
    values.append({c : 0 for c in ALPHABET})

f = open('day6_1_input.txt', 'r')
for data in f:
    data = data.rstrip().rstrip("\n")
    assert len(data) == LENGTH
    for i in range(LENGTH):
        c = data[i]
        values[i][c] += 1

message = ""
for x in range(LENGTH):
    values[x] = sorted(values[x].items(), key=lambda x: x[1], reverse=False)
    # values[x] is now an array of tuples (character: frequency) sorted by frequency
    # We need to find the first character with a non-zero frequency
    for i in range(len(ALPHABET)):
        if values[x][i][1] == 0:
            continue
        else:
            message += values[x][i][0]
            break

print message



