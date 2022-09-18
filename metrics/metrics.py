import math


def get_metrics(time, user_input, text):
    user_input_text = ''.join(user_input)
    correct = correct_characters(user_input_text, text)

    wpm = get_wpm(correct, time)
    acc = get_acc(correct, len(text))

    return wpm, acc


def get_wpm(correct, time):
    words_per_second = (correct / 5) / time
    words_per_minute = words_per_second * 60

    return int(words_per_minute)


def get_acc(correct, total):
    acc = (correct / total) * 100
    acc = math.floor(acc * 100) / 100.0

    return acc


def to_next_word(text, ptr):
    while ptr < len(text) and text[ptr] != ' ':
        ptr += 1

    return ptr


def count_words(user_input, text):
    correct = 0
    i = j = 0
    while i < len(user_input) and j < len(text):
        if user_input[i] != text[j]:
            i = to_next_word(user_input, i)
            j = to_next_word(text, j)
        if not (i < len(user_input) and j < len(text)):
            break
        if user_input[i] == ' ' and text[j] == ' ':
            correct += 1
        i += 1
        j += 1
    
    return correct


def correct_characters(user_input, text):
    correct = 0
    i = j = 0
    while i < len(user_input) and j < len(text):
        if user_input[i] == ' ' and text[j] != ' ':
            while text[j] != ' ':
                j += 1
        elif user_input[i] != ' ' and text[j] == ' ':
            while user_input[i] != ' ':
                i += 1
        
        if user_input[i] == text[j]:
            correct += 1

        if not (i < len(user_input) and j < len(text)):
            break
        i += 1
        j += 1
    
    return correct