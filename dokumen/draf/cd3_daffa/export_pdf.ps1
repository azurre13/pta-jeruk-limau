param(
    [string]$TargetDir = $PSScriptRoot
)

$ErrorActionPreference = "Stop"
$files = @(
    "Tabel_Perbandingan_Alternatif_Solusi.docx",
    "CD3_Jeruk_Limau_Usulan.docx"
)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    foreach ($fn in $files) {
        $docxPath = Join-Path $TargetDir $fn
        $pdfPath = [System.IO.Path]::ChangeExtension($docxPath, ".pdf")
        if (-not (Test-Path $docxPath)) {
            Write-Warning "Tidak ditemukan: $docxPath"
            continue
        }
        $doc = $word.Documents.Open($docxPath, $false, $true)
        $doc.Repaginate()
        $pages = $doc.ComputeStatistics(2)
        # wdExportFormatPDF = 17, optimize print = 0, exportAllDocument = 0
        $doc.ExportAsFixedFormat($pdfPath, 17, $false, 0, 0, 1, 1, 0, $true, $true, 1, $true, $true, $false)
        $doc.Close([ref]$false)
        Write-Output "EXPORTED|$fn|$pages|$pdfPath"
    }
}
finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}

