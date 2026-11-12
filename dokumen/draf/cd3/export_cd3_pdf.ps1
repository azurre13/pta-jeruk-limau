# PowerShell script to export CD3_Jeruk_Limau.docx to CD3_Jeruk_Limau.pdf via Word COM
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$docxPath = (Resolve-Path (Join-Path $scriptDir "CD3_Jeruk_Limau.docx")).Path
$pdfPath = [System.IO.Path]::Combine($scriptDir, "CD3_Jeruk_Limau.pdf")

if (-not (Test-Path $docxPath)) {
    Write-Error "File not found: $docxPath"
    exit 1
}

Write-Host "Opening Microsoft Word COM..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    Write-Host "Opening document: $docxPath"
    $doc = $word.Documents.Open($docxPath)
    
    $pages = $doc.ComputeStatistics(2)
    Write-Host "Document page count: $pages"
    
    Write-Host "Exporting to PDF: $pdfPath"
    $doc.ExportAsFixedFormat(
        $pdfPath,
        17,
        $false,
        0, # OptimizeForPrint
        0, # AllDocument
        1,
        1,
        0, # DocumentContent
        $true,
        $true,
        1, # Heading bookmarks
        $true,
        $true,
        $false
    )
    Write-Host "Export completed successfully!"
    $doc.Close([ref]$false)
} catch {
    Write-Error "Failed to export PDF: $_"
} finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
