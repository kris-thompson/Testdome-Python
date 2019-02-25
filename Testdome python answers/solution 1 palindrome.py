def is_palindrome(word):
     fiword = word
     baword = fiword[::-1]
     if baword.lower() == fiword.lower():  
         return True
     else:
         return False
    
print(is_palindrome('Deleveled'))