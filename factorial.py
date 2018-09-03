# -*- coding: utf-8 -*-

def run():
  number = int(input('Ingresa un número: '))
  result = factorial(number)
  print('Resultado {}'.format(result))

def factorial(n):
  if n == 0 or n == 1:
    return 1

  return factorial(n - 1) * n


if __name__ == '__main__':
  run()
