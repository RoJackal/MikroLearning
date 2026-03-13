param (
    [switch]$Verbose = $false,
    [switch]$DryRun = $false
)
$inputPath = ".\tailwind_input.css"
$outputPath = ".\static\css\dist\styles.css"
$contentPaths = ".\templates\**\*.html,.\**\*.py,.\static\js\**\*.js"
if (!(Test-Path $inputPath)) {
    Write-Host "No input CSS found. Creating $inputPath..." -ForegroundColor Yellow
    "@import 'tailwindcss';" | Out-File -FilePath $inputPath -Encoding utf8
}
if (!(Test-Path ".\static\css\dist")) {
    if (-not $DryRun) { New-Item -ItemType Directory -Path ".\static\css\dist" -Force | Out-Null }
}
$args = @("-i", $inputPath, "-o", $outputPath, "--content", $contentPaths, "--minify")
if ($Verbose) { $args += "--verbose" }
if ($DryRun) {
    Write-Host "[DRY RUN] Would execute: .\tailwindcss.exe $($args -join ' ')" -ForegroundColor Magenta
} else {
    Write-Host "Optimizing Tailwind for Django..." -ForegroundColor Cyan
    .\tailwindcss.exe @args
    Write-Host "Success! CSS generated at $outputPath" -ForegroundColor Green
}
