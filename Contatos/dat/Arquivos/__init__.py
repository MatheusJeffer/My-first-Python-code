def contatos_archive(lista):
  with open('Contatos.txt', 'a') as archive:
      archive.write('=~=~=~=~=~=~=~=~~=~=~=~=~=Lista de contato=~=~=~=~=~=~=~=~~=~=~=~=~=\n')
      for contatos in lista:
          for keys, item in contatos.items():
              if item == contatos["Nome:"]:
                  archive.write(F'Contato:{item}\n')
              else:
                   archive.write(f'Telefone:{item}\n')
                   archive.write('=~~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~~=~=~=~=~=\n')


