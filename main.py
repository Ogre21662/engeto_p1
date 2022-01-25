'''
author = OGre
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]


users = {'bob': '123',
         'ann': 'pass123',
         'mike': 'password123',
         'liz': 'pass123'}


def print_line():
    print('-' * 40)


def say_hello(name):
    print('Welcome to the app, ' + name)
    print('We have 3 texts to be analyzed.')


def w_count(i):
    num_of_words = len(TEXTS[i].replace('.', ' ').replace(',', ' ').split())
    return num_of_words


def title_w_count(i):
    num_of_title_words = 0
    word_list = TEXTS[i].replace('.', ' ').replace(',', ' ').split()
    for word in word_list:
        if word.istitle():
            num_of_title_words += 1
    return num_of_title_words


def upper_w_count(i):
    num_of_upper_words = 0
    word_list = TEXTS[i].replace('.', ' ').replace(',', ' ').split()
    for word in word_list:
        if word.isupper() and word.isalpha():
            num_of_upper_words += 1
    return num_of_upper_words


def lower_w_count(i):
    num_of_lower_words = 0
    word_list = TEXTS[i].replace('.', ' ').replace(',', ' ').split()
    for word in word_list:
        if word.islower() and word.isalpha():
            num_of_lower_words += 1
    return num_of_lower_words


def numeric_w_count(i):
    num_of_num_words = 0
    word_list = TEXTS[i].replace('.', ' ').replace(',', ' ').split()
    for word in word_list:
        if word.isdigit():
            num_of_num_words += 1
    return num_of_num_words


def sum_digits(i):
    sum_of_digits = 0
    word_list = TEXTS[i].replace('.', ' ').replace(',', ' ').split()
    for word in word_list:
        if word.isdigit():
            sum_of_digits += int(word)
    return sum_of_digits


def analyze(i):
    print('There are ' + str(w_count(i)) + ' words in the selected text.')
    print('There are ' + str(title_w_count(i)) + ' title words.')
    print('There are ' + str(upper_w_count(i)) + ' uppercase words.')
    print('There are ' + str(lower_w_count(i)) + ' lowercase words.')
    print('There are ' + str(numeric_w_count(i)) + ' numeric strings.')
    print('The sum of all the numbers ' + str(sum_digits(i)))


def count_occurrences(i):
    word_list = TEXTS[i].replace('.', ' ').replace(',', ' ').split()
    occurrences = {}
    for word in word_list:
        length = len(word)
        if length not in occurrences:
            occurrences[length] = 1
        else:
            occurrences[length] += 1

    j = 1
    for numbers in range(max(occurrences)):
        num_of_spaces = 1
        if j not in occurrences:
            occurrences[j] = 0
        if int(j / 10) == 0:
            num_of_spaces = 2
        elif int(j / 10) > 0:
            num_of_spaces = 1
        print(' ' * num_of_spaces
              + str(j) + '|'
              + '*' * occurrences[j]
              + ' ' * (17 - occurrences[j])
              + '|' + str(occurrences[j]))
        j += 1


def graph(i):
    print('LEN|   OCCURRENCES   |NR.')
    print_line()
    count_occurrences(i)


def user_check(name, passwd):
    if name in users and users[name] == passwd:
        return True
    else:
        print('wrong name or password, terminating the program.')
        exit(1)


def text_number_check(number):
    if not number.isdigit():
        print('not a number, terminating the program.')
        exit(1)
    if 1 <= int(number) <= 3:
        print_line()
        analyze(int(number) - 1)
        print_line()
        graph(int(number) - 1)
        exit(0)
    else:
        print('number out of range, terminating the program.')
        exit(1)


def main():
    in_name = input('username:')
    in_passwd = input('password:')

    user_check(in_name, in_passwd)

    print_line()
    say_hello(in_name)
    print_line()

    in_num = input('Enter a number btw. 1 and 3 to select: ')
    text_number_check(in_num)
    print_line()


if __name__ == "__main__":
    main()