@echo off
title Comparador de Disciplinas
echo ========================================
echo   Comparador de Disciplinas - PDF
echo ========================================
python comparador_disciplinas.py
if errorlevel 1 (
    echo.
    echo ERRO: Python nao encontrado. Instale Python e as bibliotecas:
    echo   pip install pdfplumber unidecode
    pause
)