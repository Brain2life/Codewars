# https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/python
# Find the way to remove consecutive strings

def remove_consecutive_duplicates(s):
  input = s.split()
  previous_value = None
  output = ""

  for element in input:
    if element != previous_value:
      output += " " + element
      previous_value = element

  return output.strip()


print(remove_consecutive_duplicates("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))

# Another "lazy" solution is to use groupby() function from itertools

# from itertools import groupby

# def remove_consecutive_duplicates(s):
#     return ' '.join(k for k,_ in groupby(s.split()))