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

def solve_jumbles(jumbled_words, dictionary):
    """
    Solves individual jumbled words using dictionary lookup
    Returns: list of solved words
    """
    solved_words = []
    for word in jumbled_words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in dictionary:
            # Take the first solution
            solved_words.append(dictionary[sorted_word][0])
    return solved_words

if __name__ == "__main__":
  jumbled_words = ['tefon', 'sokik', 'niumem', 'siconu']
  mac_words = '/usr/share/dict/words'
  words_dict = load_dictionary(mac_words)

  # Solve each jumbled word
  solved_words = solve_jumbles(jumbled_words, words_dict)
  print(f"\nJumbled Words: {jumbled_words}")
  print(f"\nSolved Words: {solved_words}")