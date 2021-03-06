# http://adventofcode.com/2016/day/14
import hashlib
import re
import sys

class Candidate:
    def __init__(self, key, index, char):
        self.key = key
        self.index = index
        self.regexp = re.compile(r'[a-f0-9]*{0}{0}{0}{0}{0}[a-f0-9]*'.format(char))
        self.char = char

    def __str__(self):
        return "<key:{0}, index:{1}, char:{2}>".format(self.key, self.index, self.char)


def main():
    salt = "jlmsuwbz"
    #salt = "abc"
    index = 0
    keys = []
    candidates = []

    regexp_1 = re.compile(r'[a-f0-9]*?([a-f0-9])\1{2}[a-f0-9]*?')
    regexp_2 = re.compile(r'[a-f0-9]*([a-f0-9])\1{4}[a-f0-9]*')

    endgame = False

    loop_count = 0
    while len(keys) < 75:
        hashval = salt + str(index)
        for x in range(2017):
            h = hashlib.md5()
            h.update(hashval)
            hashval = h.hexdigest().lower()


        # h = hashlib.md5()
        # h.update(salt + str(index))
        # hashval = h.hexdigest().lower()

        #sys.stdout.write("Loop count is {0}\r".format(loop_count))
        #loop_count += 1

        #if index == 120:
        #    print hashval
        #    break
        #
        # if index == 817:
        #     print hashval
        #     break

        # Is this a follow-on key
        m2 = regexp_2.match(hashval)
        if m2:
            # Check existing candidate keys to determine if it matches
            # Also prune
            to_prune = []
            for candidate in candidates:
                if candidate.index + 1000 < index:
                    to_prune.append(candidate)
                elif candidate.regexp.match(hashval):
                    # print ""
                    print "Found match: Candidate index:{0} key:{1} Match index:{2} hash:{3}".format(candidate.index,
                            candidate.key, index, hashval)
                    keys.append(candidate)
                    to_prune.append(candidate)

            if len(to_prune) > 0:
                for prune in to_prune:
                    candidates.remove(prune)
                    print "Pruned candidate {0}".format(prune)


        # Is this a candidate key?
        m1 = regexp_1.match(hashval)
        if m1:
            char = m1.groups()[0]  # Matching character
            candidates.append(Candidate(hashval, index, char))
            print "Adding candidate at index {0} with char {1}: {2}".format(index, char, hashval)

        index += 1


    sorted_keys = sorted(keys, key=lambda hashcand: hashcand.index)
    #sorted_keys = keys
    assert len(sorted_keys) >= 64

    #print "Matching index is {0}".format(sorted_keys[63].index)
    print ""
    for x in range(len(sorted_keys)):
        key = sorted_keys[x]
        print "Found key {0} at index {1}: {2}".format(x+1, key.index, key.key)




main()

