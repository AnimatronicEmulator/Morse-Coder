# 1. The length of a dot is one unit.
# 2. A dash is 3 units.
# 3. The space between parts of the same letter is one unit.
# 4. The space between letters is 3 units.
# 5. The space between words is 7 units.

import time
import winsound

space = '       '
kern = '   '
morse_dict = {'a': '. −', 'b': '− . . .', 'c': '− . − .', 'd': '− . .', 'e': '.', 'è': '. . − . .', 'f': '. . − .',
              'g': '− − .', 'h': '. . . .', 'i': '. .', 'j': '. − − −', 'k': '− . −', 'l': '. − . .', 'm': '− −',
              'n': '− .', 'o': '− − −', 'p': '. − − .', 'q': '− − . −', 'r': '. − .', 's': '. . .', 't': '−',
              'u': '. . −', 'v': '. . . −', 'w': '. − −', 'x': '− . . −', 'y': '− . − −', 'z': '− − . .',
              '1': '. − − − −', '2': '. . − − −', '3': '. . . − −', '4': '. . . . −', '5': '. . . . .',
              '6': '− . . . .',  '7': '− − . . .', '8': '− − − . .', '9': '− − − − .', '0': '− − − − −',
              '.': '. − . − . −', ',': '− − . . − −', ':': '− − − . . .', '?': '. . − − . .', "'": '. − − − − .',
              '-': '− . . . . −', '/': '− . . − .', '(': '− . − − .', ')': '− . − − . −', '"': '. − . . − .',
              '⹀': '− . . . −', '+': '− . . . −', '×': '− . . −', '@': '.– – .– .', '%': '− − − − − −   . . − .   − − − − −'}

encode_decode = input("Would you like to encode a string into Morse code, or would you like to decode a Morse encoding? [E/D] ")
in_str = input("Please enter a string to convert to Morse code: \n")
char_list = list(in_str.lower())
morse_str = ''

for x in range(len(char_list)):
    if ' ' == char_list[x]:
        morse_str += space

    elif x + 1 < len(char_list) and char_list[x + 1] != ' ':
        try:
            morse_str += morse_dict[char_list[x]]
        except KeyError:
            print(f'The character "{char_list[x]}" isn\'t standard in Morse code.')
        else:
            morse_str += kern

    else:
        try:
            morse_str += morse_dict[char_list[x]]
        except KeyError:
            print(f'The character "{char_list[x]}" isn\'t standard in Morse code.')

print(morse_str)

frequency = 550
dit_duration = 60

for char in morse_str:
    if char == '.':
        winsound.Beep(frequency, dit_duration)
    elif char == '−':
        winsound.Beep(frequency, 3 * dit_duration)
    else:
        time.sleep(dit_duration / 1000)
