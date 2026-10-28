# 📚 Comparador de Disciplinas entre Ementas (PDF)

Ferramenta em Python desenvolvida para **universidades privadas** que precisam comparar ementas/grades curriculares de diferentes cursos (ou da mesma instituição) e identificar automaticamente **disciplinas em comum** para fins de **aproveitamento de créditos**.

---

## 🎯 Objetivo

Resolver o problema operacional de coordenações acadêmicas que precisam, manualmente, cruzar duas ementas em PDF para descobrir quais disciplinas podem ser aproveitadas por alunos transferidos ou em segunda graduação. O script automatiza essa leitura, comparação e gera um relatório em TXT.

---

## ✨ Funcionalidades

- ✅ Leitura automática de **2 arquivos PDF** (ementa antiga e nova)
- ✅ Interface gráfica simples via `tkinter` para seleção dos arquivos
- ✅ Comparação inteligente com **tolerância a variações** (acentos, maiúsculas, espaços)
- ✅ Uso do algoritmo `SequenceMatcher` para detectar nomes similares (ex.: *"Cenários Econômicos"* ≈ *"Cenarios Economicos"*)
- ✅ Geração automática de relatório em TXT: `Cursos que podem ser aproveitados.txt`
- ✅ Validações: evita arquivos duplicados, PDFs faltando ou corrompidos
- ✅ Instalação de dependências automatizada via `.bat`

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| **Python 3.8+** | Linguagem base |
| **pdfplumber** | Extração de texto de PDFs |
| **unidecode** | Normalização de caracteres (acentos) |
| **tkinter** | Interface gráfica (nativo do Python) |
| **difflib** | Cálculo de similaridade entre strings |

---

## 📋 Pré-requisitos

- [Python 3.8 ou superior](https://www.python.org/downloads/) instalado
- Durante a instalação do Python, **marque a opção "Add Python to PATH"**

---

## 🚀 Instalação e Uso

### Opção 1 — Instalação automática (recomendada para usuários leigos)

1. Clone ou baixe este repositório
2. Coloque os **2 PDFs** (ementa antiga e nova) em qualquer pasta
3. Dê **duplo clique** em `Instalar_e_Rodar.bat`
4. O script instala as dependências e abre a janela automaticamente

### Opção 2 — Instalação manual

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/comparador-disciplinas.git
cd comparador-disciplinas

# Instale as dependências
pip install pdfplumber unidecode

# Execute o script
python comparador_disciplinas.py
```

---

## 🖥️ Como usar

1. Ao abrir o programa, clique em **"Selecionar PDF 1"** → escolha o PDF do **curso antigo / histórico**
2. Clique em **"Selecionar PDF 2"** → escolha o PDF do **curso novo / grade atual**
3. Clique em **"🔍 Comparar e gerar relatório"**
4. O arquivo `Cursos que podem ser aproveitados.txt` será salvo na mesma pasta do PDF 1

---

## 📁 Estrutura do Projeto

```
comparador-disciplinas/
├── comparador_disciplinas.py   # Script principal
├── Instalar_e_Rodar.bat        # Instalador + executor (Windows)
├── Executar.bat                # Executor (após instalação)
├── README.md                   # Esta documentação
└── exemplos/                   # PDFs de exemplo (opcional)
```

---

## ⚙️ Como funciona (resumo técnico)

1. O `pdfplumber` extrai o texto bruto de cada PDF
2. O texto é normalizado (minúsculas, sem acentos, sem espaços extras)
3. Linhas são filtradas por heurísticas para identificar possíveis nomes de disciplinas
4. Cada disciplina do PDF 1 é comparada com todas do PDF 2 usando `SequenceMatcher`
5. Pares com **similaridade ≥ 85%** são considerados equivalentes
6. O resultado é gravado em TXT formatado

> 💡 O limite de similaridade (85%) pode ser ajustado na constante `LIMITE_SIMILARIDADE` no código.

---

## ⚠️ Limitações conhecidas

- PDFs escaneados (imagem) **não** são lidos — o texto precisa estar selecionável
- Ementas em formato de tabela muito complexa podem exigir ajuste na heurística de extração
- Disciplinas com nomes muito diferentes mas conteúdo equivalente não são detectadas (apenas comparação textual)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch: `git checkout -b minha-feature`
3. Commit: `git commit -m 'feat: minha nova feature'`
4. Push: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por ** Antonio Victor** — sob demanda para universidade privada.

> 💬 Dúvidas ou sugestões? Abra uma *issue* neste repositório.