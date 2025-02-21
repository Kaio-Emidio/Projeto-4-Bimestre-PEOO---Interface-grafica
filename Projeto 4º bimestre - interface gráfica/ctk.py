# Disciplina: PEOO
# Turma: INFO2V 
# Componentes:
# Kaio Emidio
# Maria Vitória
# Emanuelle Alves
# Vinícius Gabriel

from customtkinter import *
import pandas as pd
from tkinter import messagebox
from PIL import Image
from datetime import date

# Configuração de aparência
set_appearance_mode('dark')

# Definir o caminho dos arquivos e outras variáveis
admins = "registro admins.xlsx"
membros = "registro membros.xlsx"
livros = "registro livros.xlsx"

logo = "heheORetorno.png"

cor1 = '#e1cbb1' #fundo
cor2 = '#976f47' #botões
cor3 = '#7b5836' #botões
cor4 = '#422a14' #texto
cor5 = '#4b3828' #detalhes/borda

# tentar abrir as planilhas, caso dê erro, ele executa um aviso.
try:
    admins_df = pd.read_excel(admins)
    membros_df = pd.read_excel(membros)
    livros_df = pd.read_excel(livros)
except:
    messagebox.showerror(title='Banco de Dados', message='Falha ao abrir os bancos de dados')
    quit()

def centralizar(tela:CTk, largura:int, altura:int):
    largura_tela = tela.winfo_screenwidth()
    altura_tela = tela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2) - 50
    tela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
    tela.resizable(False, False)

def mudar_resul(resul:CTkLabel, texto:str, tela:CTk):
    resul.configure(text=texto, text_color="red")
    tela.after(3000, lambda: resul.configure(text=""))

