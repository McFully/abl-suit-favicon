# Build and Packaging Script for Suit Favicon
# Orchestrates PyInstaller and Inno Setup

$ProjectName = "SuitFavicon"
$DistDir = "dist"
$InstallerDir = "installer"

Write-Host "--- Starting Build Process for $ProjectName ---" -ForegroundColor Cyan

# 1. Install Dependencies
Write-Host "[1/4] Installing dependencies from requirements.txt..." -ForegroundColor Yellow
pip install -r requirements.txt

# 2. Build Executable with PyInstaller
Write-Host "[2/4] Building executable with PyInstaller..." -ForegroundColor Yellow
# --noconsole for GUI apps
# --onedir is better for complex apps with many dependencies like rembg
pyinstaller --noconsole --onedir --name $ProjectName --clean main.py

if ($LASTEXITCODE -ne 0) {
    Write-Error "PyInstaller failed. Aborting."
    exit $LASTEXITCODE
}

# 3. Create Installer with Inno Setup
Write-Host "[3/4] Searching for Inno Setup Compiler (iscc.exe)..." -ForegroundColor Yellow
$ISCC = Get-Command iscc.exe -ErrorAction SilentlyContinue

if ($ISCC) {
    Write-Host "Found ISCC at $($ISCC.Source). Generating setup.exe..." -ForegroundColor Green
    & $ISCC.Source "$InstallerDir\setup.iss"
} else {
    Write-Warning "Inno Setup (iscc.exe) not found in PATH."
    Write-Warning "Please install Inno Setup and run: iscc $InstallerDir\setup.iss manually."
}

# 4. Finalizing
Write-Host "--- Build Process Completed ---" -ForegroundColor Cyan
if (Test-Path "dist_installer") {
    Write-Host "Installer generated in: dist_installer\" -ForegroundColor Green
    $SetupFile = Get-ChildItem "dist_installer\*.exe" | Select-Object -First 1
    if ($SetupFile -and (Test-Path "landing")) {
        Write-Host "Copying installer to landing directory for deployment..." -ForegroundColor Yellow
        Copy-Item $SetupFile.FullName "landing\"
    }
}
