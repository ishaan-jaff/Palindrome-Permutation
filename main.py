"""
For a given string, find whether or not a permutation of this string is a palindrome. You should return TRUE if such a permutation is possible and FALSE if it isn’t possible.


"""

from collections import defaultdict

def permute_palindrome(s):
  # count chars in s
  # check 
    # need all counts to be even, 
    # at max one count can be odd
  counts = defaultdict(int)
  for c in s:
    counts[c] +=1
  print(counts)

  seen_odd = False # to allow for one odd
  for c in counts:
    if counts[c] % 2 == 1:
      if seen_odd:
        return False
      seen_odd = True
  return True
  

print(permute_palindrome("peas"))
print(permute_palindrome("aba"))
print(permute_palindrome("abba"))
print(permute_palindrome("code"))