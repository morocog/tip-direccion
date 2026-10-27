# ==============================================================================
# Telat Group | TIP Mexico - Compilador de Layout inConcert (layout_data_repli)
# ==============================================================================
# Ejecuta el motor ETL en Python para procesar las llamadas de N2A y generar
# el archivo Excel con el formato homologado de Laura Mercado (TIP Mexico).

$ErrorActionPreference = "Stop"

$pythonExe = "C:\Users\SDVP\AppData\Local\Programs\Python\Python311\python.exe"
$scriptPath = Join-Path $PSScriptRoot "convertir_layout_tip.py"

if (-not (Test-Path $pythonExe)) {
    Write-Error "No se encontro el ejecutable de Python en: $pythonExe"
}

Write-Host "[TELAT] Iniciando compilacion de layout TIP Mexico..." -ForegroundColor Cyan
& $pythonExe $scriptPath $args

if ($LASTEXITCODE -eq 0) {
    Write-Host "[TELAT] Compilacion completada con exito." -ForegroundColor Green
    Write-Host "[TELAT] Archivo listo en: $env:USERPROFILE\Downloads\layout_data_repli_19_al_23_oct_2026.xlsx" -ForegroundColor Yellow
} else {
    Write-Error "Ocurrio un error durante la ejecucion del compilador."
}
