def get_wpm(time, user_input, text):
    user_input_text = ''.join(user_input)
    correct = count_words(user_input_text, text)

    words_per_second = correct / time
    words_per_minute = words_per_second * 60

    return int(words_per_minute)


def to_next_word(text, ptr):
    while text[ptr] != ' ' and ptr < len(text):
        ptr += 1

    return ptr


def count_words(user_input, text):
    correct = 0
    i = j = 0
    while i < len(user_input) and j < len(text):
        if user_input[i] != text[j]:
            i = to_next_word(user_input, i)
            j = to_next_word(text, j)

        if user_input[i] == ' ' and text[j] == ' ':
            correct += 1
        i += 1
        j += 1
    
    return correct