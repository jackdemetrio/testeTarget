frase = input("Digite uma frase ou uma palavra: ")

contar_a = frase.lower().count('a')

if contar_a > 0:
    print(f"A letra 'a' aparece {contar_a} vezes na frase.")
else:
    print("A letra 'a' não está presente na frase.")
