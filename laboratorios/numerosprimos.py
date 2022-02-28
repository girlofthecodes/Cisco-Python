"""
Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.

¿Complicado? De ningúna manera. Por ejemplo, 8 no es un número primo, ya que puedes dividirlo entre 2 
y 4 (no podemos usar divisores iguales a 1 y 8, ya que la definición lo prohíbe).
Por otra parte, 7 es un número primo, ya que no podemos encontrar ningún divisor para el.
Tu tarea es escribir una función que verifique si un número es primo o no.
La función:
Se llama isPrime.
Toma un argumento (el valor a verificar).
Devuelve True si el argumento es un número primo, y False de lo contrario.
Sugerencia: intenta dividir el argumento por todos los valores posteriores (comenzando desde 2) y verifica 
el resto: si es cero, tu número no puede ser un número primo; analiza cuidadosamente cuándo deberías detener 
el proceso.
Si necesitas conocer la raíz cuadrada de cualquier valor, puedes utilizar el operador **. Recuerda: la raíz 
cuadrada de x es la misma que x0.5
Complementa el código en el editor.
Ejecuta tu código y verifica si tu salida es la misma que la nuestra.
"""
def isPrime(num):
    for contador in range(2,num): 
        if num % contador == 0:
            break
        else: 
            print(num)
            break
        
for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()