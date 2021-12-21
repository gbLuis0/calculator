#!/bin/python3
from os import system
from random import choice

verm = '\033[31;1m'
verd = '\033[32;1m'
amar = '\033[33;1m'
azul = '\033[34;1m'
n = '\033[37;1m'
fi = '\033[m'

banner = f'{azul}{open("banner.txt").read()}{fi}'

def limp():
    system('cls||clear')

def ent():
    input('\nenter para continuar')

def calcu(eq=''):
    if 'x' in eq:
        eq.replace('x', '*')
    return eval(eq)

while True:
    cores = verd, azul, amar
    cor = choice(cores)
    limp()
    print(banner)
    opc = input(f'{n}[ {cor}1 {n}] > {cor}calculadora\n{n}[ {cor}2 {n}] > {cor}operadores aritiméticos\n\n{n}[ {cor}0{n} ] > {cor}sair\n\n{cor}>>>{n} ').strip()[0]
    match opc:
        case '1':
            while True:
                limp()
                equacao = input(f'{n}Equação (fim para sair):\n\n{verd}').strip().lower()
                if 'fim' in equacao: break
                print(f'{n}{equacao} = {verd}{calcu(equacao)}{fi}')
                ent()
        case '2':
            print()
            ent()
        case '3':
            break
