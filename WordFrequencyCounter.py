from collections import Counter

text = input ("Enter the sentence: ")
words = text.lower().split()
counts = Counter(words)

for word, count in counts.items():
    print(f"{word}: {count}")

    import string

text = input("Enter the sentence: ")
text = text.translate(str.maketrans('', '', string.punctuation))  # 쉼표, 마침표 등 제거
words = text.lower().split()
