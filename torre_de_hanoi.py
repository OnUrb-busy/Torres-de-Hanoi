# -*- coding: utf-8 -*-
"""Torre de hanoi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bEcSTsDk_01ZsC4mw2eGAK3hf3t2Ndct
"""

!pip install colorama

import time
from IPython.display import clear_output

class HanoiConsole:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.torres = {'A': [], 'B': [], 'C': []}
        self.movimentos = 0
        self.initialize_torres()

    def initialize_torres(self):
        self.torres['A'] = list(range(self.num_discos, 0, -1))
        self.torres['B'] = []
        self.torres['C'] = []

    def move_disco(self, origem, destino):
        disco = self.torres[origem].pop()
        self.torres[destino].append(disco)
        self.movimentos += 1
        self.print_torres()

    def resolver_hanoi(self, n, origem, auxiliar, destino):
        if n == 1:
            self.move_disco(origem, destino)
            return
        self.resolver_hanoi(n-1, origem, destino, auxiliar)
        self.move_disco(origem, destino)
        self.resolver_hanoi(n-1, auxiliar, origem, destino)

    def print_torres(self):
        clear_output(wait=True)
        max_height = self.num_discos
        width = 2 * self.num_discos + 1
        torres_visuais = {'A': [], 'B': [], 'C': []}

        for torre in ['A', 'B', 'C']:
            for i in range(max_height):
                if i < len(self.torres[torre]):
                    disco = self.torres[torre][i]
                    torres_visuais[torre].append(f"{' ' * (max_height - disco)}{'-' * (2 * disco - 1)}{' ' * (max_height - disco)}")
                else:
                    torres_visuais[torre].append(' ' * width)

        for nivel in range(max_height-1, -1, -1):
            for torre in ['A', 'B', 'C']:
                print(torres_visuais[torre][nivel], end=' ')
            print()

        print(f"{'A'.center(width)} {'B'.center(width)} {'C'.center(width)}\n")
        print(f"Movimentos: {self.movimentos}")
        time.sleep(0.5)

def main():
    num_discos = int(input("Digite o número de discos: "))  # Entrada do usuário
    jogo = HanoiConsole(num_discos)
    jogo.resolver_hanoi(num_discos, 'A', 'B', 'C')
    print(f"Quantidade total de movimentos: {jogo.movimentos}")

if __name__ == "__main__":
    main()