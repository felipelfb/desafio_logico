def number_of_characters(phrase):
    number_of_chars = {}
    phrase = phrase.lower()
    for char in phrase:
        if char not in number_of_chars:
            number_of_chars[char] = 1
        else:
            number_of_chars[char] += 1
    return number_of_chars


def count_running_letters(phrase):
    phrase = phrase.lower()
    count = 0
    previous_letter = phrase[0]
    result = ''
    for index in range(len(phrase)):
        if phrase[index] == previous_letter:
            count += 1
        else:
            result += str(count) + previous_letter
            count = 1
            previous_letter = phrase[index]
    result += str(count) + previous_letter
    return result
