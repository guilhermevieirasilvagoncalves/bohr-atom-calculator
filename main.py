import numpy as np
from math import sqrt

""""
    @authors: Guilherme Vieira Silva Gonçalves, Kenzo Sugai, Daniel Alves Cunha, Bruna Pereira Paz
    @course: Ciência da Computação, 3th semester
    # ⌨️ with ❤️ using Visual Studio Code #
"""

while True:
    print(
    """
    Selecione uma opção de entrada: 
    [1] Entrada de n
    [2] Entrada do ni e nf
    [3] Calcular nf
    [4] Calcular ni
    [5] Encerrar programa
    """)

    #constantes
    e0 = 8.854 * pow(10, -12)
    a0 = 5.29 * pow(10,-11)
    h = 6.626 * pow(10, -34)
    H = 4.136 * pow(10, -15) 
    e = 1.602 * pow(10, -19)
    m = 9.109 * pow(10, -31)
    hc = 12.408 * pow(10, -7)
    c = 3 * pow(10, 8)

    D = int(input())
    if D == 1:
        n = float(input("Valor de n: "))
        r = pow(n , 2) * a0
        v = (2.187 * pow(10,6)) / n
        k = (13.6)/pow(n, 2)
        u = -27.2/pow(n, 2)
        l = (h / (m * v))
        et = -13.6 / pow(n, 2)
        print(
        """
        r = {0} m  
        v = {1} m/s
        λ = {2} m
        k = {3} eV   
        u = {4} eV
        En = {5} eV 
        """.format(np.format_float_scientific(r, precision = 2, exp_digits = 1), np.format_float_scientific(v, precision = 2, exp_digits = 1), np.format_float_scientific(l, precision = 2, exp_digits = 1), np.format_float_scientific(k, precision = 2, exp_digits = 1), np.format_float_scientific(u, precision = 2, exp_digits = 1), np.format_float_scientific(et, precision = 2, exp_digits = 1))
        )
    if D == 2:
        ni = int(input("Valor do n inicial: "))
        nf = int(input("Valor do n final: "))
        ei = -13.6/pow(ni, 2)
        ef = -13.6/pow(nf, 2)
        et = ei - ef
        l = hc/et 
        F = hc/(l*H)
        print(
        """
        E fóton = {0} eV
        λ fóton = {1} m
        F fóton = {2} Hz
        """.format(np.format_float_scientific(et, precision = 2, exp_digits = 1), np.format_float_scientific(l, precision = 2, exp_digits = 1), np.format_float_scientific(F, precision = 2, exp_digits = 1)))
    if D == 3:
        print(
        """
        Escolha uma entrada:
        
        [1] Comprimento de onda
        [2] Frequencia
        """)
        N = int(input())
        if N == 1:
            ni = int(input("Valor do n inicial: "))
            l = float(input("Valor do comprimento de onda: "))
            deltaE = H * c / l
            Ei = -13.6 / pow(ni,2)
            Ef = deltaE + Ei
            n = sqrt(-13.6 / Ef)
            print("""
                nf = {0} """.format(np.format_float_scientific(n, precision = 2, exp_digits = 1)))

        if N == 2:
            ni = int(input("Valor do n inicial: "))
            f = float(input("Valor da frequência: "))
            deltaE = H * f
            Ei = -13.6 / pow(ni,2)
            Ef = deltaE + Ei
            n = sqrt(-13.6 / Ef)
            print("""
                nf = {0} 
            """.format(np.format_float_scientific(n, precision = 2, exp_digits = 1)))
    
    if D == 4:
        print(
        """
        Escolha uma entrada:
        
        [1] Comprimento de onda
        [2] Frequencia
        """)
        N = int(input())
        if N == 1:
            nf = int(input("Valor do n final: "))
            f = float(input("Valor do comprimento de onda: "))
            deltaE = H * c / l
            Ef = -13.6 / pow(nf, 2)
            Ei = deltaE + Ef
            nprint = sqrt(-13.6 / Ei)
            print("""
                ni = {0} 
            """.format(np.format_float_scientific(nprint, precision = 2, exp_digits = 1)))
        if N == 2:
            nf = int(input("Valor do n final: "))
            f = float(input("Valor da frequência: "))
            deltaE = H * f
            Ef = -13.6 / pow(nf, 2)
            Ei = deltaE + Ef
            nprint = sqrt(-13.6 / Ei)
            print("""
                ni = {0} 
            """.format(np.format_float_scientific(nprint, precision = 2, exp_digits = 1)))
    if D == 5:
        break
