n = int(input("Digite o número de emails: "))

contador = 0

for i in range(n):
  email = input("Digite os emails:")
  if "@" not in email:
    contador = contador + 1
print("O número de emails sem @ é:", contador)