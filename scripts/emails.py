from ast import pattern
import re
class example1: 

    pattern = ([A-Z] + '@' + 'gmail.com') # Pattern that emails inside the email file follow.

  
    result = re.sub(pattern, '','@mlh.io') in emails.csv # changes the "@gmail.com" section to "@mlh.io"
  
    
    print(pattern + result) in newfile # prints the end product which is the name of the email plus the "@mlh.io" section as a single string inside a new file.
   
