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
R = 1.097E7
niveis = {1: -13.600000, 2: -3.400000, 3: -1.511111, 4: -0.850000, 5: -0.544000, 6: -0.377778, 7: -0.277551, 8: -0.212500, 9: -0.167901, 10: -0.136000, 11: -0.112397, 12: -0.094444, 13: -0.080473, 14: -0.069388, 15: -0.060444, 16: -0.053125, 17: -0.047059, 18: -0.041975, 19: -0.037673, 20: -0.034000, 21: -0.030839, 22: -0.028099, 23: -0.025709, 24: -0.023611, 25: -0.021760, 26: -0.020118, 27: -0.018656, 28: -0.017347, 29: -0.016171, 30: -0.015111, 31: -0.014152, 32: -0.013281, 33: -0.012489, 34: -0.011765, 35: -0.011102, 36: -0.010494, 37: -0.009934, 38: -0.009418, 39: -0.008941, 40: -0.008500, 41: -0.008090, 42: -0.007710, 43: -0.007355, 44: -0.007025, 45: -0.006716, 46: -0.006427, 47: -0.006157, 48: -0.005903, 49: -0.005664, 50: -0.005440, 51: -0.005229, 52: -0.005030, 53: -0.004842, 54: -0.004664, 55: -0.004496, 56: -0.004337, 57: -0.004186, 58: -0.004043, 59: -0.003907, 60: -0.003778, 61: -0.003655, 62: -0.003538, 63: -0.003427, 64: -0.003320, 65: -0.003219, 66: -0.003122, 67: -0.003030, 68: -0.002941, 69: -0.002857, 70: -0.002776, 71: -0.002698, 72: -0.002623, 73: -0.002552, 74: -0.002484, 75: -0.002418, 76: -0.002355, 77: -0.002294, 78: -0.002235, 79: -0.002179, 80: -0.002125, 81: -0.002073, 82: -0.002023, 83: -0.001974, 84: -0.001927, 85: -0.001882, 86: -0.001839, 87: -0.001797, 88: -0.001756, 89: -0.001717, 90: -0.001679, 91: -0.001642, 92: -0.001607, 93: -0.001572, 94: -0.001539, 95: -0.001507, 96: -0.001476, 97: -0.001445, 98: -0.001416, 99: -0.001388, 100: -0.001360}

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

def lambda_para_f(lamb):
    return c/lamb

def calcula_diferenca_de_ef(n, ef, option):
    if option == "+":
        return niveis[n] + ef
    elif option == "-":
        return niveis[n] - ef
    
def calcula_nivel_com_ef(ef):
    return sqrt(13.6/abs(ef))

def calcula_nivel_com_raio(r):
    return sqrt(r/(5.29E-11))

def calcula_nivel_com_velocidade(v):
    return (2.187E6/v)

def calcula_nivel_com_u(u):
    return sqrt(27.2/abs(u))

def calcula_serie(nf, ni):
    if ni != 0:
        return 1/(R*((1/nf**2)-(1/ni**2)))
    else:
        return 1/(R*(1/nf**2))

