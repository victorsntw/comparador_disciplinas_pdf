@echo off
title Instalando dependencias...
echo ========================================
echo   Instalando bibliotecas necessarias
echo ========================================
echo.

REM Tenta instalar as bibliotecas
python -m pip install --upgrade pip >nul 2>&1
python -m pip install pdfplumber unidecode

if errorlevel 1 (
    echo.
    echo ERRO: Python nao encontrado no sistema.
    echo Baixe em: https://www.python.org/downloads/
    echo Ao instalar, marque a opcao "Add Python to PATH".
    pause
    exit /b
)

echo.
echo Instalacao concluida! Abrindo o comparador...
echo.
python comparador_disciplinas.py
pause