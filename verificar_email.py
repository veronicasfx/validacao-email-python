email = input().strip()

def verificar_email(email):
  if "@" in email:
    if email [0] != "@" and email [-1] != "@" and " " not in email:
        return True
  return False
    
resultado = verificar_email(email)
if resultado:
  print("E-mail válido")
  
else:
  print("E-mail inválido")
