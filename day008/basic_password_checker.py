letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_chars = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',
                 ':',';','<','=','>','?','@',
                 '[','\\',']','^','_','`',
                 '{','|','}','~']
digits = ['0','1','2','3','4','5','6','7','8','9']


def chec_strength(password):
  has_letter = False
  has_digits = False
  has_chars = False
  for ch in password:
    if ch in letters:
      has_letter=True
    elif ch in special_chars:
      has_chars=True
    elif ch in digits:
      has_digits=True
  if len(password)>=8:
    if (has_letter and has_chars) and (has_digits):
     return "strong password"
    else:
      return "Moderate"
  else:
    return "weak password"
print(chec_strength("agent67@193456#"))
