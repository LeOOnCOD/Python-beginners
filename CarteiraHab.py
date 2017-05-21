#MIT License
#
#Copyright (c) 2017 LeOOnCOD
import sys
a = """                                        
    _____           _____  _______ _____ _ _____
   / ____|   /\    |  __ \|__   __|  ___|_|  __ \    /\ 
   | |      /  \   | |__) |  | |  | |_  | | |__) |  /  \ 
   | |     / /\ \  |  _  /   | |  |  _| | |  _  /  / /\ \ 
   | |___ / ____ \ | | \ \   | |  | |___| | | \ \ / ____ \ 
   \_____/_/    \_/|_|  \_\  |_|  |_____|_|_|  \_/_/    \_\ 
   
        _______
     __/___|___\___     ___________________________
    |< |º  |º  |  >|   | PROGRAMADO POR: LeOOnCOD  |
    .-(@)------(@)-|   | DATA: 20/05/2017          |
   
   SCRIPT - CarteiraHAB: STATUS - Iniciando...
   """
buscar = False
print(a)
print(" ")
print('----------------------------- DADOS NECESSÁRIOS -----------------------------')
print(" ")
nome_completo = str(input("CarteiraHAB: Digite seu NOME e SOBRENOME: "))
idade = int(input("CarteiraHAB: Informe sua IDADE (aa): "))
print(" ")
print('----------------------------- TOMADA DE DECISÕES ----------------------------')
print(" ")
print('1 - PARA CONSULTAR AS SEGUINTES CARTEIRAS [A] ou [B]')
print('2 - PARA CONSULTAR AS SEGUINTES CARTEIRAS [C, D e E]')
print('3 - PARA SAIR DO SCRIPT')
print(" ")
while buscar == False:
    print(" ")
    menu = int(input('CarteiraHAB: Informe qual será sua DECISÃO: '))
    print(" ")

    if menu ==1:
        print('- Carteira [A]  |')
        print('- Carteira [B]  |')
        print(" ")
        cartAB = str(input('CarteiraHAB: Informe qual será CONSULTADA: '))
        if  cartAB == 'A' or cartAB == 'a':
            print(" ")
            print("-------------------- PERGUNTAS --------------------")
            print('Ex.: Motocicletas, Ciclomotor, Motoneta ou Triciclo.')
            print(" ")
            print("DICA: EQUIPAMENTO DE PROTEÇÃO")
            respA1 = str(input("PRIMEIRA QUESTÃO: Em uma moto utiliza-se? "))
            if respA1 == 'CAPACETE' or respA1 == 'Capacete' or respA1 == 'capacete':
                print('CarteiraHAB: Você acertou a PRIMEIRA QUESTÃO!')
                print(" ")
            else:
                print("CarteiraHAB: Você errou a PRIMEIRA QUESTÃO!")
                print(" ")
            respA2 = str(input('SEGUNDA QUESTÃO: Quantas rodas possui a CATEGORIA [A]? '))
            if respA2 == '3' or respA2 == 'tres' or respA2 == 'três':
                print('CarteiraHAB: Você acertou a SEGUNDA QUESTÃO!')
                print(" ")
            else:
                print('CarteiraHAB: Você errou a SEGUNDA QUESTÃO!')
                print(" ")
            if idade >= 18:
                print('CarteiraHAB: Parábens',nome_completo+" você está APTO para a CARTEIRA [A]")
            else:
                print('CarteiraHAB: Desculpe',nome_completo+" você é MENOR DE IDADE")
        if cartAB == 'B' or cartAB == 'b':
            print(" ")
            print("-------------------- PERGUNTAS --------------------")
            print("Ex.: Automóvel, caminhonete, camioneta, utilitário.")
            print(" ")
            print("DICA: EQUIPAMENTO DE PROTEÇÃO")
            respB1 = str(input("PRIMEIRA QUESTÃO: No carro utiliza-se? "))
            if respB1 == "Cinto de segurança" or respB1 == "cinto de segurança":
                print('CarteiraHAB: Você acertou a PRIMEIRA QUESTÃO!')
                print(" ")
            else:
                print('CarteiraHAB: Você errou a PRIMEIRA QUESTÃO!')
                print(" ")
            respB2 = str(input('SEGUNDA QUESTÃO: Quantas rodas possuí um carro? '))
            if respB2 == '4' or respB2 == 'quatro' or respB2 == 'Quatro':
                print('CarteiraHAB: Você acertou a SEGUNDA QUESTÃO!')
                print(" ")
            else:
                print('CarteiraHAB: Você errou a SEGUNDA QUESTÃO!')
                print(" ")
            if idade >= 18:
                print('CarteiraHAB: Parábens', nome_completo + " você está APTO para a CARTEIRA [B]")
            else:
                print('CarteiraHAB: Desculpe', nome_completo + " você é MENOR DE IDADE")
    if menu ==2:
        print('- Carteira [C]  |')
        print('- Carteira [D]  |')
        print('- Carteira [E]  |')
        print(" ")
        cde = str(input('CarteiraHAB: Informe qual será CONSULTADA: '))
        if  cde == 'C' or cde == 'c':
            print(" ")
            print("-------------------- PERGUNTAS --------------------")
            print('Ex.: Caminhão.')
            print(" ")
            print("DICA: CAMINHÃO")
            respC1 = str(input('PRIMEIRA QUESTÃO: Quantas rodas UM CAMINHÃO tem? '))
            if respC1 == '6' or respC1 == 'seis' or respC1 == 'Seis':
                print("CarteiraHAB: Você acertou a PRIMEIRA QUESTÃO!")
                print(" ")
            else:
                print("CarteiraHAB: Você errou a PRIMEIRA QUESTÃO!")
                print(" ")
            respC2 = str(input('SEGUNDA QUESTÃO: Quantos CONJUNTOS de RODAS UM CAMINHÃO tem? '))
            if respC2 == '4' or respC2 == 'quatro' or respC2 == 'Quatro':
                print('CarteiraHAB: Você acertou a SEGUNDA QUESTÃO!')
                print(" ")
            else:
                print('CarteiraHAB: Você errou a SEGUNDA QUESTÃO!')
                print(" ")
            if idade >= 22:
                print('CarteiraHAB: Parábens', nome_completo + " você está APTO para a CARTEIRA [C]")
            else:
                print('CarteiraHAB: Desculpe', nome_completo + " você é MENOR DE IDADE para as CARTEIRAS [C, D e E]")
        if cde == 'D' or cde == 'd':
            print(" ")
            print("-------------------- PERGUNTAS --------------------")
            print('Ex.: Microônibus, Ônibus.')
            print(" ")
            print('DICA: MICROÔNIBUS')
            respD1 = str(input('PRIMEIRA QUESTÃO: Quantas RODAS possuí o MICROÔNIBUS? '))
            if respD1 == '6' or respD1 == 'seis' or respD1 == 'Seis':
                print('CarteiraHAB: Você acertou a PRIMEIRA QUESTÃO!')
                print(" ")
            else:
                print("CarteiraHAB: Você errou a PRIMEIRA QUESTÃO!")
                print(" ")
            respD2 = str(input('SEGUNDA QUESTÃO: Quantos CONJUNTOS de RODAS o MICROÔNIBUS possuí? '))
            if respD2 == '2' or respD2 == 'dois' or respD2 == 'Dois':
                print('CarteiraHAB: Você acertou a SEGUNDA QUESTÃO!')
                print(" ")
            else:
                print('CarteiraHAB: Você errou a SEGUNDA QUESTÃO!')
                print(" ")
            if idade >= 22:
                print('CarteiraHAB: Parábens', nome_completo + " você está APTO para a CARTEIRA [D]")
            else:
                print('CarteiraHAB: Desculpe', nome_completo + " você é MENOR DE IDADE para as CARTEIRAS [C, D e E]")
        if cde == 'E' or cde == 'e':
            print(" ")
            print("-------------------- PERGUNTAS --------------------")
            print('Ex.: Veículo com dois reboques acoplados.')
            print(" ")
            print('DICA: ACOPLAMENTOS')
            respE1 = str(input('PRIMEIRA QUESTÃO: Quantas RODAS possuí um veículo acoplado com 2(DOIS) REBOQUES? '))
            if respE1 == '18' or respE1 == 'dezoito' or respE1 == 'Dezoito':
                print("CarteiraHAB: Você acertou a PRIMEIRA QUESTÃO!")
                print(" ")
            else:
                print("CarteiraHAB: Você errou a PRIMEIRA QUESTÃO!")
                print(" ")
            respE2 = str(input('SEGUNDA QUESTÃO: Quantos CONJUNTOS de RODAS possuí um veículo acoplado com 2(DOIS) REBOQUES? '))
            if respE2 == '8' or respE2 == 'oito' or respE2 == 'Oito':
                print("CarteiraHAB: Você acertou a SEGUNDA QUESTÃO!")
                print(" ")
            else:
                print("CarteiraHAB: Você errou a SEGUNDA QUESTÃO!")
                print(" ")
            if idade >= 22:
                print('CarteiraHAB: Parábens', nome_completo + " você está APTO para a CARTEIRA [E]")
            else:
                print('CarteiraHAB: Desculpe', nome_completo + " você é MENOR DE IDADE para as CARTEIRAS [C, D e E]")
    if menu ==3:
     sys.exit(0)