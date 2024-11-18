from utils import all_words

# all_words = ["password"]


def correct(word1: str):
    min_score = len(word1) - 3
    word1 = word1.lower()
    best_word = {"word": None, "score": 0}
    for word2 in all_words:
        if len(word2) > len(word1) + 1 or len(word1) > len(word2) + 1:
            continue
        fail_match = 0
        max_failure_match = 2
        word2_score = 0
        word1_pointer = 0
        start = 0
        word1_letter_skip_chance = 2
        word2_letter_step_back_chance = 1
        # both_skip_chance = 2
        while not (
            fail_match >= max_failure_match
            or word1_pointer > len(word1) - 1
            or start >= len(word2)
        ):
            current_word1_char = word1[word1_pointer]
            for word2_pointer in range(start, len(word2)):
                current_word2_char = word2[word2_pointer]
                if current_word1_char == current_word2_char:
                    word2_score += 1
                    word1_pointer += 1
                    start = word2_pointer + 1
                    break

                # this condition helps for words like passwrod instead of password
                # skips a letter from word1 and tries to compare the next character with the current_word2_char
                if word1_letter_skip_chance > 0:
                    if word1_pointer < len(word1) - 1:
                        if word1[word1_pointer + 1] == current_word2_char:
                            word2_score += 1
                            word1_pointer += 2
                            start = word2_pointer + 2
                            word1_letter_skip_chance -= 1
                            break
                # this helps for words like this piassword instead of password
                # # piasswrod
                #       ^
                # # password
                #       ^
                if word2_letter_step_back_chance > 0:
                    if word2_pointer > 0:
                        if current_word1_char == word2[word2_pointer - 1]:
                            word2_score += 1
                            word1_pointer += 1
                            word2_letter_step_back_chance -= 1
                            break

                # elif
                # handle failure
                if word1_pointer > 0:
                    if current_word1_char == word1[word1_pointer - 1]:
                        word1_pointer += 1
                        break
                fail_match += 1
                if fail_match >= max_failure_match:
                    break

        if word2_score > best_word["score"]:
            best_word = {"word": word2, "score": word2_score}
    if best_word["score"] <= min_score:
        best_word = {"word": None, "score": 0}
    return best_word


if __name__ == '__main__':
    while True:
        user_word = input(">>>")
        if user_word == "fuck":
            break
        print(correct(user_word))
