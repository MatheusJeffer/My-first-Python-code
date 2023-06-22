from Contatos.dat import Arquivos

list_de_contato = []

contatos = {}

while True:
    print('[1]Adicionar contatos.\n[2]Pesquisar contatos.\n[3]Apagar contatos.\n[4]Salvar contatos em arquivo txt.\n[5]Sair.')
    select = int(input('Selecione uma opção: '))
 

    if select_init == 1:
        add_contato = str(input('O nome do contato: '))
        add_numero = str(input('Digite o número do contato: '))

        contatos["Nome:"] = add_contato #Cria dois dicionarios, que vai receber o número e nome do contato.
        contatos["Telefone:"] = add_numero
        
        list_de_contato.append(contatos.copy())
        contatos.clear() #Após o processo, todos os dados do dicionário vai ser apagados.
        print('Feito!')

    if select == 2:
        nome_contato = str(input('Digite o nome do contato: '))
        
        for cont in list_de_contato: #Vai pegar todos os dados da lista.
            for  keys, item in cont.items():
               if nome_contato in cont["Nome:"]:
                     print(keys, item)

    if select == 3:
        print('=~'*20)
        print('         Lista de contatos')
        print('=~'*20)

        for pos, pessoas in enumerate(list_de_contato):
            for chaves, contato in pessoas.items():
              if contato == pessoas["Nome:"]:  
                  print(f'{pos: <10}{contato: <10}', end='')    
              else:
                  print(contato)
        
        del_contato = str(input('Selecione o contato que deseja apagar: '))

        try:
            del_int = int(del_contato)
            list_de_contato.pop(del_int)
    
        except:
            print('\033[0;31mERROR: Esse contato não existe.\033[0m')

    if select == 4:
        Arquivos.contatos_archive(list_de_contato)

    if select == 5:
        break
                    

