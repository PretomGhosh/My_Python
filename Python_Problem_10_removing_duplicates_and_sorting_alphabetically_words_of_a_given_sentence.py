from collections import Counter
def remove_duplicates(input_sentence):
    input_sentence = str(input_sentence)
    input_sentence = input_sentence.split(" ")
    unique_word = Counter(input_sentence)
    output = " ".join(unique_word.keys())
    output = output.split(" ")
    words_list = list(set(output))
    words_list.sort()
    final_output = " ".join(words_list)
    print(final_output)

input_sentence = input("Please enter a sentence : ")

remove_duplicates(input_sentence)

