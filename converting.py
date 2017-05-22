#MIT License
#
#Copyright (c) LeOOnCOD

import sys
import socket
buscar = False
inicio = """
      _____________________________________________________________________________
     |    _____   ____  _   _ __      _ _____ _____  _______ _____ _   _  _____    |
     |   /  ___| / __ \| \ | |\ \    / |  ___|  __ \|__   __|_   _| \ | |/ ____|   |
     |   | |    | |  | |  \| | \ \  / /| |__ | |__) )  | |    | | |  \| | |  __    |
     |   | |    | |  | | . . |  \ \/ / |  __||  _  /   | |    | | |     | | |_ |   |
     |   | |___ | |__| | |\  |   \  /  | |___| | \ \   | |   _| |_| |\  | |__| |   |
     |   \_____| \____/|_| \_|    \/   |_____|_|  \_\  |_|  |_____|_| \_|\_____|   |
     |_____________________________________________________________________________|                                                                                                                                          
                                                  | CODADO POR: LeOOnCOD           |
                                                   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                                                                     
                                                                                    """
print(inicio)
print("|--------------------- TOMADA DE DECIÕES ---------------------|")
print("- DIGITE [1] PARA SABER SEU IP                                |")
print("- DIGITE [2] PARA CONVERTER DECIMAL PARA BINÁRIO              |")
print("- DIGITE [3] PARA CONVERTER BINÁRIO PARA DECIMAL              |")
print("- DIGITE [4] PARA AJUDA                                       |")
print("- DIGITE [5] PARA SAIR                                        |")
print("|-------------------------------------------------------------|")
while buscar == False:
    print(" ")
    menu = int(input("CONVERTING: Escolha a OPÇÃO: "))
    print(" ")

 #DAQUI PARA BAIXO, ACONTECERÁ A OPÇÃO ESCOLHIDA!
 #HERE DOWN, THE CHOICE OPTION WILL HAPPEN!

    if menu ==1:
        while True:
            checar = str(input("CONVERTING: Deseja pegar o IP Address? [S/N]: "))
            if checar == 'N' or checar == 'n':
                break
            else:
                if checar == 'S' or checar == 's':
                    print("Seu IP Address é: ",end="")
                    print(socket.gethostbyname(socket.gethostname()))
                    print(" ")
    if menu ==2:
        while True:
            print('CONVERTING: Digite "exit" para sair do CONVERSOR DECIMAL: ')
            dec = input("Coloque o número na forma DECIMAL: ")
            if dec == 'exit':
                break
            else:
                decimal = int(dec)
                print(decimal, "Para binário =", bin(decimal), "\n")
    if menu ==3:
        while True:
            print('CONVERTING: Digite "exit" para sair do CONVERSOR BINÁRIO: ')
            binary = input("Coloque o número na forma BINÁRIA: ")
            if binary == 'exit':
                break
            else:
                decimal = int(binary, 2)
                print(binary, "Para decimal =", decimal, "\n")
    if menu ==4:
        print("1 - O SCRIPT IRÁ PEGAR O IPV4 DO DISPOSITIVO")
        print("2 - O SCRIPT IRÁ CONVERTER O NÚMERO DECIMAL, PARA BINÁRIO")
        print("3 - O SCRIPT IRÁ CONVERTER O NÚMERO BINÁRIO, PARA DECIMAL")
        print('4 - O SCRIPT IRÁ DAR O "MANUAL" DE AJUDA')
        print("5 - O SCRIPT IRÁ ENCERRAR")
    if menu ==5:
        print("CONVERTING: STATUS - SAINDO...")
        sys.exit()
