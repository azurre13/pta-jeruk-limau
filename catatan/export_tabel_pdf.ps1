# Export Tabel_Perbandingan_Alternatif_Solusi.docx to PDF
$docxPath = (Resolve-Path "c:\Users\LENOVO\Documents\TA lulus\CD (Capstone Design)\catatan\Tabel_Perbandingan_Alternatif_Solusi.docx").Path
$pdfPath = [System.IO.Path]::ChangeExtension($docxPath, ".pdf")
$drafPdfPath = "c:\Users\LENOVO\Documents\TA lulus\CD (Capstone Design)\dokumen\draf\cd3\Tabel_Perbandingan_Alternatif_Solusi.pdf"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    Write-Host "Opening Word document: $docxPath"
    $doc = $word.Documents.Open($docxPath)
    $pages = $doc.ComputeStatistics(2)
    Write-Host "Page count: $pages"
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
    Write-Host "Successfully exported to: $pdfPath"
    $doc.Close([ref]$false)
    
    Copy-Item $pdfPath $drafPdfPath -Force
    Write-Host "Copied PDF to: $drafPdfPath"
} catch {
    Write-Error "Failed: $_"
} finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
