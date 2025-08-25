#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk

def dizer_ola():
    label.config(text="Olá, mundo!")

# Criar janela principal
janela = tk.Tk()
janela.title("Exemplo Tkinter - Olá Mundo")
janela.geometry("300x150")  # largura x altura

# Label (mensagem inicial)
label = tk.Label(janela, text="Clique no botão para dizer Olá!")
label.pack(pady=10)

# Botão para mostrar mensagem
botao_ola = tk.Button(janela, text="Dizer Olá", command=dizer_ola)
botao_ola.pack(pady=5)

# Botão para sair
botao_sair = tk.Button(janela, text="Sair", command=janela.quit)
botao_sair.pack(pady=5)

# Iniciar loop da interface
janela.mainloop()
