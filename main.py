#!/bin/python3
from os import system
from random import choice

verm = '\033[31;1m'
verd = '\033[32;1m'
amar = '\033[33;1m'
azul = '\033[34;1m'
n = '\033[37;1m'
f = '\033[m'
l = '\033[4m'

banner = open("banner.txt").read()

def limp():
    system('cls||clear')

def ent():
    input('\nenter para continuar')

def calcu(eq=''):
    if 'x' in eq: eq = eq.replace('x', '*')
    if ',' in eq: eq = eq.replace(',', '.')
    if '^' in eq: eq = eq.replace('^', '**')
    if '{' in eq: eq = eq.replace('{', '(')
    if '}' in eq: eq = eq.replace('}', ')')
    if '[' in eq: eq = eq.replace('[', '(')
    if ']' in eq: eq = eq.replace(']', ')')
    return eval(eq)

cores = verd, azul, amar
while True:
    limp()
    cor = choice(cores)
    print(cor+banner+f)
    try:
        opc = input(f'{n}[ {cor}1 {n}] > {cor}calculadora\n{n}[ {cor}2 {n}] > {cor}operadores aritiméticos\n\n{n}[ {cor}0{n} ] > {cor}sair\n\n{cor}>>>{n} ').strip()[0]
    except:
        continue
    match opc:
        case '1':
            while True:
                limp()
                try:
                    equacao = input(f'{n}Equação (fim para sair):\n\n{verd}').strip().lower()
                except:
                    continue
                if equacao == '': continue
                if 'fim' in equacao: break
                try:
                    resu = calcu(equacao)
                except:
                    continue
                print(f'{n}{equacao} = {verd}{resu}{f}')
                ent()

        case '2':
            print(f'''
    {verd}+{n} = {l}adição{f}
    {verd}-{n} = {l}subtração{f}
    {verd}x{n} ou {verd}*{n} = {l}multiplicação{f}
    {verd}**{n} ou {verd}^{n} = {l}potenciação{f}
    {verd}/{n} = {l}divisão{f}
    {verd}//{n} = {l}divisão inteira{f} {n}({amar}o valor será a parte inteira da divisão{n})
    {verd}%{n} = {l}resto da divisão{f} {n}({amar}o valor será o resto da divisão{n})
    {verd}(){n} = {l}parênteses para o cálculo começar primeiro{f}''')
            ent()

        case '0':
            break
limp()
print(azul+"Até mais!"+f)
