import fuzzymatch as f

class Match:
  def __init__(self, start_string, end_string, start_index, end_index, fuzzscore):#end = start of 2nd string
    self.start_string = start_string
    self.end_string= end_string
    self.start_index = start_index
    self.end_index = end_index
    self.fuzzscore = fuzzscore


match_list = []

ini_str = input("Enter DNA string: ").upper()
n = len(ini_str) #28
best_start_string = ""
best_start_index = 0
best_end_string = ""
best_end_index = 0
for i in range(n - 27):
  max_local_fuzzscore = 0
  for x in range(4):
    if(x==0): #MUST BE REPLACED WITH if"""i + 22 + x < n - 6""" SO IT ACTUALLY GOES THROUGH 16 TO 19 BP GAP
      current_local_fuzzscore = f.fuzzmatch(ini_str[i : i + 6], ini_str[i + 22 + x: i + 28 + x])
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