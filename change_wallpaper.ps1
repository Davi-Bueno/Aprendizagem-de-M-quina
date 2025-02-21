# Caminho absoluto da imagem (ajuste conforme necessário)
$imagePath = "$PSScriptRoot\pablovittar.jpg"

# Verifica se a imagem existe
if (Test-Path $imagePath) {
    # Adiciona suporte para modificar o plano de fundo do Windows
    Add-Type -TypeDefinition @"
        using System;
        using System.Runtime.InteropServices;
        public class Wallpaper {
            [DllImport("user32.dll", CharSet=CharSet.Auto)]
            public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
        }
"@ -Language CSharp

    # Define o plano de fundo com a imagem escolhida
    [Wallpaper]::SystemParametersInfo(20, 0, $imagePath, 3)

    # 🔹 Define o estilo do papel de parede para "Ajustar" (Fit)
    Set-ItemProperty -Path 'HKCU:\Control Panel\Desktop' -Name WallpaperStyle -Value 1
    Set-ItemProperty -Path 'HKCU:\Control Panel\Desktop' -Name TileWallpaper -Value 4

    # Atualiza o plano de fundo imediatamente
    rundll32.exe user32.dll, UpdatePerUserSystemParameters

    # 🔹 Minimiza todas as janelas para exibir a imagem
    (New-Object -ComObject Shell.Application).MinimizeAll()

    Write-Output "✅ Plano de fundo alterado com sucesso para '$imagePath' com estilo 'Ajustar'."
    Write-Output "✅ Todas as janelas foram minimizadas para exibir a imagem."
} else {
    Write-Output "🚨 Arquivo de imagem não encontrado!"
}
