# --- Part Two ---
#
# With all the decoy data out of the way, it's time to decrypt this list and get moving.
#
# The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software.
# However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like
# yourself.
#
# To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID.
# A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.
#
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
#
# What is the sector ID of the room where North Pole objects are stored?

# Rotate the alphabet by the provided number
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def rotate_alphabet(count):
    new_count = count % 26;
    return ALPHABET[new_count:] + ALPHABET[:new_count]


def decrypt(alphabet, string):
    result = ""
    for c in string:
        result += alphabet[ALPHABET.index(c)]

    return result


sector_sum = 0
real_rooms = []

f = open('day4_1_input.txt', 'r')
for line in f:
    line = line.rstrip().rstrip('\n]')

    freq_map = {}
    sector_id = 0
    checksum = ""
    scrambled_names = []

    for item in line.split('-'):
        if item[0].isalpha():
            # Process letters
            scrambled_names.append(item)
            for letter in item:
                if letter in freq_map:
                    freq_map[letter] += 1
                else:
                    freq_map[letter] = 1
        else:
            sector_data = item.split('[')
            sector_id = int(sector_data[0])
            checksum = sector_data[1]

    reverse_map = {}
    for key, value in freq_map.iteritems():
        if value in reverse_map:
            reverse_map[value].append(key)
        else:
            reverse_map[value] = [key]

    slice_length = min(5, len(reverse_map))
    sorted_by_freq = sorted(reverse_map.items(), key=lambda x: x[0], reverse=True)[:slice_length]
    allowed_list = []
    for pair in sorted_by_freq:
        allowed_list = allowed_list + sorted(pair[1])

    actual_checksum = ""
    for i in range(min(len(checksum), len(allowed_list))):
        actual_checksum += allowed_list[i]

    if actual_checksum == checksum:
        sector_sum += sector_id

        new_alphabet = rotate_alphabet(sector_id)
        print [decrypt(new_alphabet, x) for x in scrambled_names]
        print sector_id

#print sector_sum

