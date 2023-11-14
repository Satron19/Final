def char_to_byte_verbose(char):
    ascii_value = ord(char)
    binary_representation = format(ascii_value, '08b')
    return f'ASCII Character value of "{char}" is {ascii_value}. Binary representation of "{char}" in a Byte is {binary_representation}'

def word_to_byte_verbose(word):
    results = [char_to_byte_verbose(char) for char in word]
    total_binary = ' '.join(format(ord(char), '08b') for char in word)
    return '\n'.join(results) + f'\nTotal: {total_binary}'

def main_menu():
    print('Menu\n======')
    print('1. Character\n2. Word')
    choice = input()

    if choice == '1':
        char = input('Enter a character:\n')
        print('Results\n=======')
        print(char_to_byte_verbose(char))
    elif choice == '2':
        word = input('Enter a word:\n')
        print('Results\n=======')
        print(word_to_byte_verbose(word))

if __name__ == '__main__':
    main_menu()

