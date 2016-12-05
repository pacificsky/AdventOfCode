# --- Day 4: Security Through Obscurity ---
#
# Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy
# data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.
#
# Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a
# checksum in square brackets.
#
# A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties
# broken by alphabetization. For example:
#
# aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y,
# and z, which are listed alphabetically. a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all
# tied (1 of each), the first five are listed alphabetically. not-a-real-room-404[oarel] is a real room.
# totally-real-room-200[decoy] is not. Of the real rooms from the list above, the sum of their sector IDs is 1514.
#
# What is the sum of the sector IDs of the real rooms?

sector_sum = 0

f = open('day4_1_input.txt', 'r')
for line in f:
    line = line.rstrip().rstrip('\n]')

    freq_map = {}
    sector_id = 0
    checksum = ""

    for item in line.split('-'):
        if item[0].isalpha():
            # Process letters
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

print sector_sum

    #print sorted_by_freq





    # sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    #
    # allowed_list = []
    # count_map = {}
    # for pair in sorted_freq:
    #     if len(count_map) < 5:
    #         allowed_list.add(pair[0])
    #         count_map[pair[1]] = 1
    #     elif len(count_map) == 5 and pair[0] in count_map:
    #         allowed_list.append(pair[0])
    #
    #
    # print sorted_freq


