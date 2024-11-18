text: str = str(input("Write a sentence :"))
words: list[str] = text.split()
print(text)
if words:
    last_words = words[-1]
    print(f" The last word is {last_words} with length {len(last_words)}.")
else:
    print("You entered an empty sentence")
