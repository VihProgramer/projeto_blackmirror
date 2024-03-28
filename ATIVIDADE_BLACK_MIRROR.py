# DESENVOLVA UM PROGRAMA EM QUE
# O USUÁRIO IRÁ INFORMAR UMA
# PERGUNTA (UTILIZANDO EXATAMENTE AS PERGUNTAS DO
# QUESTIONÁRIO ANTERIOR) E O
# SISTEMA DEVERÁ APRESENTAR A
# RESPOSTA A RESPOSTA.

# QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO

# QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?

# QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?

# COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?

# QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?

# QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?

# O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.

opcao = -1

while opcao != 0:
    opcao = int(input(f'''
    #############  O QUE DESEJA FAZER?  ##########
            [1] - UMA PERGUNTA
            [0] - SAIR
    ##############################################                            
    '''))
    if opcao == 1:
        pergunta = str(input('QUAL É A SUA PERGUNTA? ')).upper()

        if "NOME" in pergunta and "COMPLETO" in pergunta and "PROTAGONISTA" in pergunta and "EPISÓDIO" in pergunta:
            print(f'PERGUNTA: {pergunta}')
            print('RESPOSTA: JOAN TAIT')

        elif "DIRIGE" in pergunta and "VIDA" in pergunta and "JOAN" in pergunta and "TEMPO REAL" in pergunta and "SÉRIE" in pergunta and "TELEVISÃO" in pergunta:
            print(f'PERGUNTA: {pergunta}')
            print('RESPOSTA: É UM COMPUTADOR QUÂNTICO, QUE MAPEIA A VIDA DA JOAN E GERA A SÉRIE EM CGI')

        elif "NOME" in pergunta and "SERVIÇO" in pergunta and "STREAMING" in pergunta and "FICTÍCIO" in pergunta and "PARODIA" in pergunta and "NETFLIX" in pergunta and "EPISÓDIO" in pergunta:
            print(f'PERGUNTA: {pergunta}')
            print('RESPOSTA: O NOME DO STREAMING FICTÍCIO É STREAMBERRY')

        elif "DESCOBRE" in pergunta and "EXISTÊNCIA" in pergunta and "SÉRIE" in pergunta and "VIDA" in pergunta:
            print(f'PERGUNTA: {pergunta}')
            print('RESPOSTA: AO SENTAR NO SOFÁ PARA ASSISTIR SÉRIES COM O SEU NOIVO, ELA DESCOBRE QUE A PLATAFORMA DE STREAMING STREAMBERRY LANÇOU UMA SÉRIE QUE CONTA SUA VIDA EM TEMPO REAL')

        elif "REAÇÃO" in pergunta and "INICIAL" in pergunta and "JOAN" in pergunta and "DESCOBRIR" in pergunta and "SÉRIE" in pergunta and "RESPOSTA" in pergunta:
            print(f'PERGUNTA: {pergunta}')
            print('RESPOSTA: ELA FICOU HORRORIZADA AO PERCEBER QUE A SÉRIE MOSTRAVA SUA VIDA, E TENTOU NEGAR TUDO O QUE ACONTECIA NA SÉRIE')

        elif "TEMAS" in pergunta and "PRINCIPAIS" in pergunta and "EXPLORADOS" in pergunta and "EPISÓDIO" in pergunta and "BLACK MIRROR" in pergunta:
            print(f'PERGUNTA: {pergunta}')
            print('RESPOSTA: ALGUNS DOS TEMAS ABORDADOS NESTE EPISÓDIO DA SÉRIE INCLUEM: REALIDADE E ILUSÃO, CONTROLE E LIBERDADE, VIGILÂNCIA E PRIVACIDADE, MORALIDADE E ÉTICA, MEMÓRIA E TRAUMA.')

        elif "TERMINA" in pergunta and "MANEIRA TÍPICA" in pergunta and "SÉRIE" in pergunta and "BLACK MIRROR" in pergunta and "EXPLIQUE" in pergunta:
            print(f'PERGUNTA: {pergunta}')
            print('RESPOSTA: SIM, O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA BLACK MIRROR,\n COM UM FINAL AMBIGUAMENTE SOMBRIO E ABERTO À INTERPRETAÇÃO DO ESPECTADOR.\n JOAN CONSEGUE ESCAPAR DA SÉRIE,\n MAS A SUA LIBERDADE É LIMITADA E O SEU FUTURO É INCERTO.\n O EPISÓDIO DEIXA O ESPECTADOR REFLETIR SOBRE OS PERIGOS DA TECNOLOGIA,\n AS IMPLICAÇÕES ÉTICAS DO SEU USO E A POSSIBILIDADE DE REDENÇÃO PARA A PERSONAGEM.')

        else:
            print("PERGUNTA NÃO IDENTIFICADA")
    elif opcao == 0:
        print("ATÉ MAIS!!!")
    else:
        print("OPÇÃO INVÁLIDA, POR FAVOR TENTE NOVAMENTE.")