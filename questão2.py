from Contatos.dat import Arquivos


def line(text):
    tamanho = len(text)
    print('=~'*tamanho)
    print(f'        {text}')
    print('=~'*tamanho)



list_de_contato = []
contatos = {}


while True:
    print('[1]Adicionar contatos.\n[2]Pesquisar contatos.\n[3]Apagar contatos.\n[4]Salvar contatos em arquivo txt.\n[5]Sair.')
    select = str(input('Selecione uma opção: '))

    while select not in ('1','2','3','4','5') or select.isnumeric() == False:
         print('\033[0;31mERROR: digite uma opção válida.\033[0m')
         select = str(input('Selecione uma opção: '))
         
    select = int(select)

    if select == 1:
        print('=-'*18)
        add_contato = str(input('O nome do contato: '))
        add_numero = str(input('Digite o número do contato: '))

        contatos["Nome:"] = add_contato #Cria dois dicionarios, que vai receber o número e nome do contato.
        contatos["Telefone:"] = add_numero
        
        list_de_contato.append(contatos.copy())
        contatos.clear() #Após o processo, todos os dados do dicionário vai ser apagados.
        print('Feito!')
        print('=-'*18)
        
    if select == 2:
        line('Pesquisar contatos')
        nome_contato = str(input('Digite o nome do contato: '))
        contador = 0
        for cont in list_de_contato: #Vai pegar todos os dados da lista.
            for  keys, item in cont.items():
               if nome_contato in cont["Nome:"]: #Vai analizar se o nome digitado está no dicionário.
                     print(keys, item)
                     contador =+ 1

        if contador == 0:
            print('\033[0;31mO contato não existe\033[0m')
        print('=~'*18)

    if select == 3:
        line('Deletar contatos')
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
            print("\033[0;32mContato apagado com sucesso!\033[0m")
    
        except:
            print('\033[0;31mERROR: Esse contato não existe.\033[0m')

    if select == 4:
        Arquivos.contatos_archive(list_de_contato)
        print('\033[0;32mArquivo criado!\033[0m')

    if select == 5:
        break
                    

