from tkinter import *

def verificar_autenticacao():
    usuario_digitado = usuario_entry.get()
    senha_digitada = senha_entry.get()

    if senha_digitada == usuario_digitado:
        resultado_label.config(text='Senha incorreta, nome de usuário e senha não podem ser iguais!')
    else:
        resultado_label.config(text=f'Bem-vindo, {usuario_digitado}!')


janela = Tk()
janela.title('Autenticação de Usuário')
janela.geometry('400x300')


texto_usuario = Label(janela, text='Informe seu nome de usuário:')
texto_usuario.pack(padx=10, pady=10)

usuario_entry = Entry(janela)
usuario_entry.pack(padx=10, pady=10)

texto_senha = Label(janela, text='Informe sua senha:')
texto_senha.pack(padx=10, pady=10)

senha_entry = Entry(janela, show='*')  
senha_entry.pack(padx=10, pady=10)

botao_autenticar = Button(janela, text='Autenticar', command=verificar_autenticacao)
botao_autenticar.pack(padx=10, pady=10)

resultado_label = Label(janela, text='')
resultado_label.pack(padx=10, pady=10)


janela.mainloop()
