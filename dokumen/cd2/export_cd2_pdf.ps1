$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Definition }
    $docxPath = (Resolve-Path (Join-Path $scriptDir "CD2_Jeruk_Limau.docx")).Path
    $pdfPath = Join-Path $scriptDir "CD2_Jeruk_Limau.pdf"
    
    Write-Host "Opening Word file: $docxPath"
    $doc = $word.Documents.Open($docxPath, $false, $true)
    
    Write-Host "Exporting to PDF: $pdfPath"
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    
    $pageCount = $doc.ComputeStatistics(2)
    $doc.Close([ref]$false)
    Write-Host "SUCCESS! Page count: $pageCount"
} catch {
    Write-Host "ERROR: $_"
} finally {
    $word.Quit()
}
