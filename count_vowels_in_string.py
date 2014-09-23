def count_vowels_in_string(s):
 
  vowels_count = 0
   
  for character in s:
    if character in ['a', 'e', 'i', 'o', 'u']:
      vowels_count += 1

  return vowels_count
  
print "Number of vowels:", count_vowels_in_string('azcbobobegghakl')