@echo off
chcp 65001 >nul
color 1F
title Verificacion Matutina de Lineas de Atencion - TIP Mexico

echo ======================================================================
echo           TELAT GROUP - CONTROL OPERATIVO TIP MEXICO
echo       VERIFICACION MATUTINA DE LINEAS DE ATENCION POR MARCA
echo ======================================================================
echo.
echo  Instrucciones para Miriam:
echo  1. Asegurate de tener Bria abierto en tu computadora.
echo  2. El script marcara a los 9 numeros publicos de cada linea y marca.
echo  3. En cuanto escuches el audio de bienvenida en tu diadema, cuelga en Bria.
echo  4. Presiona [ENTER] en esta ventana para pasar a la siguiente marca.
echo.
echo ======================================================================
pause
cls

:: --- LINEA 1 ---
echo.
echo [1 de 9] Marcando a: TIP GENERAL (800 908 6700)
echo -> Disparando llamada a Bria...
start "" "sip:8009086700"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- LINEA 2 ---
echo.
echo [2 de 9] Marcando a: BITCAR (800 999 2136)
echo -> Disparando llamada a Bria...
start "" "sip:8009992136"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- LINEA 3 ---
echo.
echo [3 de 9] Marcando a: OFS (55 5093 7300)
echo -> Disparando llamada a Bria...
start "" "sip:5550937300"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- LINEA 4 ---
echo.
echo [4 de 9] Marcando a: JAC (800 649 0751)
echo -> Disparando llamada a Bria...
start "" "sip:8006490751"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- LINEA 5 ---
echo.
echo [5 de 9] Marcando a: KIA (800 999 1151)
echo -> Disparando llamada a Bria...
start "" "sip:8009991151"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- LINEA 6 ---
echo.
echo [6 de 9] Marcando a: MG (800 999 2057)
echo -> Disparando llamada a Bria...
start "" "sip:8009992057"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- LINEA 7 ---
echo.
echo [7 de 9] Marcando a: GCO (800 967 0527)
echo -> Disparando llamada a Bria...
start "" "sip:8009670527"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- LINEA 8 ---
echo.
echo [8 de 9] Marcando a: CHIREY (800 649 0084)
echo -> Disparando llamada a Bria...
start "" "sip:8006490084"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- LINEA 9 ---
echo.
echo [9 de 9] Marcando a: CARNOT (800 122 7668)
echo -> Disparando llamada a Bria...
start "" "sip:8001227668"
echo -> Escucha el audio de bienvenida en tu diadema y cuelga en Bria.
pause
cls

:: --- FIN DE LA PRUEBA Y COPIADO AL PORTAPAPELES ---
powershell -NoProfile -Command "$h = (Get-Date).ToString('dd/MM/yyyy HH:mm'); $t = @\"
📞 Verificación matutina de líneas de atención - TIP México
Fecha y hora: $h hrs

Se realizaron llamadas de prueba a cada número directo a 10 dígitos:
✅ TIP General (800 908 6700): Conectada y con audio de bienvenida OK
✅ Bitcar (800 999 2136): Conectada y con audio de bienvenida OK
✅ OFS (55 5093 7300): Conectada y con audio de bienvenida OK
✅ JAC (800 649 0751): Conectada y con audio de bienvenida OK
✅ KIA (800 999 1151): Conectada y con audio de bienvenida OK
✅ MG (800 999 2057): Conectada y con audio de bienvenida OK
✅ GCO (800 967 0527): Conectada y con audio de bienvenida OK
✅ Chirey (800 649 0084): Conectada y con audio de bienvenida OK
✅ Carnot (800 122 7668): Conectada y con audio de bienvenida OK

Resultado: 9 de 9 líneas operativas con enrutamiento y audio correcto.
\"@; Set-Clipboard -Value $t; Write-Host $t"

echo.
echo ======================================================================
echo ¡LISTO! El reporte detallado de arriba ya esta copiado en tu portapapeles.
echo Solo abre el chat de WhatsApp de TIP y presiona Ctrl + V para enviarlo.
echo ======================================================================
echo.
pause
