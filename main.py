from math import *

E0 = 8.85E-12
m = 9.11E-31
e = 1.602E-19
h = 6.626E-34
h2 = 4.136E-15
c = 3E8


def calcula_raio(n):
    return E0 * (((n ** 2) * (h ** 2)) / (pi * m * (e ** 2)))


def calcula_velocidade(n):
    return (1 / E0) * (e ** 2 / 2 * n * h)


def calcula_lambda(v):
    return h / (m * v)


def calcula_energia_cinetica(n):
    return ((m * e ** 4) / (8 * (n ** 2) * (h ** 2) * (E0 ** 2)))/1.602E-19


def calcula_energia_potencial(n):
    return -(1 / (E0 ** 2)) * ((m * (e ** 4)) / (4 * (n ** 2) * (h ** 2)))/1.602E-19


def calcula_energia_total(kn, un):
    return kn + un


def calcula_ef_com_niveis(ni, nf):
    niveis = {1: -13.6, 2: -3.4, 3: -1.51, 4: -0.85, 5: -0.54, 6: -0.38, 7: -0.28}
    if nf > ni:
        return niveis[nf] - niveis[ni]
    else:
        return niveis[ni] - niveis[nf]
    
def calcula_ef_com_ff(ff):
    return h2*ff

def calcula_lambda_foton(Ef):
    return (h2*c)/Ef

def calcula_f_foton(Ef):
    return Ef/h2

def calcula_diferenca_de_ef(n, ef, option):
    niveis = {1: -13.6, 2: -3.4, 3: -1.51, 4: -0.85, 5: -0.54, 6: -0.38, 7: -0.28}
    if option == "absorcao":
        return niveis[n] + ef
    elif option == "emissao":
        return niveis[n] - ef
    
def calcula_nivel_com_ef(n):
    niveis = {1: -13.6, 2: -3.4, 3: -1.51, 4: -0.85, 5: -0.54, 6: -0.38, 7: -0.28}
    for key, value in niveis.items():
        if value >= n-0.1 and value <= n+0.1:
            return key

while True:

    print("Qual cálculo deseja realizar?\n")
    print("1) rn, vn, \u03BB, Kn, Un e En")
    print("2) E_fóton, f_fóton \u03BB_fóton")
    print("3) nf ou ni (absorção de fóton)")
    print("4) nf ou ni (emissão de fóton")

    while True:
        option = input("\nInsira o número da opção desejada (ou sair): ")
        if option == "sair":
            exit(0)
        elif option == "1" or option == "2" or option == "3" or option == "4":
            break
        else:
            print("Opção inválida! Digite novamente.\n")

    if option == "1":
        while True:
            n = input("Insira o valor de n: ")
            try:
                n = int(n)
                break
            except:
                print("Valor inválido. Insira um número inteiro.")

        rn = calcula_raio(n)
        vn = calcula_velocidade(n)
        lambn = calcula_lambda(vn)
        kn = calcula_energia_cinetica(n)
        un = calcula_energia_potencial(n)
        et = calcula_energia_total(kn, un)

        print("\nrn = {:.3e} m".format(rn))
        print("vn = {:.3e} m/s".format(vn))
        print("lambda = {:.3e} m".format(lambn))
        print("kn = {:.3e} eV".format(kn))
        print("un = {:.3e} eV".format(un))
        print("et = {:.3e} eV".format(et))

    elif option == "2":
        while True:
            ni = input("Insira o valor de ni: ")
            try:
                ni = int(ni)
                break
            except:
                print("Valor inválido. Insira um número inteiro.")
        while True:
            nf = input("Insira o valor de nf: ")
            try:
                nf = int(nf)
                break
            except:
                print("Valor inválido. Insira um número inteiro.")

        ef = calcula_ef_com_niveis(ni, nf)
        lambf = calcula_lambda_foton(ef)
        ff = calcula_f_foton(ef)

        print("\nEf = {:.3e} eV".format(ef))
        print("lambda_f = {:.3e} m".format(lambf))
        print("f_f = {:.3e} Hz".format(ff))

    elif option == "3":
        print("Você deseja calcular nf ou ni?")
        print("1) nf")
        print("2) ni")
        while True:
            option2 = input("\nInsira o número da opção desejada (ou sair): ")
            if option2 == "sair":
                exit(0)
            elif option2 == "1" or option2 == "2":
                break
            else:
                print("Opção inválida! Digite novamente.\n")
        
        print("Você possui o valor de f_fóton ou lambda_fóton?")
        print("1) f_fóton")
        print("2) lambda_fóton")
        while True:
            option3 = input("\nInsira o número da opção desejada (ou sair): ")
            if option3 == "sair":
                exit(0)
            elif option3 == "1" or option3 == "2":
                break
            else:
                print("Opção inválida! Digite novamente.\n")
        
        if option2 == "1":
            while True:
                ni = input("\nInsira o valor de ni: ")
                try:
                    ni = int(ni)
                    break
                except:
                    print("Valor inválido. Insira um número inteiro.")
            if option3 == "1":
                while True:
                    ff = input("Insira o valor de f_fóton: ")
                    try:
                        ff = float(ff)
                        break
                    except:
                        print("Valor inválido. Insira um número real.")
                ef = calcula_ef_com_ff(ff)
            else:
                while True:
                    lambf = input("Insira o valor de lambda_fóton: ")
                    try:
                        lambf = float(lambf)
                        break
                    except:
                        print("Valor inválido. Insira um número real.")
                ff = c/lambf
                ef = calcula_ef_com_ff(ff)
            salto = calcula_diferenca_de_ef(ni, ef, "absorcao")
            print(salto)
            nf = calcula_nivel_com_ef(salto)
            print("\nnf = {:.3e}".format(nf))
        else:
            while True:
                nf = input("\nInsira o valor de nf: ")
                try:
                    nf = int(nf)
                    break
                except:
                    print("Valor inválido. Insira um número inteiro.")
            if option3 == "1":
                while True:
                    ff = input("Insira o valor de f_fóton: ")
                    try:
                        ff = float(ff)
                        break
                    except:
                        print("Valor inválido. Insira um número real.")
                ef = calcula_ef_com_ff(ff)
            else:
                while True:
                    lambf = input("Insira o valor de lambda_fóton: ")
                    try:
                        lambf = float(lambf)
                        break
                    except:
                        print("Valor inválido. Insira um número real.")
                ff = c/lambf
                ef = calcula_ef_com_ff(ff)
            salto = calcula_diferenca_de_ef(nf, ef, "emissao")
            ni = calcula_nivel_com_ef(salto)
            print("\nni = {:.3e}".format(ni))