def abrir_login():
    global resultado_login, entrada_senha, entrada_usuario, login
    login = CTk(cor1)
    login.title("Login")
    centralizar(login, 500, 650)

    img_logo = CTkImage(Image.open(logo), size=(200,200))
    label_logo = CTkLabel(login, image=img_logo, text="")
    label_logo.pack(pady=10)

    texto_login = CTkLabel(login, text_color=cor4, text='Login', font=('Courier', 32, 'bold'), anchor='s')
    texto_login.pack()

    texto_login2 = CTkLabel(login, text_color=cor4, text='Acesse à Biblioteca de Alexandria:', font=('Courier', 16, 'bold'))
    texto_login2.pack(pady=20)

    texto_usuario = CTkLabel(login, text_color=cor4, text='Usuário:', font=('Courier', 12, 'bold'), width=400, anchor='w')
    texto_usuario.pack(pady=5)

    entrada_usuario = CTkEntry(login, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu usuário', width=400)
    entrada_usuario.pack()

    texto_senha = CTkLabel(login, text_color=cor4, text='Senha:', font=('Courier', 12, 'bold'), width=400, anchor='w')
    texto_senha.pack(pady=5)

    entrada_senha = CTkEntry(login, fg_color=cor5, text_color=cor1, placeholder_text='Digite sua senha', show='*', width=400)
    entrada_senha.pack()

    botão_esqueceu_senha = CTkButton(login, text_color=cor4, hover_color=cor3, corner_radius=32, text='Esqueceu ou deseja alterar sua senha?', font=('Courier', 12, 'bold'), command=abrir_alterar_senha_admins, fg_color="transparent", width=400, anchor='e')
    botão_esqueceu_senha.pack(pady=5)

    botao_login = CTkButton(login, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Login', font=('Courier', 12, 'bold'), command=validar_login_admin)
    botao_login.pack()

    resultado_login = CTkLabel(login,text='', font=('Courier', 12, 'bold'))
    resultado_login.pack()

    botao_cadastro = CTkButton(login, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Criar conta', font=('Courier', 12, 'bold'), command=abrir_cadastro_admins)
    botao_cadastro.pack(pady=10)

    login.mainloop()

def abrir_cadastro_admins():
    login.destroy()
    cadastro_admins = CTk(cor1)
    cadastro_admins.title("Cadastro de Administadores")
    centralizar(cadastro_admins, 600, 675)

    texto_cadastro = CTkLabel(cadastro_admins, text_color=cor4, text='Cadastro de\nAdministadores', font=('Courier', 32, 'bold'), anchor='s')
    texto_cadastro.pack(pady=20)

    texto_cadastro2 = CTkLabel(cadastro_admins, text_color=cor4, text='Preencha as informações abaixo para criar seu perfil:', font=('Courier', 16, 'bold'))
    texto_cadastro2.pack()

    texto_usuario = CTkLabel(cadastro_admins, text_color=cor4, text='Usuário:', font=('Courier', 12, 'bold'), width=450, anchor='w')
    texto_usuario.pack(pady=5)
    entrada_usuario = CTkEntry(cadastro_admins, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu Usuário', width=450)
    entrada_usuario.pack()

    texto_email = CTkLabel(cadastro_admins, text_color=cor4, text='Email:', font=('Courier', 12, 'bold'), width=450, anchor='w')
    texto_email.pack(pady=5)
    entrada_email = CTkEntry(cadastro_admins, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu Email', width=450)
    entrada_email.pack()

    texto_confirm_email = CTkLabel(cadastro_admins, text_color=cor4, text='Confirme seu Email:', font=('Courier', 12, 'bold'), width=450, anchor='w')
    texto_confirm_email.pack(pady=5)
    entrada_confirm_email = CTkEntry(cadastro_admins, fg_color=cor5, text_color=cor1, placeholder_text='Confirme seu Email', width=450)
    entrada_confirm_email.pack()

    frame_TDG = CTkFrame(cadastro_admins, fg_color=cor1)

    texto_telefone = CTkLabel(frame_TDG, text_color=cor4, text='Telefone:', font=('Courier', 12, 'bold'), anchor='w', width=143)
    texto_telefone.grid(row=0, column=0, padx=5)
    entrada_telefone = CTkEntry(frame_TDG, fg_color=cor5, text_color=cor1, placeholder_text='(99) 99999-9999', width=143)
    entrada_telefone.grid(row=1, column=0, padx=5)

    texto_nascimento = CTkLabel(frame_TDG, text_color=cor4, text='Data de Nascimento:', font=('Courier', 12, 'bold'), anchor='w', width=143)
    texto_nascimento.grid(row=0, column=1, padx=5)
    entrada_nascimento = CTkEntry(frame_TDG, fg_color=cor5, text_color=cor1, placeholder_text='dd/mm/aaaa', width=143)
    entrada_nascimento.grid(row=1, column=1, padx=5)

    texto_genero = CTkLabel(frame_TDG, text_color=cor4, text='Gênero:', font=('Courier', 12, 'bold'), anchor='w', width=143)
    texto_genero.grid(row=0, column=2, padx=5)
    entrada_genero = CTkEntry(frame_TDG, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu Gênero', width=143)
    entrada_genero.grid(row=1, column=2, padx=5)

    frame_TDG.pack()

    texto_senha = CTkLabel(cadastro_admins, text_color=cor4, text='Senha:', font=('Courier', 12, 'bold'), width=450, anchor='w')
    texto_senha.pack(pady=5)
    entrada_senha = CTkEntry(cadastro_admins, fg_color=cor5, text_color=cor1, placeholder_text='Digite sua senha', show='*', width=450)
    entrada_senha.pack()

    texto_confirm_senha = CTkLabel(cadastro_admins, text_color=cor4, text='Confirmar Senha:', font=('Courier', 12, 'bold'), width=450, anchor='w')
    texto_confirm_senha.pack(pady=5)
    entrada_confirm_senha = CTkEntry(cadastro_admins, fg_color=cor5, text_color=cor1, placeholder_text='Confirme sua Senha', show='*', width=450)
    entrada_confirm_senha.pack()

    texto_result_cad = CTkLabel(cadastro_admins, text="", justify="left", font=('Courier', 12, 'bold'))
    texto_result_cad.pack(pady=5)

    def voltar():
        cadastro_admins.destroy()
        abrir_login()

    def ver_cadastro_admin():
        usuario, senha, conf_senha, email, conf_email, telefone, nascimento, genero = entrada_usuario.get(), entrada_senha.get(), entrada_confirm_senha.get(), entrada_email.get(), entrada_confirm_email.get(), entrada_telefone.get(), entrada_nascimento.get(), entrada_genero.get()

        if any(var == '' for var in [usuario, senha, conf_senha, email, conf_email, telefone, nascimento, genero]):
            mudar_resul(texto_result_cad, 'Preencha todos os campos!', cadastro_admins)
        else:
            if senha != conf_senha:
                mudar_resul(texto_result_cad, 'As Senhas não coincidem, tente novamente!', cadastro_admins)
            elif email != conf_email:
                mudar_resul(texto_result_cad, 'Os Emails não coincidem, tente novamete!', cadastro_admins)
            elif usuario in admins_df["Usuário"].astype(str).values:
                mudar_resul(texto_result_cad, 'Esse usuário já existe, faça login. \nCaso esqueceu a senha, recupere-a.', cadastro_admins)
            else:
                add = {'Usuário':usuario, 
                       'Senha':senha, 
                       'Email':email, 
                       'Telefone':telefone, 
                       'Data de Nascimento':nascimento,
                       'Gênero':genero}

                admins_df.loc[len(admins_df)] = add
                admins_df.to_excel(admins, index=False)
                messagebox.showinfo('Conta Criada.', 'Usuário cadastradado com sucesso!')
    
    botao_cadastro = CTkButton(cadastro_admins, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Confirmar Cadastro', font=('Courier', 12, 'bold'), command=ver_cadastro_admin)
    botao_cadastro.pack(pady=10)

    botao_voltar = CTkButton(cadastro_admins, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Voltar', font=('Courier', 12, 'bold'), command=voltar)
    botao_voltar.pack(pady=10)

    cadastro_admins.mainloop()

def abrir_alterar_senha_admins():
    login.destroy()
    alterar_senha = CTk(cor1)
    alterar_senha.title("Alterar Senha")
    centralizar(alterar_senha, 600, 450)

    texto_alterar_senha = CTkLabel(alterar_senha, text_color=cor4, text='Alterar Senha', font=('Courier', 32, 'bold'), anchor='s')
    texto_alterar_senha.pack(pady=20)

    texto_usuario = CTkLabel(alterar_senha, text_color=cor4, text='Usuário:', font=('Courier', 12, 'bold'), width=400, anchor='w')
    texto_usuario.pack(pady=5)

    entrada_usuario = CTkEntry(alterar_senha, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu usuário', width=400)
    entrada_usuario.pack()

    texto_senha_nov = CTkLabel(alterar_senha, text_color=cor4, text='Senha Nova:', font=('Courier', 12, 'bold'), width=400, anchor='w')
    texto_senha_nov.pack(pady=5)

    entrada_senha_nov = CTkEntry(alterar_senha, fg_color=cor5, text_color=cor1, placeholder_text='Digite sua nova senha', show='*', width=400)
    entrada_senha_nov.pack()

    texto_senha_nov_conf = CTkLabel(alterar_senha, text_color=cor4, text='Confirmar Senha:', font=('Courier', 12, 'bold'), width=400, anchor='w')
    texto_senha_nov_conf.pack(pady=5)

    entrada_senha_nov_conf = CTkEntry(alterar_senha, fg_color=cor5, text_color=cor1, placeholder_text='Confirme sua senha', show='*', width=400)
    entrada_senha_nov_conf.pack()

    texto_result_nvs = CTkLabel(alterar_senha, text="", justify="left", font=('Courier', 12, 'bold'))
    texto_result_nvs.pack(pady=5)

    def voltar():
        alterar_senha.destroy()
        abrir_login()
    
    def mudar_senha():
        usuario = entrada_usuario.get()
        senha = entrada_senha_nov.get()
        confsenha = entrada_senha_nov_conf.get()

        if not any(var == '' for var in [usuario, senha, confsenha]):
            if usuario in admins_df["Usuário"].astype(str).values:
                if senha == confsenha:
                    admins_df.loc[admins_df['Usuário'] == usuario, 'Senha'] = senha
                    admins_df.to_excel(admins)
                    messagebox.showinfo('Senha alterada', 'Senha alterada com sucesso!')
                else:
                    mudar_resul(texto_result_nvs, 'As senhas não coincidem!', alterar_senha)
            else:
                mudar_resul(texto_result_nvs, 'Usuário não encontrado!', alterar_senha)
        else:
            mudar_resul(texto_result_nvs, 'Preencha todos os campos!', alterar_senha)

    botao_alterar_senha = CTkButton(alterar_senha, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Alterar Senha', font=('Courier', 12, 'bold'), command=mudar_senha)
    botao_alterar_senha.pack(pady=10)

    botao_voltar = CTkButton(alterar_senha, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Voltar', font=('Courier', 12, 'bold'), command=voltar)
    botao_voltar.pack(pady=10)

    alterar_senha.mainloop()

def validar_login_admin():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == '' or senha == '':
        mudar_resul(resultado_login, 'Preencha ambos dos campos!', login)
    elif usuario in admins_df["Usuário"].astype(str).values and senha in admins_df.loc[admins_df['Usuário'] == usuario, 'Senha'].astype(str).values:
        login.destroy()
        abrir_principal()
    else:
        mudar_resul(resultado_login, 'Usuário ou senha incorretos!', login)

def abrir_principal():
    global principal
    principal = CTk(cor1)
    principal.title("Biblioteca de Alexandria")
    centralizar(principal, 800, 600)
    
    img_logo = CTkImage(Image.open(logo), size=(200,200))
    label_logo = CTkLabel(principal, image=img_logo, text="")  # display image with a CTkLabel
    label_logo.pack(pady=50)

    frame_botoes = CTkFrame(principal, border_color=cor5, border_width=3, fg_color=cor1)
    frame_botoes.pack(pady=10)

    botao_registro_livro = CTkButton(frame_botoes, command=abrir_registro_livros, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Registrar Livro', font=('Courier', 12, 'bold'))
    botao_registro_livro.grid(row=0, column=0, padx=10, pady=10)
    
    botao_emprestimo_devolucao = CTkButton(frame_botoes, command=pre_abrir_ed, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Gerenciar Empréstimos\ne Devoluções', font=('Courier', 12, 'bold'))
    botao_emprestimo_devolucao.grid(row=0, column=1, padx=10, pady=10)

    botao_gerenciar_multas = CTkButton(frame_botoes, command=abrir_gerenciar_multas, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Gerenciar Multas', font=('Courier', 12, 'bold')) 
    botao_gerenciar_multas.grid(row=0, column=2, padx=10, pady=10)

    botao_logoff = CTkButton(frame_botoes, command=logoff, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Logoff', font=('Courier', 12, 'bold'))
    botao_logoff.grid(row=1, column=0, padx=10, pady=10)

    botao_sair = CTkButton(frame_botoes, command=lambda:principal.destroy(), text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Sair', font=('Courier', 12, 'bold'))
    botao_sair.grid(row=1, column=1, padx=10, pady=10)

    principal.mainloop()

def logoff():
    principal.destroy()
    abrir_login()

def abrir_cadastro_membros():
    emprestimo_devolucao.destroy()
    cadastro_membros = CTk(fg_color=cor1)
    cadastro_membros.title("Cadastro de Membros")
    centralizar(cadastro_membros, 600, 600)

    texto_cadastro = CTkLabel(cadastro_membros, text_color=cor4, text='Cadastro de Membros', font=('Courier', 32, 'bold'), anchor='s')
    texto_cadastro.pack(pady=20)

    texto_cadastro2 = CTkLabel(cadastro_membros, text_color=cor4, text='Preencha as informações abaixo para criar seu perfil:', font=('Courier', 16, 'bold'))
    texto_cadastro2.pack()

    texto_usuario = CTkLabel(cadastro_membros, text_color=cor4, text='Usuário:', font=('Courier', 12, 'bold'), width=450, anchor='w')
    texto_usuario.pack(pady=5)
    entrada_usuario = CTkEntry(cadastro_membros, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu Usuário', width=450)
    entrada_usuario.pack()

    frame_ES = CTkFrame(cadastro_membros, fg_color=cor1)

    texto_email = CTkLabel(frame_ES, text_color=cor4, text='Email:', font=('Courier', 12, 'bold'), anchor='w', width=220)
    texto_email.grid(row=0, column=0, padx=5)
    entrada_email = CTkEntry(frame_ES, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu Email', width=220)
    entrada_email.grid(row=1, column=0, padx=5)

    texto_confirm_email = CTkLabel(frame_ES, text_color=cor4, text='Confirme seu Email:', font=('Courier', 12, 'bold'), anchor='w', width=220)
    texto_confirm_email.grid(row=2, column=0, padx=5)
    entrada_confirm_email = CTkEntry(frame_ES, fg_color=cor5, text_color=cor1, placeholder_text='Confirme seu Email', width=220)
    entrada_confirm_email.grid(row=3, column=0, padx=5)

    texto_senha = CTkLabel(frame_ES, text_color=cor4, text='Senha:', font=('Courier', 12, 'bold'), anchor='w', width=220)
    texto_senha.grid(row=0, column=1, padx=5)
    entrada_senha = CTkEntry(frame_ES, fg_color=cor5, text_color=cor1, placeholder_text='Digite sua senha', show='*', width=220)
    entrada_senha.grid(row=1, column=1, padx=5)

    texto_confirm_senha = CTkLabel(frame_ES, text_color=cor4, text='Confirmar Senha:', font=('Courier', 12, 'bold'), anchor='w', width=220)
    texto_confirm_senha.grid(row=2, column=1, padx=5)
    entrada_confirm_senha = CTkEntry(frame_ES, fg_color=cor5, text_color=cor1, placeholder_text='Confirme sua Senha', show='*', width=220)
    entrada_confirm_senha.grid(row=3, column=1, padx=5)

    frame_ES.pack()

    frame_TDG = CTkFrame(cadastro_membros, fg_color=cor1)

    texto_telefone = CTkLabel(frame_TDG, text_color=cor4, text='Telefone:', font=('Courier', 12, 'bold'), anchor='w', width=143)
    texto_telefone.grid(row=4, column=0, padx=5)
    entrada_telefone = CTkEntry(frame_TDG, fg_color=cor5, text_color=cor1, placeholder_text='(99) 99999-9999', width=143)
    entrada_telefone.grid(row=5, column=0, padx=5)

    texto_nascimento = CTkLabel(frame_TDG, text_color=cor4, text='Data de Nascimento:', font=('Courier', 12, 'bold'), anchor='w', width=143)
    texto_nascimento.grid(row=4, column=1, padx=5)
    entrada_nascimento = CTkEntry(frame_TDG, fg_color=cor5, text_color=cor1, placeholder_text='dd/mm/aaaa', width=143)
    entrada_nascimento.grid(row=5, column=1, padx=5)

    texto_genero = CTkLabel(frame_TDG, text_color=cor4, text='Gênero:', font=('Courier', 12, 'bold'), anchor='w', width=143)
    texto_genero.grid(row=4, column=2, padx=5)
    entrada_genero = CTkEntry(frame_TDG, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu Gênero', width=143)
    entrada_genero.grid(row=5, column=2, padx=5)

    frame_TDG.pack()

    texto_endereco = CTkLabel(cadastro_membros, text_color=cor4, text='Endereço:', font=('Courier', 12, 'bold'), width=450, anchor='w')
    texto_endereco.pack(pady=5)
    entrada_endereco = CTkEntry(cadastro_membros, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu Endereço', width=450)
    entrada_endereco.pack()

    texto_result_cad = CTkLabel(cadastro_membros, text="", justify="left", font=('Courier', 12, 'bold'))
    texto_result_cad.pack(pady=5)

    def voltar():
        cadastro_membros.destroy()
        abrir_emprestimo_devolucao()

    def ver_cadastro_membro():
        usuario, senha, conf_senha, email, conf_email, telefone, nascimento, genero, endereco = entrada_usuario.get(), entrada_senha.get(), entrada_confirm_senha.get(), entrada_email.get(), entrada_confirm_email.get(), entrada_telefone.get(), entrada_nascimento.get(), entrada_genero.get(), entrada_endereco.get()

        if any(var == '' for var in [usuario, senha, conf_senha, email, conf_email, telefone, nascimento, genero, endereco]):
            mudar_resul(texto_result_cad, 'Preencha todos os campos!', cadastro_membros)
        else:
            if senha != conf_senha:
                mudar_resul(texto_result_cad, 'As Senhas não coincidem, tente novamete!', cadastro_membros)
            elif email != conf_email:
                mudar_resul(texto_result_cad, 'Os Emails não coincidem, tente novamete!', cadastro_membros)
            elif usuario in membros_df["Usuário"].astype(str).values:
                mudar_resul(texto_result_cad, 'Esse usuário já existe, faça login. \nCaso esqueceu a senha, recupere-a.', cadastro_membros)
            else:
                add = {'Usuário':usuario, 
                       'Senha':senha, 
                       'Multas': 'Não',
                       'Email':email, 
                       'Telefone':telefone, 
                       'Data de Nascimento':nascimento,
                       'Gênero':genero, 
                       'Endereço': endereco,
                       'Status': 'Em dia'}

                membros_df.loc[len(membros_df)] = add
                membros_df.to_excel(membros, index=False)
                messagebox.showinfo('Conta Criada.', 'Usuário cadastradado com sucesso!')
    
    botao_cadastro = CTkButton(cadastro_membros, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Confirmar Cadastro', font=('Courier', 12, 'bold'), command=ver_cadastro_membro)
    botao_cadastro.pack(pady=10)

    botao_voltar = CTkButton(cadastro_membros, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Voltar', font=('Courier', 12, 'bold'), command=voltar)
    botao_voltar.pack(pady=10)

    cadastro_membros.mainloop()

def abrir_alterar_senha_membros():
    emprestimo_devolucao.destroy()
    alterar_senha = CTk(cor1)
    alterar_senha.title("Alterar Senha")
    centralizar(alterar_senha, 600, 450)

    texto_alterar_senha = CTkLabel(alterar_senha, text_color=cor4, text='Alterar Senha', font=('Courier', 32, 'bold'), anchor='s')
    texto_alterar_senha.pack(pady=20)

    texto_usuario = CTkLabel(alterar_senha, text_color=cor4, text='Usuário:', font=('Courier', 12, 'bold'), width=400, anchor='w')
    texto_usuario.pack(pady=5)

    entrada_usuario = CTkEntry(alterar_senha, fg_color=cor5, text_color=cor1, placeholder_text='Digite seu usuário', width=400)
    entrada_usuario.pack()

    texto_senha_nov = CTkLabel(alterar_senha, text_color=cor4, text='Senha Nova:', font=('Courier', 12, 'bold'), width=400, anchor='w')
    texto_senha_nov.pack(pady=5)

    entrada_senha_nov = CTkEntry(alterar_senha, fg_color=cor5, text_color=cor1, placeholder_text='Digite sua nova senha', show='*', width=400)
    entrada_senha_nov.pack()

    texto_senha_nov_conf = CTkLabel(alterar_senha, text_color=cor4, text='Confirmar Senha:', font=('Courier', 12, 'bold'), width=400, anchor='w')
    texto_senha_nov_conf.pack(pady=5)

    entrada_senha_nov_conf = CTkEntry(alterar_senha, fg_color=cor5, text_color=cor1, placeholder_text='Confirme sua senha', show='*', width=400)
    entrada_senha_nov_conf.pack()

    texto_result_nvs = CTkLabel(alterar_senha, text="", justify="left", font=('Courier', 12, 'bold'))
    texto_result_nvs.pack(pady=5)

    def voltar():
        alterar_senha.destroy()
        abrir_emprestimo_devolucao()
    
    def mudar_senha():
        usuario = entrada_usuario.get()
        senha = entrada_senha_nov.get()
        confsenha = entrada_senha_nov_conf.get()

        if not any(var == '' for var in [usuario, senha, confsenha]):
            if usuario in membros_df["Usuário"].astype(str).values:
                if senha == confsenha:
                    membros_df.loc[membros_df['Usuário'] == usuario, 'Senha'] = senha
                    membros_df.to_excel(membros)
                    messagebox.showinfo('Senha alterada', 'Senha alterada com sucesso!')
                else:
                    mudar_resul(texto_result_nvs, 'As senhas não coincidem!', alterar_senha)
            else:
                mudar_resul(texto_result_nvs, 'Usuário não encontrado!', alterar_senha)
        else:
            mudar_resul(texto_result_nvs, 'Preencha todos os campos!', alterar_senha)

    botao_alterar_senha = CTkButton(alterar_senha, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Alterar Senha', font=('Courier', 12, 'bold'), command=mudar_senha)
    botao_alterar_senha.pack(pady=10)

    botao_voltar = CTkButton(alterar_senha, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, text='Voltar', font=('Courier', 12, 'bold'), command=voltar)
    botao_voltar.pack(pady=10)

    alterar_senha.mainloop()

def pre_abrir_ed():
    principal.destroy()
    abrir_emprestimo_devolucao()

def abrir_emprestimo_devolucao():
    global emprestimo_devolucao
    emprestimo_devolucao = CTk(fg_color=cor1)
    emprestimo_devolucao.title('Gerenciador de Empréstimos e devoluções')
    centralizar(emprestimo_devolucao, 800, 600)
    
    titulo = CTkLabel(emprestimo_devolucao, text='Gerenciador de\nEmpréstimos e devoluções', text_color=cor4, font=('Courier', 32, 'bold'))
    titulo.pack(pady=20)

    texto_usuario = CTkLabel(emprestimo_devolucao, text='Usuário:', width=400, anchor='w', text_color=cor4, font=('Courier', 12, 'bold'))
    texto_usuario.pack(pady=5)
    entrada_usuario = CTkEntry(emprestimo_devolucao, placeholder_text='Digite aqui seu Usuário', width=400, fg_color=cor5, text_color=cor1)
    entrada_usuario.pack(pady=5)

    texto_senha = CTkLabel(emprestimo_devolucao, text='Senha:', width=400, anchor='w', text_color=cor4, font=('Courier', 12, 'bold'))
    texto_senha.pack(pady=5)
    entrada_senha = CTkEntry(emprestimo_devolucao, placeholder_text='Digite aqui sua Senha', width=400, fg_color=cor5, text_color=cor1)
    entrada_senha.pack(pady=5)

    texto_livro = CTkLabel(emprestimo_devolucao, text='Livro:', width=400, anchor='w', text_color=cor4, font=('Courier', 12, 'bold'))
    texto_livro.pack(pady=5)
    entrada_livro = CTkEntry(emprestimo_devolucao, placeholder_text='Digite o nome do Livro', width=400, fg_color=cor5, text_color=cor1)
    entrada_livro.pack(pady=5)

    texto_resul = CTkLabel(emprestimo_devolucao, text='', text_color=cor4, font=('Courier', 12, 'bold'))
    texto_resul.pack(pady=5)


    def emprestimo():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        livro = entrada_livro.get()
        if any(var == '' for var in [usuario, senha, livro]):
            mudar_resul(texto_resul, 'Preencha todos os campos!', emprestimo_devolucao)
        else:
            if usuario in membros_df['Usuário'].astype(str).values and senha in membros_df.loc[membros_df['Usuário'] == usuario, 'Senha'].astype(str).values:
                if 'Em dia' == membros_df.loc[membros_df['Usuário'] == usuario, 'Status'].astype(str).values:
                    if livro in livros_df["Título"].astype(str).values:
                        if 'Disponível' == livros_df.loc[livros_df['Título'] == livro, 'Status'].astype(str).values:
                            membros_df.loc[membros_df['Usuário'] == usuario, 'Status'] = 'Pendente'
                            livros_df.loc[livros_df['Título'] == livro, 'Status'] = 'Indisponível'
                            membros_df.to_excel(membros)
                            livros_df.to_excel(livros)
                            messagebox.showinfo('Empréstimo', 'Empréstimo efetuado com sucesso!')
                        else:
                            mudar_resul(texto_resul, 'Livro indisponível!', emprestimo_devolucao)
                    else:
                        mudar_resul(texto_resul, 'Livro inexistente!', emprestimo_devolucao)
                else:
                    mudar_resul(texto_resul, 'Usuário já efetuou um empréstimo!', emprestimo_devolucao)
            else:
                mudar_resul(texto_resul, 'Usuário ou senha incorretos!', emprestimo_devolucao)

    def devolucao():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        livro = entrada_livro.get()
        if any(var == '' for var in [usuario, senha, livro]):
            mudar_resul(texto_resul, 'Preencha todos os campos!', emprestimo_devolucao)
        else:
            if usuario in membros_df['Usuário'].astype(str).values and senha in membros_df.loc[membros_df['Usuário'] == usuario, 'Senha'].astype(str).values:
                if 'Pendente' == membros_df.loc[membros_df['Usuário'] == usuario, 'Status'].astype(str).values:
                    if livro in livros_df["Título"].astype(str).values:
                        if 'Indisponível' == livros_df.loc[livros_df['Título'] == livro, 'Status'].astype(str).values:
                            membros_df.loc[membros_df['Usuário'] == usuario, 'Status'] = 'Em dia'
                            livros_df.loc[livros_df['Título'] == livro, 'Status'] = 'Disponível'
                            membros_df.to_excel(membros)
                            livros_df.to_excel(livros)
                            messagebox.showinfo('Devolução', 'Devolução efetuada com sucesso!')
                        else:
                            mudar_resul(texto_resul, 'Livro não está indisponível!', emprestimo_devolucao)
                    else:
                        mudar_resul(texto_resul, 'Livro inexistente!', emprestimo_devolucao)
                else:
                    mudar_resul(texto_resul, 'Usuário não efetuou nenhum um empréstimo!', emprestimo_devolucao)
            else:
                mudar_resul(texto_resul, 'Usuário ou senha incorretos!', emprestimo_devolucao)

    frame_botoes = CTkFrame(emprestimo_devolucao, fg_color=cor1, width=400)

    botao_emprestimo = CTkButton(frame_botoes, text='Fazer Empréstimo', command=emprestimo, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_emprestimo.grid(row=0, column=0, padx=5)

    botao_devolucao = CTkButton(frame_botoes, text='Fazer Devolução', command=devolucao, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_devolucao.grid(row=0, column=2, padx=5)

    frame_botoes.pack()

    texto_conta = CTkLabel(emprestimo_devolucao, text='Não possui uma conta? Crie uma!', width=400, text_color=cor4, font=('Courier', 12, 'bold'))
    texto_conta.pack(pady=10)

    botao_cadastro = CTkButton(emprestimo_devolucao, text='Criar Conta', command=abrir_cadastro_membros, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_cadastro.pack(pady=5)

    botão_esqueceu_senha = CTkButton(emprestimo_devolucao, text_color=cor4, hover_color=cor3, corner_radius=32,text='Esqueceu ou deseja alterar sua senha?', command=abrir_alterar_senha_membros, font=('Courier', 12, 'bold'), fg_color="transparent", anchor='e')
    botão_esqueceu_senha.pack(pady=5)

    def voltar():
        emprestimo_devolucao.destroy()
        abrir_principal()
    
    botao_voltar = CTkButton(emprestimo_devolucao, text='Voltar', command=voltar, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_voltar.pack(pady=10)

    emprestimo_devolucao.mainloop()

def abrir_registro_livros():
    global imagem, label_imagem, entrada_titulo, entrada_ano, entrada_autor, entrada_editora, entrada_genero, entrada_observacao
    principal.destroy()
    registro_livros = CTk(cor1)
    registro_livros.title("Registro de livros - Biblioteca de Alexandria")
    centralizar(registro_livros, 800, 675)
    
    imagem = None
    label_imagem = None 

    titulo = CTkLabel(registro_livros, text='Registro de Livros', text_color=cor4, font=('Courier', 32, 'bold'))
    titulo.pack(pady=20)

    texto_titulo = CTkLabel(registro_livros, text='Título', width=530, anchor='w', text_color=cor4, font=('Courier', 12, 'bold'))
    texto_titulo.pack(pady=5)
    entrada_titulo = CTkEntry(registro_livros, placeholder_text='Título do livro', width=530, fg_color=cor5, text_color=cor1)
    entrada_titulo.pack(pady=5)

    frame_AAE = CTkFrame(registro_livros, fg_color=cor1)

    texto_ano = CTkLabel(frame_AAE, text='Ano de lançamento', width=170, text_color=cor4, font=('Courier', 12, 'bold'), anchor='w')
    texto_ano.grid(row=0, column=0, padx=5)
    entrada_ano = CTkEntry(frame_AAE, placeholder_text='Ano de lançamento do livro', width=170, fg_color=cor5, text_color=cor1)
    entrada_ano.grid(row=1, column=0, padx=5)

    texto_autor = CTkLabel(frame_AAE, text='Nome do(a) Autor(a)', width=170, text_color=cor4, font=('Courier', 12, 'bold'), anchor='w')
    texto_autor.grid(row=0, column=1, padx=5)
    entrada_autor = CTkEntry(frame_AAE, placeholder_text='Nome do(a) autor(a) do livro', width=170, fg_color=cor5, text_color=cor1)
    entrada_autor.grid(row=1, column=1, padx=5)

    texto_editora = CTkLabel(frame_AAE, text='Nome da Editora', width=170, text_color=cor4, font=('Courier', 12, 'bold'), anchor='w')
    texto_editora.grid(row=0, column=2, padx=5)
    entrada_editora = CTkEntry(frame_AAE, placeholder_text='Nome da editora do livro', width=170, fg_color=cor5, text_color=cor1)
    entrada_editora.grid(row=1, column=2, padx=5)

    frame_AAE.pack()
    frame_outros = CTkFrame(registro_livros, fg_color=cor1, width=530)

    def opcao_outro(gen:str):
        if gen == "Outro":
            entrada_outros.grid(row=1, column=1)
        else:
            entrada_outros.grid_forget()

    tipo = ["Ficção","Romance", "Terror", "Thriller", "Gibi", "Livro infantil", "Livro didático", "Outro"]

    entrada_outros = CTkEntry(frame_outros, placeholder_text='Insira aqui o gênero do livro', width=170, fg_color=cor5, text_color=cor1)

    texto_genero = CTkLabel(frame_outros, text='Gênero do livro', width=170, text_color=cor4, font=('Courier', 12, 'bold'))
    texto_genero.grid(row=0, column=0, padx=5)
    entrada_genero = CTkOptionMenu(frame_outros, values=tipo, command=opcao_outro, corner_radius=32, fg_color=cor2, button_color=cor2, button_hover_color=cor3, dropdown_fg_color=cor2, dropdown_hover_color=cor3)
    entrada_genero.grid(row=1, column=0, padx=5)

    frame_outros.pack(pady=10) 

    texto_observacao = CTkLabel(registro_livros, text='Observações', width=530, anchor='w', text_color=cor4, font=('Courier', 12, 'bold'))
    texto_observacao.pack(pady=5)
    entrada_observacao = CTkEntry(registro_livros, placeholder_text='Observações relevantes sobre o livro', width=530, fg_color=cor5, text_color=cor1)
    entrada_observacao.pack(pady=5)

    def escolher_imagem():
        global imagem_original
        caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        if caminho_imagem:  
            imagem_original = Image.open(caminho_imagem)
            imagem = CTkImage(light_image=imagem_original, dark_image=imagem_original, size=(100, 150))
            if label_imagem:
                label_imagem.configure(image=imagem, text="")  
    
    label_imagem = CTkLabel(registro_livros, text="Nenhuma capa selecionada", width=100, height=150, text_color=cor4, font=('Courier', 12, 'bold'))
    label_imagem.pack(pady=5)
    botao_escolher_imagem = CTkButton(registro_livros, text="Escolher Capa", command=escolher_imagem, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_escolher_imagem.pack(pady=5) 

    texto_result_reg = CTkLabel(registro_livros, text="", justify="left", font=('Courier', 12, 'bold'))
    texto_result_reg.pack(pady=5)

    def confirmar_registro():
        titulo = entrada_titulo.get()
        ano = entrada_ano.get()
        autor = entrada_autor.get()
        editora = entrada_editora.get()
        genero = entrada_genero.get() if entrada_outros.get() == '' else entrada_outros.get()
        observacao = entrada_observacao.get()
        imagem = imagem_original
        
        data = date.today().strftime("%d/%m/%Y")
        
        if any(var == '' for var in [titulo, ano, autor, editora, genero]):
            mudar_resul(texto_result_reg, 'Preencha todos os campos!', registro_livros)
        else:
            add = {'Número':len(livros_df), 
                    'Título': titulo, 
                    'Ano': ano, 
                    'Autor': autor, 
                    'Editora': editora, 
                    'Gênero': genero, 
                    'Observações': observacao, 
                    'Data de cadastro': data,
                    'Imagem': imagem, 
                    'Status': 'Disponível'}

            livros_df.loc[len(livros_df)] = add
            livros_df.to_excel(livros, index=False)
            messagebox.showinfo('Livro Registrado.', 'Livro registrado com sucesso!')

    botao_confirmar = CTkButton(registro_livros, text='Confirmar registro', command=confirmar_registro, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_confirmar.pack(pady=5)

    def voltar():
        registro_livros.destroy()
        abrir_principal()

    botao_voltar = CTkButton(registro_livros, text='Voltar', command=voltar, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_voltar.pack(pady=5)

    registro_livros.mainloop()

def abrir_gerenciar_multas():
    principal.destroy()
    gerenciar_multas = CTk(fg_color=cor1)
    gerenciar_multas.title('Gerenciador de Multas')
    centralizar(gerenciar_multas, 500, 400)
    # Funções para os botões
    def aplicar_multa():
        usuario_multa = usuario_entry.get()

        if usuario_multa in membros_df["Usuário"].astype(str).values:
            if membros_df.loc[membros_df['Usuário'] == usuario_multa, 'Multas'].astype(str).values == 'Não':
                membros_df.loc[membros_df['Usuário'] == usuario_multa, 'Multas'] = 'Sim'
                membros_df.to_excel(membros, index=False)
                detalhes_label.configure(text=f"Multa aplicada no usuário {usuario_multa}.", text_color="red")
                gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))
            else:
                detalhes_label.configure(text=f"Usuário {usuario_multa} já está com uma multa pendente.", text_color="red")
                gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))
        else:
            detalhes_label.configure(text=f"Usuário {usuario_multa} não foi encontrado.", text_color="red")
            gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))

    def pagar_multa():
        usuario_multa = usuario_entry.get()

        if usuario_multa in membros_df["Usuário"].astype(str).values:
            if membros_df.loc[membros_df['Usuário'] == usuario_multa, 'Multas'].astype(str).values == 'Sim':
                membros_df.loc[membros_df['Usuário'] == usuario_multa, 'Multas'] = 'Não'
                membros_df.to_excel(membros, index=False)
                res = messagebox.askquestion('Gerar recibo?', 'Deseja gerar um recibo de comprovação do pagamento da multa?')
                if res == 'yes':
                    print('Finge que é um recibo')
                    detalhes_label.configure(text="Recibo gerado com sucesso!", text_color="green")
                    gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))
                detalhes_label.configure(text=f"Multa do usuário {usuario_multa} paga com sucesso.", text_color="green")
                gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))
            else:
                detalhes_label.configure(text=f"Usuário {usuario_multa} não está com multas pendentes.", text_color="green")
                gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))
        else:
            detalhes_label.configure(text=f"Usuário {usuario_multa} não foi encontrado.", text_color="green")
            gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))

    def verificar_multa():
        usuario_multa = usuario_entry.get()

        if usuario_multa in membros_df["Usuário"].astype(str).values:
            if membros_df.loc[membros_df['Usuário'] == usuario_multa, 'Multas'].astype(str).values == 'Sim':
                detalhes_label.configure(text=f"Usuário {usuario_multa} está com multas pendentes.", text_color="blue")
                gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))
            else:
                detalhes_label.configure(text=f"Usuário {usuario_multa} não está com multas pendentes.", text_color="blue")
                gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))
        else:
            detalhes_label.configure(text=f"Usuário {usuario_multa} não foi encontrado.", text_color="green")
            gerenciar_multas.after(3000, lambda: detalhes_label.configure(text=""))

    # Tela
    titulo = CTkLabel(gerenciar_multas, text='Gerenciador de Multas', text_color=cor4, font=('Courier', 24, 'bold'))
    titulo.pack(pady=20)

    # Campos de entrada para usuário e senha
    usuario_label = CTkLabel(gerenciar_multas, text='Usuário', text_color=cor4, font=('Courier', 12, 'bold'))
    usuario_label.pack(pady=5)
    usuario_entry = CTkEntry(gerenciar_multas, fg_color=cor5, text_color=cor1, placeholder_text="Digite o nome do usuário")
    usuario_entry.pack(pady=5)

    # Botões
    botao_listar = CTkButton(gerenciar_multas, text="Aplicar Multa", command=aplicar_multa, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_listar.pack(pady=10)

    botao_pagar = CTkButton(gerenciar_multas, text="Pagar Multa", command=pagar_multa, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_pagar.pack(pady=10)

    botao_recibo = CTkButton(gerenciar_multas, text="Verificar Multa", command=verificar_multa, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_recibo.pack(pady=10)

    # Label para exibir detalhes
    detalhes_label = CTkLabel(gerenciar_multas, text="", justify="left", font=('Courier', 12, 'bold'))
    detalhes_label.pack(pady=20)

    def voltar():
        gerenciar_multas.destroy()
        abrir_principal()

    botao_voltar = CTkButton(gerenciar_multas, text='Voltar', command=voltar, text_color=cor4, fg_color=cor2, hover_color=cor3, corner_radius=32, font=('Courier', 12, 'bold'))
    botao_voltar.pack(pady=5)

    gerenciar_multas.mainloop()

abrir_login()