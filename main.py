print("NL 2 - CF3121: Tópicos de Óptica e Física Moderna\n")

def get_sub(x):
    normal = "abcdefghijklmnopqrstuvwxyz"
    sub_s = "ᴀʙᴄᴅᴇғɢʜᵢᴊᴋʟᴍₙᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

# Exibe o nome dos integrantes do grupo

print("Integrantes do grupo: \n")

print("Gustavo Garcia Bagio - RA: 24.122.012-8")
print("Ruan Pastrelo Turola - RA: 24.122.050-8\n")

print("Átomo de Bohr e Quantização\n")

print("O programa consegue calcular os seguintes valores: r{} (raio de órbita do elétron), v{} (velocidade do elétron na órbita), \u03BB{} (comprimento de onda de De Broglie do elétron no nível n), K{} (energia cinética no modelo de Bohr), U{} (energia potencial no modelo de Bohr), E{} (energia total no modelo de Bohr), E{} (energia do fóton emitido ou absorvido), \u03BB{} (comprimento de onda do fóton emitido ou absorvido), f{} (frequência do fóton emitido ou absorvido), n{} (nível quântico inicial de um fóton pelo átomo de H), n{} (nível quântico final de um fóton pelo átomo de H).\n".format(get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n"), get_sub("t"), get_sub("f"), get_sub("f"), get_sub("f"), get_sub("i"), get_sub("f")))

print("Conceitos básicos:")
print("- Emissão: Um átomo cai de um nível inicial i para um nível final f de energia inferior emitindo um fóton com energia igual à diferença entre os níveis i e f.")
print("- Absorção: Um átomo é elevado de um nível inicial i para um nível final f de energia, absorvendo um fóton com uma energia igual à diferença entre os níveis f e i.\n")

print("Conceitos Importantes:")
print("- Fóton, níveis de energia de um átomo, quantização, emissão e absorção de fótons, ionização, transição entre níveis, excitação e decaimento, salto quântico.")
print("- Energia de Ionização: => Menor energia necessária para arrancar o elétron do átomo.")
print("- A energia do átomo aumenta ou diminui ao absorver ou emitir um fóton.\n")


print("O programa não faz conversão de unidades!\n")

from math import *

E0 = 8.85E-12
m = 9.11E-31
e = 1.602E-19
h = 6.626E-34
h2 = 4.136E-15
c = 3E8
niveis = {1: -13.6, 2: -3.4, 3: -1.51, 4: -0.85, 5: -0.54, 6: -0.38, 7: -0.28, 8: -0.22, 9: -0.18, 10: -0.15, 11: -0.13, 12: -0.11, 13: -0.1}

def calcula_raio(n):
    return E0 * (((n ** 2) * (h ** 2)) / (pi * m * (e ** 2)))

def calcula_velocidade(n):
    return (1 / E0) * (e ** 2 / (2 * n * h))

def calcula_lambda(v):
    return h / (m * v)

def calcula_energia_cinetica(n):
    return ((m * e ** 4) / (8 * (n ** 2) * (h ** 2) * (E0 ** 2)))/1.602E-19

def calcula_energia_potencial(n):
    return -(1 / (E0 ** 2)) * ((m * (e ** 4)) / (4 * (n ** 2) * (h ** 2)))/1.602E-19

def calcula_energia_total(kn, un):
    return kn + un

def calcula_ef_com_niveis(ni, nf):
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
    if option == "+":
        return niveis[n] + ef
    elif option == "-":
        return niveis[n] - ef
    
def calcula_nivel_com_ef(ef):
    return sqrt(13.6/abs(ef))
       

while True:

    print("Qual cálculo deseja realizar?\n")
    print("1) r{}, v{}, \u03BB, K{}, U{} e E{}".format(get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n")))
    print("2) E{}, f{}, \u03BB{}".format(get_sub("f"), get_sub("f"), get_sub("f")))
    print("3) n{} ou n{} (Absorção)".format(get_sub("f"), get_sub("i")))
    print("4) n{} ou n{} (Emissão)".format(get_sub("f"), get_sub("i")))

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

        print("\nr{} = {:.3e} m".format(get_sub("n"), rn))
        print("v{} = {:.3e} m/s".format(get_sub("n"), vn))
        print("\u03BB = {:.3e} m".format(lambn))
        print("K{} = {:.3e} eV".format(get_sub("n"), kn))
        print("U{} = {:.3e} eV".format(get_sub("n"), un))
        print("E{} = {:.3e} eV\n".format(get_sub("t"), et))

    elif option == "2":
        while True:
            ni = input("Insira o valor de n{}: ".format(get_sub("i")))
            try:
                ni = int(ni)
                break
            except:
                print("Valor inválido. Insira um número inteiro.")
        while True:
            nf = input("Insira o valor de n{}: ".format(get_sub("f")))
            try:
                nf = int(nf)
                break
            except:
                print("Valor inválido. Insira um número inteiro.")

        ef = calcula_ef_com_niveis(ni, nf)
        lambf = calcula_lambda_foton(ef)
        ff = calcula_f_foton(ef)

        print("\nE{} = {:.3e} eV".format(get_sub("f"), ef))
        print("\u03BB{} = {:.3e} m".format(get_sub("f"), lambf))
        print("f{} = {:.3e} Hz\n".format(get_sub("f"), ff))

    elif option == "3" or "4":
        print("Você deseja calcular n{} ou n{}?".format(get_sub("f"), get_sub("i")))
        print("1) n{}".format(get_sub("f")))
        print("2) n{}".format(get_sub("i")))

        while True:
            option2 = input("\nInsira o número da opção desejada (ou sair): ")
            if option2 == "sair":
                exit(0)
            elif option2 == "1" or option2 == "2":
                break
            else:
                print("Opção inválida! Digite novamente.\n")
        
        print("Você possui o valor de f{} ou \u03BB{}?".format(get_sub("f"), get_sub("f")))
        print("1) f{}".format(get_sub("f")))
        print("2) \u03BB{}".format(get_sub("f")))

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
                ni = input("\nInsira o valor de n{}: ".format(get_sub("i")))
                try:
                    ni = int(ni)
                    break
                except:
                    print("Valor inválido. Insira um número inteiro.")
            if option3 == "1":
                while True:
                    ff = input("Insira o valor de f{}: ".format(get_sub("f")))
                    try:
                        ff = float(ff)
                        break
                    except:
                        print("Valor inválido. Insira um número real.")
                ef = calcula_ef_com_ff(ff)
            else:
                while True:
                    lambf = input("Insira o valor de \u03BB{}: ".format(get_sub("f")))
                    try:
                        lambf = float(lambf)
                        break
                    except:
                        print("Valor inválido. Insira um número real.")
                ff = c/lambf
                ef = calcula_ef_com_ff(ff)

            if option == "3":
                salto = calcula_diferenca_de_ef(ni, ef, "+")
            elif option == "4":
                salto = calcula_diferenca_de_ef(ni, ef, "-")

            nf = calcula_nivel_com_ef(salto)
            print("\nE{} final = {:.3e} eV".format(get_sub("f"), salto))
            print("n{}".format(get_sub("f"), ni) + " = %.2f" % nf)
            print("n{}".format(get_sub("f"), ni) + " = %d\n" % round(nf, 1))
        else:
            while True:
                nf = input("\nInsira o valor de n{}: ".format(get_sub("f")))
                try:
                    nf = int(nf)
                    break
                except:
                    print("Valor inválido. Insira um número inteiro.")

            if option3 == "1":
                while True:
                    ff = input("Insira o valor de f{} (Hz): ".format(get_sub("f")))
                    try:
                        ff = float(ff)
                        break
                    except:
                        print("Valor inválido. Insira um número real.")
                ef = calcula_ef_com_ff(ff)
            else:
                while True:
                    lambf = input("Insira o valor de \u03BB{} (metros): ".format(get_sub("f")))
                    try:
                        lambf = float(lambf)
                        break
                    except:
                        print("Valor inválido. Insira um número real.")
                ff = c/lambf
                ef = calcula_ef_com_ff(ff)

            if option == "3":
                salto = calcula_diferenca_de_ef(nf, ef, "-")
            elif option == "4":
                salto = calcula_diferenca_de_ef(nf, ef, "+")

            ni = calcula_nivel_com_ef(salto)
            print("\nE{} inicial = {:.3e} eV".format(get_sub("f"), salto))
            print("n{}".format(get_sub("i"), ni) + " = %.2f" % ni)
            print("n{}".format(get_sub("i"), ni) + " = %d\n" % round(ni, 1))