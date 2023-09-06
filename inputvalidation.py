accepted_characters = ['A','T','C','G']
dna_string = input("Enter DNA string: ").upper()

class InvalidInputError(Exception):
    """Exception raised for invalid characters in DNA Input.

    Attributes:
      error_string --  The invalid DNA input
      message -- explanation of the error
    """

    def __init__(self, error_string):
        invalid_dict = {}
        for i in range(len(dna_string)):
          if dna_string[i] not in accepted_characters:
            invalid_dict.setdefault(dna_string[i], 0)
            invalid_dict[dna_string[i]] = invalid_dict[dna_string[i]] + 1 #USE INDICES AND NOT COUNTS
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
    error_string = "DNA string entered is only " + str(len(dna_string)) + " characters long, it needs to be a minimum of 28 characters."
    self.message = error_string
    super().__init__(self.message)
    
  
for i in range(len(dna_string)):
  if dna_string[i] not in accepted_characters:
    raise InvalidInputError(dna_string)
  elif len(dna_string) < 28:
    raise InvalidLengthError(dna_string)
  break
