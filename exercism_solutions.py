from collections import Counter
from typing import List
import math
from collections import OrderedDict
from numpy import empty
import re
from typing import Dict


# anagram
def anagram(word: str, possible_anagram: str) -> bool:
    return bool(lambda x, y: Counter(sorted(word.lower())) == Counter(sorted(possible_anagram.lower())))


# armstrong number
def armstrong_number(number: int) -> str:
    number_sum = sum([int(i) ** len(str(number)) for i in str(number)])
    if number_sum == number:
        return "Given number is an Armstrong Number."
    else:
        return "Given number is not an Armstrong Number."


# collatz conjecture
def collatz_conjecture(number: int) -> List[int]:
    steps = []
    numbers = []
    step = 0
    numbers.append(number)
    steps.append(step)

    while number != 1:
        if number % 2 == 0:
            num = number / 2
        else:
            num = 3 * number + 1
        number = num
        step += 1

        numbers.append(int(num))
    return numbers


# dart
def dart(x: int, y: int) -> (int, int):
    if not isinstance(x, int) or not isinstance(y, int):
        print("One of the values is not an integer type.")
        quit()
    elif x < 0:
        print(f"Given value of x should be greater than 0.")
        exit(1)
    elif y < 0:
        print(f"Given value of y should be greater than 0.")
        exit(1)
    else:
        radius = math.sqrt(x ** 2 + y ** 2)
        if radius > 10:
            earned_points = 0
        elif 10 >= radius > 5:
            earned_points = 1
        elif 5 >= radius > 1:
            earned_points = 5
        else:
            earned_points = 10

        return earned_points, radius


# square difference
def square_difference(num_li: list) -> int:
    if not isinstance(num_li, list):
        print("Given values are not a list type.")
        quit()
    elif not all(isinstance(x, int) for x in num_li):
        print("Not all elements in list are integer type.")
        quit()
    else:
        square_of_the_sum = sum(num_li)**2
        sum_of_the_squares = sum([i**2 for i in num_li])
        return square_of_the_sum - sum_of_the_squares


# flatten array
def flatten_array(input_list: list) -> list:
    flattened_list = []
    for element in input_list:
        if isinstance(element, int):
            flattened_list.append(element)
        elif isinstance(element, list):
            for sublist_element in element:
                if isinstance(sublist_element, type(None)):
                    continue
                flattened_list.append(sublist_element)
    return flattened_list


# grade schools
def grade_schools(name: str, grade: int) -> list:
    students = OrderedDict()
    students[name] = grade
    return list(zip(students.keys(), students.values()))


# hamming distance
def hamming_distance(str1: str, str2: str) -> int:
    if not isinstance(str1, str) or not isinstance(str2, str):
        print("One of the values are not string type.")
        quit()
    else:
        if len(str1) != len(str2):
            print("Strings are not equal")
            quit()
        hamming = sum(i != j for i, j in zip(str1, str2))
        return hamming


# high scores
def high_scores(score_list: list) -> str:
    best_score = max(score_list)
    worst_score = min(score_list)
    last_score = sorted(score_list)[-1]
    top_three_score = sorted(set(score_list), reverse=True)[:3]
    avg_score = sum(score_list) / len(score_list)
    scores_report = f"best score: {best_score}, \n" \
                    f"worst score: {worst_score}, \n" \
                    f"last score: {last_score}, \n" \
                    f"top three score: {top_three_score}, \n" \
                    f"avg score: {avg_score} \n"
    return scores_report


# word isogram
def word_isogram(word: str) -> str:
    given_word = word.lower()

    len_set_of_word = len(set(given_word))
    print("Length of given word set: ", len_set_of_word)

    len_of_word = len(given_word)
    print("Length of given word: ", len_of_word)

    if len_set_of_word == len_of_word:
        return f"Given word: {word} is an isogram"
    else:
        return f"Given word: {word} is not an isogram"


# check leap year
def check_leap_year(year: int) -> bool:
    if not isinstance(year, int):
        print("Wrong type of input value.")
        quit()
    elif len(str(year)) != 4:
        print("Wrong length of input. Given value should be a four digit number.")
        quit()
    else:
        print("The year " + str(year) + " is leap:")
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False


# luhn
def luhn(num: int, check=False) -> int:
    num_len = [char for char in str(num)]
    alternately_list = empty((len(num_len), ), int)
    alternately_list[::2] = 2
    alternately_list[1::2] = 1

    nums = [int(number) for number in str(num)]
    multiplied_list = ([x*y for x, y in zip(nums, alternately_list)])

    num_list = []
    for i in multiplied_list:
        if i > 9:
            num_list.append(i-9)
        else:
            num_list.append(i)
    if check:
        result = (sum(num_list) % 10)
        return result
    else:
        last_number = 10 - (sum(num_list) % 10)
        return last_number


