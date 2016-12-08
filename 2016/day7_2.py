# --- Part Two ---
#
# You would also like to know which IPs support SSL (super-secret listening).
#
# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square
# bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is
# any three-character sequence which consists of the same character twice with a different character between them, such as
# xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.
#
# For example:
#
# aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets). xyx[xyx]xyx does
# not support SSL (xyx, but no corresponding yxy). aaa[kek]eke supports SSL (eke in supernet with corresponding kek in
# hypernet; the aaa sequence is not related, because the interior character must be different). zazbz[bzb]cdb supports SSL
# (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap). How many IPs in your
# puzzle input support SSL?


def is_aba(data):
    return len(data) == 3 and \
        data[0] == data[2] and \
        data[0] != data[1]


def is_bab(data):
    return is_aba(data)


def flip(string):
    assert len(string) == 3
    assert is_aba(string)
    return string[1] + string[0] + string[1]


def main():
    f = open("day7_1_input.txt", "r")

    ssl_ip_count = 0

    for line in f:
        data = []
        inside_box = False
        aba_set = set()
        bab_set = set()
        for c in line:
            if c == '[':
                inside_box = True
                data = []
                continue
            elif c == ']':
                inside_box = False
                data = []
                continue

            if len(data) == 3:
                data.pop(0)

            data.append(c)

            if inside_box:
                if is_bab(data):
                    bab_set.add(reduce(lambda x,y: str(x) + str(y), data))
            else:
                if is_aba(data):
                    aba_set.add(reduce(lambda x, y: str(x) + str(y), data))

        if len(bab_set) > 0 and len(aba_set) > 0:
            for string in bab_set:
                if flip(string) in aba_set:
                    ssl_ip_count += 1
                    break

    print "SSL IP count is {0}".format(ssl_ip_count)




main()