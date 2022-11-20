import random

class Word:
   """
   This class is responsible for getting and modifying the word being used.
   
   Args:
      self (Word ): An instance of Graphic 

   

   Attributes:
      correct_word (string): holds the value of the correct word
      working_word (list): holds the value of the masked word
      word_list (list): holds the list of possible words to choose from
      total_guessed_words (integer): holds the total number of letters guessed
   """
   def __init__(self):
      """ The class constructor

      Args: 
         self (Word): an instance of Word
      """
      self._word_list = ["argentina", "worldcup", "champion", "messi", "winner"]
      self._correct_word = random.choice(self._word_list)  
      self._working_word = []
      for _ in range(len(self._correct_word)):  
         self._working_word.append('_')
      


   """Check if the letter from the user exist in the word 
   if it exists call add_letter to replace underscores with the letter
   """
   def check_letter(self, letter):
      positions = []  
      position = 0
      for i in self._correct_word:  
         if letter == i:
            positions.append(position)  
             
         position += 1
      
      if len(positions) > 0:
         self.add_letter(letter, positions)
         return True
      else:
         return False
   
   """Recive a list with the positions in working_word to be repalced with letter"""
   def add_letter(self, letter, positions):  
      for i in positions:
         self._working_word[i] = letter
         
   
   def print_guessedWord(self):
      for i in self._working_word:
         print(f"{i} ", end='')
      print("")

   def user_wins(self):
      return  "".join(self._working_word) == self._correct_word
