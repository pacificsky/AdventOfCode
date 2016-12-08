# --- Day 7: Internet Protocol Version 7 ---
#
# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is
# much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).
#
# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence
# which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba.
# However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.
#
# For example:
#
# abba[mnop]qrst supports TLS (abba outside square brackets). abcd[bddb]xyyx does not support TLS (bddb is within square
# brackets, even though xyyx is outside square brackets). aaaa[qwer]tyui does not support TLS (aaaa is invalid; the
# interior characters must be different). ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though
# it's within a larger string). How many IPs in your puzzle input support TLS?

def is_tls(data):
    return len(data) == 4 and \
        data[0] == data[3] and \
        data[1] == data[2] and \
        data[0] != data[1]

def main():
    f = open("day7_1_input.txt", "r")

    tls_ip_count = 0

    for line in f:
        data = []
        inside_box = False
        tls_inside_box_count = 0
        tls_outside_box_count = 0
        for c in line:
            if c == '[':
                inside_box = True
                data = []
                continue
            elif c == ']':
                inside_box = False
                data = []
                continue

            if len(data) == 4:
                data.pop(0)

            data.append(c)

            has_tls = is_tls(data)
            if has_tls:
                if inside_box:
                    tls_inside_box_count += 1
                else:
                    tls_outside_box_count += 1

        if tls_inside_box_count == 0 and tls_outside_box_count > 0:
            tls_ip_count += 1

    print "TLS IP count is {0}".format(tls_ip_count)




main()