from collections import defaultdict


def main():
    with open("resourse_1.txt", "r", encoding="utf-8") as fin:
        text = fin.read()
        words = text.split()
        words_dict = defaultdict(int)
        for el in words:
            if el.isalpha():
                words_dict[el] += 1

        words_sorted = sorted(words_dict.items(), key=lambda x: (-x[1], x[0]))

        with open("result_1.txt", "w", encoding="utf-8") as fout:
            for word, count in words_sorted:
                print(word, count, file=fout)


if __name__ == '__main__':
    main()
