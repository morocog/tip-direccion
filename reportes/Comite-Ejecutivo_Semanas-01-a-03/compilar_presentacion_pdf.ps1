# Script de compilación PDF para la Presentación Ejecutiva Semanas 01 a 03 (TIP México)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$htmlFile = Join-Path $scriptDir "presentacion_ejecutiva_tip_semanas_01_a_03.html"
$outputPdf = Join-Path $scriptDir "presentacion_ejecutiva_tip_semanas_01_a_03.pdf"

Write-Host "Iniciando compilación PDF para el Comité Ejecutivo de TIP México (3 Láminas 16:9)..." -ForegroundColor Cyan

if (-not (Test-Path $htmlFile)) {
    Write-Host "ERROR: No existe $htmlFile" -ForegroundColor Red
    exit 1
}

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    $chromePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
}

$htmlUri = "file:///" + ($htmlFile -replace '\\', '/')

$chromeArgs = @(
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=4000",
    "--print-to-pdf=$outputPdf",
    $htmlUri
)

Start-Process -FilePath $chromePath -ArgumentList $chromeArgs -Wait -NoNewWindow

if (Test-Path $outputPdf) {
    $item = Get-Item $outputPdf
    Write-Host "PDF generado exitosamente: $($item.FullName)" -ForegroundColor Green
    Write-Host "Tamaño: $([math]::Round($item.Length / 1KB, 2)) KB" -ForegroundColor Green
} else {
    Write-Host "ERROR: No se encontró el PDF generado." -ForegroundColor Red
    exit 1
}
