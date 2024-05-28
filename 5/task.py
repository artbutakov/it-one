from difflib import SequenceMatcher


with open('nouns.txt', 'r', encoding='utf-8') as file:
    nouns = file.read().split('\n')


def glue_nouns(user_noun: str = input('Enter noun: ')):
    gotten_nouns = list()
    for index, noun in enumerate(nouns):
        if index < len(nouns) - 1 and user_noun != noun:
            match = SequenceMatcher(a=user_noun, b=noun).find_longest_match()
            sequence = user_noun[match.a:match.a + match.size]
            if match.size > 1 and user_noun.endswith(sequence) and noun.startswith(sequence):
                gotten_nouns.append(user_noun[:-match.size] + noun)
    return gotten_nouns


print(', '.join(glue_nouns()))
