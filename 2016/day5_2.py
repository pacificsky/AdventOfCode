# --- Part Two ---
#
# As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism.
# Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers
# have worked out a better solution.
#
# Instead of simply filling in the password from left to right, the hash now also indicates the position within the
# password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents
# the position (0-7), and the seventh character is the character to put in that position.
#
# A hash result of 000001f means that f is the second character in the password. Use only the first result for each
# position, and ignore invalid positions.
#
# For example, if the Door ID is abc:
#
# The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______. In the
# previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position
# (8). The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___. You
# almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.
#
# Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a
# cinematic "decrypting" animation.
#
# Your puzzle input is still reyedfim.

import md5
import sys

counter = 0
door_id = "reyedfim"
#door_id = "abc"
password = ['X' for x in range(8)]
found = 0

sys.stdout.write("{0}\r".format(password))
sys.stdout.flush()

while found < 8:
    data = door_id + str(counter)

    hasher = md5.new()
    hasher.update(data)
    hashval = hasher.hexdigest()

    if hashval[:5] == "00000":
        index = int(hashval[5], 16)
        if index <= 7 and password[index] == 'X':
            password[index] = hashval[6]
            found += 1
            #print "data: {0}".format(data)
            #print "hashval: {0}".format(hashval)
            sys.stdout.write("{0}\r".format(password))
            sys.stdout.flush()

    counter += 1

print password

