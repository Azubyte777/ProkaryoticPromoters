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