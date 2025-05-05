#Ejercicio 18: Suma de los 100 números siguientes
print("Ejercicio 18: Suma de los 100 números siguientes")
# Pedir al usuario que ingrese un número.
# Lo que el usuario escribe siempre es str 
texto_ingresado = input("Por favor, ingresa un número entero: ")
# Conver el texto ingresado a un número entero.
# Como input() nos da texto, usamos int() para convertir ese texto a un número entero.
# Guardar este número entero en una variable llamada numero_inicial.
numero_inicial = int(texto_ingresado)
#Crear una variable para guardar la suma y la inicializamos en cero.
# Empieza en 0 porque aún no se ha sumado ningún número.  "acumulador".
suma_siguientes_100 = 0
# Aquí comienza un bucle 'for'.
# range(inicio, fin) crea una secuencia de números.
# El primer número siguiente es numero_inicial + 1.
# El último número que sumaremos será numero_inicial + 100.
for i in range(numero_inicial + 1, numero_inicial + 101):
  # Dentro del bucle, sumamos el valor actual de 'i' a nuestra suma_siguientes_100.
  # En cada paso, sumamos el número actual (i) al total que llevamos sumado.
  suma_siguientes_100 += i
# imprimimos el resultado.
print(f"La suma de los 100 números siguientes a {numero_inicial} es: {suma_siguientes_100}")
print("-----------------------")
print()

print("Ejercicio 19: Conversión de Euros a Dólares")
# Ejercicio 19: Conversión de Euros a Dólares
# Definir la tasa de cambio 
# Usamos float para decimales.
tipo_cambio_eur_usd = 1.08 # 1 Euro = 1.08 Dólares 
# Pedir al usuario la cantidad en euros.
texto_euros = input("Por favor, ingresa la cantidad en euros: ")
# Convertir el texto a un número decimal (float).
cantidad_euros = float(texto_euros)
# Calcular la cantidad en dólares.
# Multiplicamos euros por la tasa de cambio.
cantidad_dolares = cantidad_euros * tipo_cambio_eur_usd
# Imprimir el resultado.
# Se usa :.2f para mostrar 2 decimales en los dólares.
print(f"{cantidad_euros} euros equivalen a {cantidad_dolares:.2f} dólares (aprox).")

print("-----------------------")
print()
print("-----------------------")
print("Ejercicio 20: Área de un Rectángulo")
# Ejercicio 20: Área de un Rectángulo
# Pedir la altura del rectángulo.
# Convertir la entrada a float.
texto_altura = input("Por favor, ingresa la altura del rectángulo (puede ser decimal): ")
altura = float(texto_altura)

# Pedir la anchura del rectángulo.
# Convertir la entrada a float.
texto_anchura = input("Por favor, ingresa la anchura del rectángulo (puede ser decimal): ")
anchura = float(texto_anchura)
# Calcular el área (altura * anchura).
area = altura * anchura

# Imprimir el resultado.
print(f"El área del rectángulo con altura {altura} y anchura {anchura} es: {area}")

print("-----------------------")
print()
print("-----------------------")
print("Ejercicio 21: Mayor y Menor de Dos Números")
# Ejercicio 21: Mayor y Menor de Dos Números
# Pedir el primer número y convertirlo a float.
texto_num1 = input("Por favor, ingresa el primer número: ")
numero1 = float(texto_num1)

# Pedir el segundo número y convertirlo a float.
texto_num2 = input("Por favor, ingresa el segundo número: ")
numero2 = float(texto_num2)

# Usar estructuras condicionales (if, elif, else) para comparar.
# Si numero1 es mayor que numero2:
if numero1 > numero2:
  print(f"El número mayor es: {numero1}")
  print(f"El número menor es: {numero2}")
# Si no (elif), verificar si numero2 es mayor que numero1:
elif numero2 > numero1:
  print(f"El número mayor es: {numero2}")
  print(f"El número menor es: {numero1}")
# Si ninguna de las anteriores es verdadera (else), son iguales:
else:
  print("Ambos números son iguales.")
  

