def fuzzmatch(string_one, string_two):
  match_count_one = 0
  match_count_two = 0
  thirty_five_cs = "TTGACA"
  ten_cs = "TATAAT"
  for i in range(6):
    if string_one[i] == thirty_five_cs[i]:
      match_count_one+=1
    
    if string_two[i] == ten_cs[i]:
      match_count_two+=1
  return match_count_one+match_count_two

accepted_characters = ['A','T','C','G']
ini_str = input("Enter DNA string: ").upper()

class InvalidInputError(Exception):
    """Exception raised for invalid characters in DNA Input.

    Attributes:
      error_string --  The invalid DNA input
      message -- explanation of the error
    """

    def __init__(self, error_string):
        invalid_dict = {}
        for i in range(len(ini_str)):
          if ini_str[i] not in accepted_characters:
            invalid_dict.setdefault(ini_str[i], 0)
            invalid_dict[ini_str[i]] = invalid_dict[ini_str[i]] + 1 #USE INDICES AND NOT COUNTS,
        error_string = str(invalid_dict) 
        self.message = error_string
        super().__init__(self.message)

class InvalidLengthError(Exception):
  """Exception raised for input of invalid DNA length
  
  Attributes:
    error_string --  The invalid DNA input
    message -- Explanation of the error
  """
  
  def __init__(self, error_string):
    error_string = "DNA string entered is only " + str(len(ini_str)) + " characters long, it needs to be a minimum of 28 characters."
    self.message = error_string
    super().__init__(self.message)
    
  
for i in range(len(ini_str)):
  if ini_str[i] not in accepted_characters:
    raise InvalidInputError(ini_str)
if len(ini_str) < 28:
  raise InvalidLengthError(ini_str)



class Match:
  def __init__(self, start_string, end_string, start_index, end_index, fuzzscore):#end = start of 2nd string
    self.start_string = start_string
    self.end_string= end_string
    self.start_index = start_index
    self.end_index = end_index
    self.fuzzscore = fuzzscore


match_list = []

#ini_str = input("Enter DNA string: ").upper()
n = len(ini_str) #28
best_start_string = ""
best_start_index = 0
best_end_string = ""
best_end_index = 0
for i in range(n - 27):
  max_local_fuzzscore = 0
  for x in range(4):
    if(i + x <= n - 28):
      current_local_fuzzscore = fuzzmatch(ini_str[i : i + 6], ini_str[i + 22 + x: i + 28 + x])
      if current_local_fuzzscore > max_local_fuzzscore:
        max_local_fuzzscore = current_local_fuzzscore
        best_start_string =  ini_str[i : i + 6]
        best_start_index = i
        best_end_string = ini_str[i + 22 + x: i + 28 + x]
        best_end_index = i + 22 + x
  match_list.append(Match(best_start_string,best_end_string,best_start_index,best_end_index,max_local_fuzzscore))   

for obj in match_list:
  print(obj.start_string, obj.end_string, obj.start_index, obj.end_index, obj.fuzzscore, sep=" ")

#if that second for loop actually works we can then pull out the best fuzzscore matches from the array, or even sort it or sth then show it in text form with colors maybe