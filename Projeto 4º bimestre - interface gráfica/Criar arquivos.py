from pandas import *

nah = 'a'

admins = {'Usuário': ['admin', 'Kaio', 'Vini'], 
          'Senha': ['1234', 'kaiokaio010203', 'vinigamerbr'], 
          'Email': [nah, nah, nah], 
          'Telefone': [nah, nah, nah], 
          'Data de Nascimento': [nah, nah, nah], 
          'Gênero': [nah, nah, nah]}

livros = {'Número': ['0', '1', '2'], 
          'Título': ['A Cabana', 'Percy Jackson', 'O Mágico de Oz'], 
          'Ano': [nah, nah, nah], 
          'Autor': [nah, nah, nah], 
          'Editora': [nah, nah, nah], 
          'Gênero': [nah, nah, nah],
          'Observação': [nah, nah, nah],
          'Data de cadastro': [nah, nah, nah],
          'Imagem': [nah, nah, nah],
          'Status': ['Disponível', 'Disponível', 'Disponível']}

membros = {'Usuário': ['Manu', 'Vitória', 'Pedro'], 
          'Senha': ['123', '321', 'pedrinn'], 
          'Multas': ['Não', 'Não', 'Não'],
          'Email': [nah, nah, nah], 
          'Telefone': [nah, nah, nah], 
          'Data de Nascimento': [nah, nah, nah], 
          'Gênero': [nah, nah, nah],
          'Endereço': [nah, nah, nah],
          'Status': ['Em dia', 'Em dia', 'Em dia']}

admins_df = DataFrame(admins)
livros_df = DataFrame(livros)
membros_df = DataFrame(membros)

admins_df.to_excel('registro admins.xlsx', index=False)
livros_df.to_excel('registro livros.xlsx', index=False)
membros_df.to_excel('registro membros.xlsx', index=False)

print(read_excel('registro admins.xlsx'))
print(read_excel('registro livros.xlsx'))
print(read_excel('registro membros.xlsx'))