print("-----------------------")
print()
print("-----------------------")
print("Ejercicio 22: Números Impares Menores que un Entero Dado")
# Ejercicio 22: Números Impares Menores que un Entero Dado
# Pedir un número entero positivo.
# Convertir la entrada a int.
texto_limite = input("Por favor, ingresa un número entero positivo: ")
numero_limite = int(texto_limite)

# Verificar si el número es positivo.
if numero_limite > 0:
  # Mensaje introductorio.
  print(f"Números impares menores que {numero_limite}:")
  # Bucle para revisar números desde 1 hasta numero_limite-1.
  for num in range(1, numero_limite):
    # Usar el operador módulo (%) para saber si es impar.
    # Si num dividido entre 2 tiene residuo diferente de 0, es impar.
    if num % 2 != 0:
      # Si es impar, imprimir el número.
      print(num)
else:
  # Si el número no es positivo, mostrar un error.
  print("Por favor, ingresa un número entero positivo.")

print("-----------------------")
print()
print("-----------------------")
print("Ejercicio 23: Algoritmo de Euclides para el GCD")
# Ejercicio 23: Algoritmo de Euclides para el GCD
# Definir una función para calcular el GCD.
# Esta función toma dos parámetros: a y b.
def calcular_gcd(a, b):
  # Obtener el valor absoluto de los números (para manejar negativos).
  a = abs(a)
  b = abs(b)
  # Bucle while: se ejecuta mientras la condición sea verdadera. La condición 'b' es verdadera si b no es cero.
  # El bucle se repite hasta que b sea 0.
  while b:
    # Calcular el residuo de a dividido por b.
    residuo = a % b
    # Actualizar a con el valor actual de b.
    a = b
    # Actualizar b con el valor del residuo.
    b = residuo
    # Esto sigue los pasos del Algoritmo de Euclides.
  # Cuando el bucle termina, 'a' tiene el GCD.
  return a
# pedir los números al usuario y convertirlos a int.
texto_num1 = input("Por favor, ingresa el primer número entero: ")
num1 = int(texto_num1)

texto_num2 = input("Por favor, ingresa el segundo número entero: ")
num2 = int(texto_num2)

# Llamar a la función calcular_gcd con los números del usuario y guardar el valor que retorna la función en gcd_resultado.
gcd_resultado = calcular_gcd(num1, num2)

# Imprimir el resultado.
print(f"El máximo común divisor (GCD) de {num1} y {num2} es: {gcd_resultado}")

print("-----------------------")
print()
print("-----------------------")
print("Ejercicio 24: Ecuación de Segundo Grado")
# Ejercicio 24: Ecuación de Segundo Grado
# Importar el módulo math para usar la raíz cuadrada (sqrt).
import math
# Pedir los coeficientes a, b y c.
# Convertir las entradas a float para permitir decimales.
texto_a = input("Por favor, ingresa el coeficiente 'a': ")
a = float(texto_a)

texto_b = input("Por favor, ingresa el coeficiente 'b': ")
b = float(texto_b)

texto_c = input("Por favor, ingresa el coeficiente 'c': ")
c = float(texto_c)
# Calcular el discriminante (delta).Fórmula: delta = b^2 - 4*a*c
discriminante = b**2 - 4*a*c
# Usar condicionales para analizar el discriminante.
# Si el discriminante es mayor o igual a 0, hay soluciones reales.
if discriminante >= 0:
  # Verificar que 'a' no sea cero (si a=0 no es de segundo grado).
  if a != 0:
    # Calcular las dos soluciones usando la fórmula general.
    # math.sqrt() calcula la raíz cuadrada.
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    # Imprimir las soluciones.
    print("La ecuación tiene soluciones reales:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
  else:
    # Si a es 0, no es de segundo grado.
    print("El coeficiente 'a' no puede ser cero para una ecuación de segundo grado.")
# Si el discriminante es menor que 0, no hay soluciones reales.
elif discriminante < 0:
  print("La ecuación no tiene soluciones reales (tiene soluciones complejas).")