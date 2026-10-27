$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = [Microsoft.Office.Interop.Word.WdAlertLevel]::wdAlertsNone

try {
    $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Definition }
    $docxPath = (Resolve-Path (Join-Path $scriptDir "CD2_Jeruk_Limau.docx")).Path
    $pdfPath = Join-Path $scriptDir "CD2_Jeruk_Limau.pdf"
    
    Write-Host "Opening Word file: $docxPath"
    $doc = $word.Documents.Open($docxPath, $false, $true)
    $pageCount = $doc.ComputeStatistics(2)
    Write-Host "Document opened. Page count: $pageCount"
    
    Write-Host "Exporting to PDF: $pdfPath"
    $doc.ExportAsFixedFormat($pdfPath, 17)
    Write-Host "SUCCESS! Export complete. Page count: $pageCount"
    
    $doc.Close($false)
} catch {
    Write-Host "ERROR: $($_.Exception.Message)"
} finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