while True:

    print("Qual cálculo deseja realizar?\n")
    print("1) r{}, v{}, \u03BB, K{}, U{} e E{}".format(get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n")))
    print("2) E{}, f{}, \u03BB{}".format(get_sub("f"), get_sub("f"), get_sub("f")))
    print("3) n{} ou n{} (Absorção)".format(get_sub("f"), get_sub("i")))
    print("4) n{} ou n{} (Emissão)".format(get_sub("f"), get_sub("i")))
    print("5) Espectro do átomo de Hidrogênio")
    print("6) Verificar possibilidade de absorção")
    print("7) Calcular nível com r{}, v{}, \u03BB, K{}, U{} e E{}".format(get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n")))

    while True:
        option = input("\nInsira o número da opção desejada (ou sair): ")
        if option == "sair":
            exit(0)
        elif option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6" or option == "7":
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

    elif option == "3" or option == "4":
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
                salto = calcula_diferenca_de_ef(ni, ef, "+")
            elif option == "4":
                salto = calcula_diferenca_de_ef(ni, ef, "-")

            nf = calcula_nivel_com_ef(salto)
            print("\nE{} final = {:.3e} eV".format(get_sub("f"), salto))
            print("n{}".format(get_sub("f"), ni) + " = %.2f" % nf)
            print("n{}".format(get_sub("f"), ni) + " = %d\n" % round(nf))
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
            print("n{}".format(get_sub("i"), ni) + " = %d\n" % round(ni))

    elif option == "5":

        print("\nInsira o espectro no qual deseja calcular: ")
        print("1) Serie de Lyman (ultravioleta)")
        print("2) Serie de Balmer (luz visivel e ultravioleta)")
        print("3) Serie de Paschen (infravermelho)")
        print("4) Serie de Brackett (infravermelho)")
        print("5) Serie de Pfund (infravermelho)")
        
        while True:
            option4 = input("\nInsira o número da opção desejada (ou sair): ")
            if option4 == "sair":
                exit(0)
            elif option4 == "1" or option4 == "2" or option4 == "3" or option4 == "4" or option4 == "5":
                break
            else:
                print("Opção inválida! Digite novamente.\n")

        while True:
            ni = input("\nInsira o valor de n{}: ".format(get_sub("i")))
            try:
                ni = int(ni)
                break
            except:
                print("Valor inválido. Insira um número inteiro.")

        if option4 == "1":
            lambada = calcula_serie(1, ni)
        elif option4 == "2":
            lambada = calcula_serie(2, ni)
        elif option4 == "3":
            lambada = calcula_serie(3, ni)
        elif option4 == "4":
            lambada = calcula_serie(4, ni)
        elif option4 == "5":
            lambada = calcula_serie(5, ni)

        print("\n\u03BB{} = {:.3e} m".format(get_sub("f"), lambada))
        print("f{} = {:.3e} Hz\n".format(get_sub("f"), lambda_para_f(lambada)))
    
    elif option == "6":
        print("Você possui o valor de f{} ou \u03BB{}?".format(get_sub("f"), get_sub("f")))
        print("1) f{}".format(get_sub("f")))
        print("2) \u03BB{}".format(get_sub("f")))

        while True:
            option5 = input("\nInsira o número da opção desejada (ou sair): ")
            if option5 == "sair":
                exit(0)
            elif option5 == "1" or option5 == "2":
                break
            else:
                print("Opção inválida! Digite novamente.\n")

        if option5 == "1":
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
        salto = calcula_diferenca_de_ef(1, ef, "+")
        ni = calcula_nivel_com_ef(salto)
        print("n{}".format(get_sub("i"), ni) + " = %.2f" % ni)
        print("n{}".format(get_sub("i"), ni) + " = %d\n" % round(ni))
        if abs(ni - round(ni)) < 0.1:
            print("Sim, ocorreria absorção e salto quântico.\n")
        else:
            print("Não, não ocorreria absorção e salto quântico.\n")
    elif option == "7":
        print("Você possui o valor de r{}, v{}, \u03BB, K{} ou U{}?".format(get_sub("n"), get_sub("n"), get_sub("n"), get_sub("n")))
        print("1) r{}".format(get_sub("n")))
        print("2) v{}".format(get_sub("n")))
        print("3) \u03BB{}".format(get_sub("n")))
        print("4) K{}".format(get_sub("n")))
        print("5) U{}".format(get_sub("n")))

        option6 = input("\nInsira o número da opção desejada (ou sair): ")
        if option6 == "sair":
            exit(0)
        elif option6 == "1":
            while True:
                r = input("Insira o valor do raio de órbita (metros): ")
                try:
                    r = float(r)
                    break
                except:
                    print("Valor inválido. Insira um número real.")
            n = calcula_nivel_com_raio(r)
        elif option6 == "2":
            while True:
                v = input("Insira o valor da velocidade (metros/segundo): ")
                try:
                    v = float(v)
                    break
                except:
                    print("Valor inválido. Insira um número real.")
            n = calcula_nivel_com_velocidade(v)
        elif option6 == "3":
            while True:
                lamb = input("Insira o valor de \u03BB{} (metros): ".format(get_sub("n")))
                try:
                    lamb = float(lamb)
                    break
                except:
                    print("Valor inválido. Insira um número real.")
            ff = c/lamb
            ef = calcula_ef_com_ff(ff)
            n = calcula_nivel_com_ef(ef)
        elif option6 == "4":
            while True:
                ef = input("Insira o valor de K{} (eV): ".format(get_sub("f")))
                try:
                    ef = float(ef)
                    break
                except:
                    print("Valor inválido. Insira um número real.")
            n = calcula_nivel_com_ef(ef)
        elif option6 == "5":
            while True:
                u = input("Insira o valor de U{} (eV): ".format(get_sub("f")))
                try:
                    u = float(u)
                    break
                except:
                    print("Valor inválido. Insira um número real.")
            n = calcula_nivel_com_u(u)
        else:
            print("Opção inválida! Digite novamente.\n")
        print("\nn = %.2f" % n)
        print("n = %d\n" % round(n))