# pangram
def pangram(text: str) -> str:
    if len(text.lower()) == len(set(text.lower())):
        return f"Sentence: {text}. \n Given sentence is a pangram."
    else:
        return f"Sentence: {text}. \n Given sentence is not a pangram."


# perfect numbers
def perfect_numbers(n: int) -> str:
    if not isinstance(n, int):
        print("[WARNING] Given number is not 'integer' type. Only integers are allowed.")
        quit()
    elif n < 0:
        print("[WARNING] You gave an negative number. Allowed numbers are positive integers.")
        quit()
    else:
        divisors = [j for j in [i for i in range(1, n+1)] if n % j == 0][:-1]
        sum_of_divisors = sum(divisors)

        if n == sum_of_divisors:
            return "Perfect"
        elif n < sum_of_divisors:
            return "Abundant"
        else:
            return "Deficient"


# raindrop
def raindrop(number: int) -> str:
    tears = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }
    return ''.join(tears[i] for i in tears if number % i == 0)


# reverse string
def reverse_string(text: str) -> str:
    return text[::-1]


# run length encoding
def encoding(seq: str) -> dict:
    letters_dict = dict()
    for letter in seq:
        if letter not in letters_dict.keys():
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return letters_dict


def decoding(letters_dict):
    if type(letters_dict) != dict:
        print("WARNING! Given argument is not 'dict / dictionary' type.")
    else:
        return ''.join([key*value for key, value in letters_dict.items()])


# saddle points
def saddle_points(matrix):
    row_max_values = []
    row_min_values = []
    col_max_values = []
    col_min_values = []

    for row in matrix:
        row_max_values.append(row.max())
        row_min_values.append(row.min())

    for col in matrix.T:
        col_max_values.append(col.max())
        col_min_values.append(col.min())

    saddle_points_list = []

    for i in row_min_values:
        for j in col_max_values:
            if i == j:
                saddle_points_list.append(i)

    for i in row_max_values:
        for j in col_min_values:
            if i == j:
                saddle_points_list.append(i)

    return saddle_points_list


# secret handshake
def secret_handshake(number: int) -> list:
    encoder = {
        1: "wink",
        10: "double blink",
        100: "close your eyes",
        1000: "jump"
    }

    binary_number = int("{0:b}".format(number))
    num_list = []

    for key, value in encoder.items():
        if binary_number >= 10000:
            num_list.append(value)
            num_list = num_list[::-1]
        elif binary_number > key < 10000:
            num_list.append(value)
    return num_list


# series
def series(num_string: str, digit_subset: int) -> list:
    if not len(num_string):
        print("WARNING! Given string length is equal to 0.")
        exit(1)
    elif digit_subset > len(num_string):
        print(f"WARNING! Given substring size is greater than length of string. Proper subset length is {len(num_string)}.")
        exit(1)
    else:
        return [num_string[i:i + digit_subset] for i in range(len(num_string) - (digit_subset - 1))]


# sublist
def is_sublist(list_1: list, list_2: list) -> str:
    if all(elem in list_2 for elem in list_1) and len(list_1) == len(list_2):
        return "Given lists are equal"
    elif all(elem in list_2 for elem in list_1):
        return "List_1 is a sublist of list_2"
    else:
        return "list_1 is not a superlist of, sublist of or equal to list_2"


# triangle
def check_triangle(*args: int) -> str:
    # check if args are int or float
    for i in args:
        if not isinstance(i, (int, float)):
            print(f"{i} is not valid format.")
            exit(1)

    # sort values and check values
    a, b, c = sorted(args)
    if a == b == c:
        return 'Equilateral triangle'
    elif a == b or a == c or b == c:
        return 'Isosceles triangle'
    else:
        return 'Scalene triangle'


# two ferry
def two_fer(name: str) -> str:
    return f"One for {name}, one for me."


# word count
def word_count(sentence: str) -> Dict[str]:
    word_counts = dict()  # create dictionary
    lower_sentence = sentence.lower()  # make sentence lowercase
    lower_sentence = re.sub(r"[^\w\s]", "", lower_sentence)  #
    words = lower_sentence.split()  # split sentence into single words

    for word in words:  # loop over words
        if word in word_counts:  # if word is in word_counts dictionary add next occurrence
            word_counts[word] += 1
        else:  # if word does not exist in word_counts dictionary initialize as first occurrence
            word_counts[word] = 1
    return word_counts
