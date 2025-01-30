#pedir dos numero, y mostrar la suma de esos numeros


print("escriba un numero")
numero1 = input()

print("escriba otro numero")
numero2 = input()

if numero1 not in range(100) or numero2 not in range(100):
    print("no es numero burro")
else:
    print(int(numero1) + int(numero2))
    print()
    input()

