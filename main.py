def main():
    text = read_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    character_counts.sort(reverse=True, key=sort_on)

    print(f"{word_count} words found in the book\n\n")

    for item in character_counts:
        character = item["character"]
        character_count = item["count"]
        if not character.isalpha():
            continue
        print(f"The '{character}' character was found {character_count} times")


def sort_on(dict):
    return dict["count"]


def read_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def convert_to_list(dict):
    character_count = []
    for key in dict:
        character_count.append({"character": key, "count": dict[key]})
    return character_count


def get_character_counts(text):
    character_count_map = {}
    lowercase_text = text.lower()
    for character in lowercase_text:
        if character in character_count_map:
            character_count_map[character] += 1
        else:
            character_count_map[character] = 1
    character_count_list = convert_to_list(character_count_map)
    return character_count_list


main()