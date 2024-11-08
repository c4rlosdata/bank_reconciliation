import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
import numpy as np
from formatacao import format_files
from preenchedor_v2 import sheet_filling

# Flag de sinalização
formatacao_concluida = False

def abrir_arquivos():
    global formatacao_concluida  # Acessar a variável global
    filepaths = filedialog.askopenfilenames(
        initialdir="/",
        title="Selecione arquivos XLSX",
        filetypes=(("Arquivos XLSX", "*.xlsx"), ("todos os arquivos", "*.*"))
    )
    if not filepaths or len(filepaths) != 2:
        messagebox.showwarning("Aviso", "Selecione exatamente dois arquivos XLSX.")
        return

    try:
        df_itau = pd.read_excel(filepaths[0])
        df_kazah = pd.read_excel(filepaths[1])
        
        # Executar a formatação e definir a flag
        format_files(df_itau, df_kazah)
        formatacao_concluida = True

        # Verificar se a formatação foi concluída antes de preencher
        if formatacao_concluida:
            sheet_filling()
            messagebox.showinfo("Sucesso", "Arquivos formatados e planilha preenchida com sucesso!")
        else:
            messagebox.showerror("Erro", "A formatação dos arquivos ainda não foi concluída.")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado.")



# Cria a janela principal
janela = tk.Tk()
janela.title("Formatador de Arquivos e planilha preenchida")

# Estilo para os widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))

# Rótulo de instrução
ttk.Label(janela, text="Selecione os arquivos Itaú e Kazah:").pack(pady=10)

# Botão para abrir arquivos
ttk.Button(janela, text="Abrir Arquivos", command=abrir_arquivos).pack()

janela.mainloop()
