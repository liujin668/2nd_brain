$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$taskDocx = (Get-ChildItem -LiteralPath $taskRoot -Filter '*.docx' | Select-Object -First 1).FullName
$taskRender = Join-Path $PSScriptRoot 'render'
New-Item -ItemType Directory -Path $taskRender -Force | Out-Null
$taskPdf = Join-Path $taskRender 'template.pdf'
$taskWord = $null
$taskDocument = $null
try {
    $taskWord = New-Object -ComObject Word.Application
    $taskWord.Visible = $false
    $taskWord.DisplayAlerts = 0
    $taskWord.AutomationSecurity = 3
    $taskDocument = $taskWord.Documents.Open($taskDocx, $false, $true)
    $taskDocument.Repaginate()
    $taskDocument.ExportAsFixedFormat($taskPdf, 17)
    Write-Output ('Rendered pages: ' + $taskDocument.ComputeStatistics(2))
} finally {
    if ($null -ne $taskDocument) { $taskDocument.Close(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($taskDocument) }
    if ($null -ne $taskWord) { $taskWord.Quit(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($taskWord) }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
