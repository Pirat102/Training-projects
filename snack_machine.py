from collections import Counter
import pig_game


print(f"The value of __name__ in snack_machine is: {__name__}")


# def letter_sum_all(text):
#     return sum(Counter(text).values())


# def word_counter(text):
#     return sum(Counter(text.split()).values())



# ## Split the words, sum number of letters in each word, calculate the average lenght of the words
# def mean_word_lenght(text):
#     results = []
#     split = text.split()
#     for word in split:
#         c = Counter(word)
#         i = sum(c.values())
#         results.append(i)
#     average_lenght = round(sum(results) / len(results),2)
#     print(f"The average lenght of the word is: {average_lenght}")





# def main():
#     #txt = input("Type smth: ")
#     txt = "Aga lubi pływać w wodzie. Sprawie jej to przyjemność. Może w przyszłości zostanie ratowniczką? To byłoby coś!"

#     counter = Counter(txt)
#     dots = counter.get(".")
#     exclamation_marks = counter.get("!")
#     question_marks = counter.get("?")

#     all_letters = letter_sum_all(txt)
#     print(f"Number of all letters: {all_letters}")

#     sentences = dots + exclamation_marks + question_marks
#     print(f"Number of sentences: {sentences}")

#     spaces_count = counter[" "]
#     print(f"Number of all spaces: {spaces_count}")

#     letters_without_spaces = all_letters - spaces_count
#     print(f"Number of letters without spaces: {letters_without_spaces}")

#     all_words = letter_sum_all(txt.split())
#     print(f"Number of words: {all_words}")

#     words_split = txt.split()
#     most_common_words = Counter(words_split).most_common(1)
#     print(f"This is most common word: {most_common_words[0][0]}")

#     each_word = Counter(words_split).most_common()
#     print(f"Those are all words with the number of appearence : {each_word}")

#     mean_word_lenght(txt)



# main()
    









    