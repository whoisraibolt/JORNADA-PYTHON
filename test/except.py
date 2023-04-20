import logging

# Configura o nível de logging
logging.basicConfig(filename = 'log_2.txt', level = logging.ERROR)

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 / num2

    print("O resultado da divisão é:", resultado)
except ZeroDivisionError:
    logging.error("Ocorreu um erro ao dividir por zero!")
except:
    logging.critical("Ocorreu um erro inesperado!")
finally:
    print("Obrigado por utilizar o programa!")