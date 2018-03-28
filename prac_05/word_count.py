WORD_COUNTS = {}


def main():
    input_text = input("Enter a Sentence: ")
    word_list = input_text.split()

    for word in word_list:
        if word in WORD_COUNTS:
            WORD_COUNTS[word] += 1
        else:
            WORD_COUNTS[word] = 1

    longestString = max(WORD_COUNTS, key=len)
    for key in sorted(WORD_COUNTS.keys()):
        print("{:>{}} : {}".format(key, len(longestString), WORD_COUNTS[key]))


main()
