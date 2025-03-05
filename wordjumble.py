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

if __name__ == "__main__":
  jumbled_words = ['tefon', 'sokik', 'niumem', 'siconu']
  mac_words = '/usr/share/dict/words'
  words_dict = load_dictionary(mac_words)