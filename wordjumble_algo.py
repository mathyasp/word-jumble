from itertools import permutations

def load_dictionary(filepath):
    """
    Creates hash table from dictionary file
    Returns: dict where key = sorted letters, value = list of possible words
    """
    words_dict = {}
    with open(filepath, 'r') as file:
      for word in file:
        word = word.strip().lower()

        # Create key
        sorted_word = ''.join(sorted(word))

        # Add to dict, creating a new list if needed
        if sorted_word in words_dict:
          words_dict[sorted_word].append(word)
        else:
          words_dict[sorted_word] = [word]

    return words_dict

def solve_jumbles(jumbled_words, words_dict):
    """
    Solves individual jumbled words using dictionary lookup
    Returns: list of solved words
    """
    solved_words = []
    for word in jumbled_words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in words_dict:
            # Take the first solution
            solved_words.append(words_dict[sorted_word][0])
    return solved_words

def final_solution(solved_words, circled_positions, words_dict):
    """
    Extracts circled letters from solved words to find final solution
    Format: __-______ (2 letters, hyphen, 6 letters)
    Returns: formatted string with solution or "No answer found"
    """
    def get_circled_letters():
        """Helper function to extract circled letters from solved words"""
        letters = ''
        for i, word in enumerate(solved_words):
            for pos in circled_positions[i]:
                letters += word[pos]
        return letters

    def is_valid_word(letters):
        """Helper function to check if letters form a valid word"""
        sorted_letters = ''.join(sorted(letters))
        return sorted_letters in words_dict

    def try_combination(first, second):
        """Helper function to format solution if both parts are valid words"""
        if is_valid_word(first) and is_valid_word(second):
            return f"{words_dict[''.join(sorted(first))][0]}-{words_dict[''.join(sorted(second))][0]}"
        return None

    # Get all possible permutations of circled letters
    letter_bank = get_circled_letters()
    all_perms = [''.join(p) for p in permutations(letter_bank)]

    # Try each permutation
    for perm in all_perms:
        first_part = perm[:2]
        
        # Try 6-letter word
        solution = try_combination(first_part, perm[2:8])
        if solution:
            return solution
            
        # Try 5-letter word + extra letter
        second_part = perm[2:7]
        if is_valid_word(first_part) and is_valid_word(second_part):
            last_letter = perm[7] if len(perm) > 7 else ''
            return f"{words_dict[''.join(sorted(first_part))][0]}-{words_dict[''.join(sorted(second_part))][0] + last_letter}"

    return "No answer found"

if __name__ == "__main__":
    jumbled_words = ['tefon', 'sokik', 'niumem', 'siconu']
    mac_words = '/usr/share/dict/words'
    words_dict = load_dictionary(mac_words)
    circled_positions = [[2,4], [0,1,3], [4], [3,4]]

    # Solve each jumbled word
    solved_words = solve_jumbles(jumbled_words, words_dict)
    print(f"\nJumbled Words: {jumbled_words}")
    print(f"\nSolved Words: {solved_words}")

    print(final_solution(solved_words, circled_positions, words_dict))