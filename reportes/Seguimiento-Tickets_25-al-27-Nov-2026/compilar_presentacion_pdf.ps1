$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$htmlFile = Join-Path $scriptDir "presentacion_tip_27nov2026.html"
$outputPdf = Join-Path $scriptDir "presentacion_tip_27nov2026.pdf"

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
    Write-Host "PDF generado: $($item.FullName) ($([math]::Round($item.Length / 1KB, 2)) KB)" -ForegroundColor Green
} else {
    Write-Host "ERROR: No se generó el PDF." -ForegroundColor Red
    exit 1
}
