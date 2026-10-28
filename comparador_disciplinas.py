import os
import re
import pdfplumber
from unidecode import unidecode
from difflib import SequenceMatcher
import tkinter as tk
from tkinter import filedialog, messagebox

LIMITE_SIMILARIDADE = 0.85


def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            t = pagina.extract_text()
            if t:
                texto += t + "\n"
    return texto


def normalizar(texto):
    return re.sub(r"\s+", " ", unidecode(texto)).strip().lower()


def extrair_disciplinas(texto):
    disciplinas = set()
    for linha in texto.split("\n"):
        linha = linha.strip()
        if not linha or len(linha) < 4:
            continue
        if re.fullmatch(r"[\d\.\-\s]+", linha):
            continue
        if linha.lower() in {"ementa", "grade curricular", "disciplinas", "curso"}:
            continue
        disciplinas.add(linha)
    return disciplinas


def similaridade(a, b):
    return SequenceMatcher(None, a, b).ratio()


def encontrar_comuns(lista_a, lista_b):
    comuns = []
    norm_b = {normalizar(x): x for x in lista_b}
    for item_a in lista_a:
        na = normalizar(item_a)
        for nb, orig_b in norm_b.items():
            if similaridade(na, nb) >= LIMITE_SIMILARIDADE:
                comuns.append((item_a, orig_b))
                break
    return comuns


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparador de Disciplinas")
        self.root.geometry("520x320")
        self.root.resizable(False, False)

        self.pdf1 = None
        self.pdf2 = None

        tk.Label(root, text="📚 Comparador de Disciplinas",
                 font=("Arial", 14, "bold")).pack(pady=10)

        # PDF 1
        frame1 = tk.Frame(root)
        frame1.pack(fill="x", padx=20, pady=5)
        tk.Label(frame1, text="PDF 1 (Curso antigo / histórico):",
                 anchor="w").pack(fill="x")
        self.lbl1 = tk.Label(frame1, text="Nenhum arquivo selecionado",
                             fg="gray", anchor="w", wraplength=460)
        self.lbl1.pack(fill="x")
        tk.Button(frame1, text="Selecionar PDF 1",
                  command=self.selecionar_pdf1).pack(pady=3)

        # PDF 2
        frame2 = tk.Frame(root)
        frame2.pack(fill="x", padx=20, pady=5)
        tk.Label(frame2, text="PDF 2 (Curso novo / grade atual):",
                 anchor="w").pack(fill="x")
        self.lbl2 = tk.Label(frame2, text="Nenhum arquivo selecionado",
                             fg="gray", anchor="w", wraplength=460)
        self.lbl2.pack(fill="x")
        tk.Button(frame2, text="Selecionar PDF 2",
                  command=self.selecionar_pdf2).pack(pady=3)

        # Botão comparar
        tk.Button(root, text="🔍 Comparar e gerar relatório",
                  font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
                  command=self.comparar).pack(pady=15)

    def selecionar_pdf1(self):
        caminho = filedialog.askopenfilename(
            title="Selecione o PDF do curso antigo",
            filetypes=[("PDF", "*.pdf")])
        if caminho:
            self.pdf1 = caminho
            self.lbl1.config(text=os.path.basename(caminho), fg="black")

    def selecionar_pdf2(self):
        caminho = filedialog.askopenfilename(
            title="Selecione o PDF do curso novo",
            filetypes=[("PDF", "*.pdf")])
        if caminho:
            self.pdf2 = caminho
            self.lbl2.config(text=os.path.basename(caminho), fg="black")

    def comparar(self):
        if not self.pdf1 or not self.pdf2:
            messagebox.showwarning("Atenção",
                                   "Selecione os DOIS arquivos PDF antes de comparar.")
            return
        if self.pdf1 == self.pdf2:
            messagebox.showwarning("Atenção",
                                   "Você selecionou o mesmo arquivo duas vezes.")
            return

        try:
            texto1 = extrair_texto_pdf(self.pdf1)
            texto2 = extrair_texto_pdf(self.pdf2)
            disc1 = extrair_disciplinas(texto1)
            disc2 = extrair_disciplinas(texto2)
            comuns = encontrar_comuns(disc1, disc2)

            # Salva o TXT na mesma pasta do PDF 1
            pasta_saida = os.path.dirname(self.pdf1)
            caminho_saida = os.path.join(pasta_saida,
                                         "Cursos que podem ser aproveitados.txt")
            with open(caminho_saida, "w", encoding="utf-8") as f:
                f.write("DISCIPLINAS EM COMUM (APROVEITÁVEIS)\n")
                f.write(f"PDF 1: {os.path.basename(self.pdf1)}\n")
                f.write(f"PDF 2: {os.path.basename(self.pdf2)}\n")
                f.write("=" * 60 + "\n\n")
                if comuns:
                    for i, (d1, d2) in enumerate(comuns, 1):
                        f.write(f"{i:02d}. {d1}   <-->   {d2}\n")
                else:
                    f.write("Nenhuma disciplina em comum foi identificada.\n")

            messagebox.showinfo("Concluído",
                                f"{len(comuns)} disciplina(s) em comum.\n\n"
                                f"Arquivo salvo em:\n{caminho_saida}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao processar:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()