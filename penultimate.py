#Brian Enwonwu, Cody Speh, Jean Jacques Gbekou and Jimmy Moloney.
from prettytable import PrettyTable

# Start of the fuzzmatch function
""" Function that takes 2 string parameters from the current window and compares them to the prokaryotic promoter sequences
   @param string_one - The first string
   @param string_two - The second string
   @return - The number of matches of both strings to the prokaryotic promoter sequences
"""
def fuzzmatch(string_one, string_two): # The function
    match_count_one = 0
    match_count_two = 0
    thirty_five_cs = "TTGACA"  # Variable to store the -35 CS sequence
    ten_cs = "TATAAT" # Variable to store the -10 CS sequence
    for i in range(6):
      if string_one[i] == thirty_five_cs[i]: 
        match_count_one+=1 
      if string_two[i] == ten_cs[i]:
        match_count_two+=1
    return match_count_one+match_count_two
# End of the fuzzmatch function

# Start of the InvalidInputError class
""" InvalidInputError class throws an exception in case of invalid characters in DNA input 
    Attributes:
    error_string --  The invalid DNA input
    message -- explanation of the error
"""
class InvalidInputError(Exception):
  def __init__(self, error_string):
    invalid_dict = {} # A dictionary to store the invalid characters
    highlighted_string = ""
    
    """ 
    After the initial string (sequence) has been inputted,
    The for loop checks if each nucleotide is part of the accepted list of nucleotides
    Invalid characters get highlighted and stored in a dictionary
    """
    for i in range(len(ini_str)): 
      if ini_str[i] not in accepted_characters: # Checks is character is valid
        char = ini_str[i] # Invalid character gets stored in the char variable
        highlighted_string += f"\033[1;31m{char}\033[0m" # the character gets highlighted 
        invalid_dict[i] = ini_str[i] # invalid char gets added to the dictionary
      else:
        highlighted_string += ini_str[i] 
      error_string = str(invalid_dict) # A copy of the dictionary in string format is stored in the error_string variable
      self.message = error_string # The error message (whole input with invalid characters highlighted) gets stored in the message variable
      super().__init__(self.message) # The error message gets displayed
    print('\n' + highlighted_string + '\n') # Thw whole input with invalid characters highlighted gets displayed
# End of the InvalidInputError class

# Start of the InvalidLengthError class
""" InvalidLengthError class throws an exception if the DNA input is less than 28 characters or greater than 10,000 characters
    Attributes:
    error_string --  The invalid DNA input
    message -- Explanation of the error
"""
class InvalidLengthError(Exception):
  def __init__(self, error_string):
    error_string = "DNA string entered is " + str(len(ini_str)) + " characters long, it needs to be a between 28 and 10,000 (inclusive) characters." 
    self.message = error_string 
    super().__init__(self.message) 
# End of the InvalidLengthError class

# Beginning of the Match class
""" The object class below is meant to store sequence matches from our window search alongside the matches string indexes and fuzzscores
"""
class Match:
  def __init__(self, start_string, end_string, start_index, end_index, fuzzscore):#end = start of 2nd string
    self.start_string = start_string
    self.end_string= end_string
    self.start_index = start_index
    self.end_index = end_index
    self.fuzzscore = fuzzscore
  
accepted_characters = ['A', 'T','C', 'G', 'U', 'K', 'B', 'V', 'S', 'N', 'W', 'D', 'Y', 'R', 'H']  
  
again = True # Flag for our while loop
while again==True:
  
  ini_str = input("Enter DNA string: ").upper()
  if len(ini_str) < 28 or len(ini_str) > 10000:
    raise InvalidLengthError(ini_str) # Exception gets thrown if the length of the sequence is not between 28 and 10,000 base pairs
  for i in range(len(ini_str)):
    if ini_str[i] not in accepted_characters:
      raise InvalidInputError(ini_str) # Exception gets thrown if any invalid character has been located in the sequence 
  
  
  match_list = []

  """ The nested for loop below window searches through the DNA input and repeatedly runs the fuzzy match function to 
      compare the strings to the prokaryotic promoter sequences
  """
  n = len(ini_str) #28
  best_start_string = ""
  best_start_index = 0
  best_end_string = ""
  best_end_index = 0
  for i in range(n - 27):
    max_local_fuzzscore = 0
    for x in range(4): # This second for loop is to scan between the possible 16bp and 19bp distances between sequences
      if(i + x <= n - 28):
        current_local_fuzzscore = fuzzmatch(ini_str[i : i + 6], ini_str[i + 22 + x: i + 28 + x]) 
        if current_local_fuzzscore > max_local_fuzzscore:
          max_local_fuzzscore = current_local_fuzzscore
          best_start_string =  ini_str[i : i + 6]
          best_start_index = i
          best_end_string = ini_str[i + 22 + x: i + 28 + x]
          best_end_index = i + 22 + x
    match_list.append(Match(best_start_string,best_end_string,best_start_index,best_end_index,max_local_fuzzscore)) 
    match_list.sort(key=lambda x:x.fuzzscore, reverse = True) #Sorts output by fuzzscore in descending order
  
  #This creates our output table and adds our Match objects to it
  for obj in match_list:
    table = PrettyTable(['-35 String','-10 String', '-35 Start Index', '-10 Start Index', 'Fuzzy Score'])
    table.add_row([obj.start_string, obj.end_string, obj.start_index, obj.end_index, obj.fuzzscore])
    print(table)

  # The loop below gives the opportunity to the user to enter another DNA sequence: N for declining and Y for accepting
  while True: 
    again = input("\nAre you submitting another sequence? Y/N ").strip().upper() # Gets user choice
    if again == "Y": # User has can input another DNA sequence
      again = True 
      break
    elif again == "N": # Program stops
      again = False
      break
    else:
      print("\nResponse must be either Y or N") # Y and N are the only valid responses, if the user enters anything else,
                                                # the program will keep asking for valid input
