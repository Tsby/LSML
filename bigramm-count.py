import sys
import csv
import re


def mapper():
    pattern = re.compile(r"[a-z]+")
    for row in csv.reader(iter(sys.stdin.readline, '')):
        content = row[2]
        matches = list(pattern.finditer(content.lower()))
        for i in range(len(matches) - 1):
            word_1 = matches[i].group(0)
            word_2 = matches[i + 1].group(0)
            print("{}\t{}".format(f'{word_1} {word_2}', 1))


def reducer():
    word, number = next(sys.stdin).split('\t')
    number = int(number)
    for line in sys.stdin:
        current_word, current_number = line.split('\t')
        current_number = int(current_number)
        if current_word != word:
            print("{}\t{}".format(word, number))
            word = current_word
            number = current_number
        else:
            number += current_number
    print("{}\t{}".format(word, number))


if __name__ == '__main__':
    mr_command = sys.argv[1]
    {
        'map': mapper,
        'reduce': reducer
    }[mr_command]()