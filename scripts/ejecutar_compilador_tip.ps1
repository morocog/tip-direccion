<#
==============================================================================
Telat Group | TIP Mexico - Compilador de Layout Oficial (layout_data_repli)
==============================================================================
Ejecuta el motor ETL en Python para procesar los registros de llamadas del
conmutador cloud y generar el archivo Excel con el formato homologado de Laura Mercado.
#>

param(
    [ValidateSet("1", "2")]
    [string]$Semana = "2",
    [string[]]$Inputs,
    [string]$Template,
    [string]$Output,
    [string]$StartDate,
    [string]$EndDate
)

$ErrorActionPreference = "Stop"

# Blindaje de codificacion UTF-8 en consola
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# Deteccion dinamica y tolerante del interprete de Python
$pythonCandidates = @(
    "C:\Users\SDVP\AppData\Local\Programs\Python\Python311\python.exe",
    (Get-Command python -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -ErrorAction SilentlyContinue),
    (Get-Command py -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -ErrorAction SilentlyContinue)
)

$pythonExe = $null
foreach ($cand in $pythonCandidates) {
    if ($cand -and (Test-Path $cand)) {
        $pythonExe = $cand
        break
    }
}

if (-not $pythonExe) {
    Write-Error "No se encontro ningun ejecutable de Python disponible en el sistema."
}

$scriptPath = Join-Path $PSScriptRoot "convertir_layout_tip.py"

Write-Host "[TELAT] Iniciando compilacion de layout TIP Mexico (Semana $Semana)..." -ForegroundColor Cyan

$cmdArgs = @($scriptPath)

if ($Inputs) {
    $cmdArgs += "--inputs"
    $cmdArgs += $Inputs
    if ($Template) { $cmdArgs += @("--template", $Template) }
    if ($Output) { $cmdArgs += @("--output", $Output) }
    if ($StartDate) { $cmdArgs += @("--start-date", $StartDate) }
    if ($EndDate) { $cmdArgs += @("--end-date", $EndDate) }
} else {
    $cmdArgs += @("--semana", $Semana)
    if ($Template) { $cmdArgs += @("--template", $Template) }
    if ($Output) { $cmdArgs += @("--output", $Output) }
}

& $pythonExe $cmdArgs

if ($LASTEXITCODE -eq 0) {
    Write-Host "[TELAT] Compilacion completada con exito." -ForegroundColor Green
} else {
    Write-Error "Ocurrio un error durante la ejecucion del compilador (Codigo de salida: $LASTEXITCODE)."
}
