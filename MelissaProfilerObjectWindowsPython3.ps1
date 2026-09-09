<#
.SYNOPSIS
    Downloads the required components and then runs MelissaProfilerObjectWindowsPython3

.DESCRIPTION
    This script uses the Melissa Updater to fetch the data file(s), DLL(s), and the Python wrapper,
    verifies the DLL(s) downloaded, then runs the Python script against the supplied input file.

    Overall flow:
      1. Read parameters / prompt for the license and data path.
      2. Download data file(s), DLL(s), and wrapper via the Melissa Updater.
      3. Confirm the DLL(s) are present.
      4. Run the script (single test input file or interactive).

.PARAMETER file
    Path to the input file to profile.

.PARAMETER dataPath
    Path to an existing data files directory. If omitted, the script prompts for
    a path; pressing Enter at that prompt skips it and downloads the data files
    into the project's Data folder via the Melissa Updater. A path that does not
    exist aborts the script.

.PARAMETER license
    License string. Resolved in this order:
      1. This parameter.
      2. An interactive prompt, if the parameter was not supplied.
      3. The MD_LICENSE environment variable, if the prompt was left blank.
    Note that the environment variable is the last resort, not the first: running
    without -license always prompts, even when MD_LICENSE is set.

.PARAMETER quiet
    Suppresses the Melissa Updater console output during downloads.

.EXAMPLE
    .\MelissaProfilerObjectWindowsPython3.ps1 -license "your-license"

.EXAMPLE
    .\MelissaProfilerObjectWindowsPython3.ps1 -file "MelissaProfilerObjectSampleInput.csv" -license "your-license"
#>

######################### Parameters ##########################

param(
  $file = '""',
  $dataPath = '',
  $license = '', 
  [switch]$quiet = $false 
  )

######################### Classes ##########################

# Describes a single file to request from the Melissa Updater
class FileConfig {
  [string] $FileName;
  [string] $ReleaseVersion;
  [string] $OS;
  [string] $Compiler;
  [string] $Architecture;
  [string] $Type;
}

# Declared for parity with the other Melissa Updater scripts; unused in this sample.
class ManifestConfig {
  [string] $ManifestName;
  [string] $ReleaseVersion;
}

######################### Config ###########################

# Product release the updater pulls files for
$RELEASE_VERSION = '2026.Q3'
$ProductName = "profiler_data"

# Uses the location of the .ps1 file 
$CurrentPath = $PSScriptRoot
Set-Location $CurrentPath
$ProjectPath = "$CurrentPath\MelissaProfilerObjectWindowsPython3"

if ([string]::IsNullOrEmpty($dataPath)) {
  $DataPath = "$ProjectPath\Data" 
}

if (!(Test-Path $DataPath) -and ($DataPath -eq "$ProjectPath\Data")) {
  New-Item -Path $ProjectPath -Name 'Data' -ItemType "directory"
}
elseif (!(Test-Path $DataPath) -and ($DataPath -ne "$ProjectPath\Data")) {
  Write-Host "`nData file path does not exist. Please check that your file path is correct."
  Write-Host "`nAborting program, see above.  Press any button to exit.`n"
  $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") > $null
  exit
}

# Binary/DLL(s) needed to run the example
$DLLs = @(
  [FileConfig]@{
    FileName       = "mdProfiler.dll";
    ReleaseVersion = $RELEASE_VERSION;
    OS             = "WINDOWS";
    Compiler       = "DLL";
    Architecture   = "64BIT";
    Type           = "BINARY";
  }
)

# Python wrapper source that exposes the DLL to the script
$Wrapper          = [FileConfig]@{
  FileName        = "mdProfiler_pythoncode.py";
  ReleaseVersion  = $RELEASE_VERSION;
  OS              = "ANY";
  Compiler        = "PYTHON";
  Architecture    = "ANY" ;
  Type            = "INTERFACE"
}

######################## Functions #########################

# Download the product data file(s) into $DataPath via the Melissa Updater.
function DownloadDataFiles([string] $license) {
  Write-Host "`n=================================== MELISSA UPDATER ================================="
  Write-Host "MELISSA UPDATER IS DOWNLOADING DATA FILE(S)..."

  .\MelissaUpdater\MelissaUpdater.exe manifest -p $ProductName -r $RELEASE_VERSION -l $license -t $DataPath 
  if($? -eq $False ) {
    Write-Host "`nCannot run Melissa Updater. Please check your license string!"
    Exit
  }     

  Write-Host "Melissa Updater finished downloading data file(s)!"
}

# Download each DLL in $DLLs into the project folder (with a progress bar).
function DownloadDLLs() {
  Write-Host "MELISSA UPDATER IS DOWNLOADING DLL(s)..."
  $DLLProg = 0
  foreach ($DLL in $DLLs) {
    Write-Progress -Activity "Downloading DLL(s)" -Status "$([math]::round($DLLProg / $DLLs.Count * 100, 2))% Complete:"  -PercentComplete ($DLLProg / $DLLs.Count * 100)

    # Check for quiet mode
    if ($quiet) {
      .\MelissaUpdater\MelissaUpdater.exe file --filename $DLL.FileName --release_version $DLL.ReleaseVersion --license $LICENSE --os $DLL.OS --compiler $DLL.Compiler --architecture $DLL.Architecture --type $DLL.Type --target_directory $ProjectPath > $null
      if(($?) -eq $False) {
          Write-Host "`nCannot run Melissa Updater. Please check your license string!"
          Exit
      }
    }
    else {
      .\MelissaUpdater\MelissaUpdater.exe file --filename $DLL.FileName --release_version $DLL.ReleaseVersion --license $LICENSE --os $DLL.OS --compiler $DLL.Compiler --architecture $DLL.Architecture --type $DLL.Type --target_directory $ProjectPath 
      if(($?) -eq $False) {
          Write-Host "`nCannot run Melissa Updater. Please check your license string!"
          Exit
      }
    }
    
    Write-Host "Melissa Updater finished downloading " $DLL.FileName "!"
    $DLLProg++
  }
}

# Download the Python wrapper source into the project folder.
function DownloadWrapper() {
  Write-Host "MELISSA UPDATER IS DOWNLOADING WRAPPER(S)..."

  # Check for quiet mode
  if ($quiet) {
    .\MelissaUpdater\MelissaUpdater.exe file --filename $Wrapper.FileName --release_version $Wrapper.ReleaseVersion --license $LICENSE --os $Wrapper.OS --compiler $Wrapper.Compiler --architecture $Wrapper.Architecture --type $Wrapper.Type --target_directory $ProjectPath > $null
    if(($?) -eq $False) {
        Write-Host "`nCannot run Melissa Updater. Please check your license string!"
        Exit
    }
  }
  else {
    .\MelissaUpdater\MelissaUpdater.exe file --filename $Wrapper.FileName --release_version $Wrapper.ReleaseVersion --license $LICENSE --os $Wrapper.OS --compiler $Wrapper.Compiler --architecture $Wrapper.Architecture --type $Wrapper.Type --target_directory $ProjectPath 
    if(($?) -eq $False) {
        Write-Host "`nCannot run Melissa Updater. Please check your license string!"
        Exit
    }
  }

  Write-Host "Melissa Updater finished downloading " $Wrapper.FileName "!"
}

# Verify the expected DLL(s) landed in the project folder
function CheckDLLs() {
  Write-Host "`nDouble checking dll(s) were downloaded...`n"
  $FileMissing = $false 
  if (!(Test-Path ("$ProjectPath\mdProfiler.dll"))) {
    Write-Host "mdProfiler.dll not found." 
    $FileMissing = $true
  }
  if ($FileMissing) {
    Write-Host "`nMissing the above data file(s).  Please check that your license string and directory are correct."
    return $false
  }
  else {
    return $true
  }
}

########################## Main ############################

Write-Host "`n============================== Melissa Profiler Object ==============================`n                         [ Python3 | Windows | 64BIT ]`n"

# Get license (either from parameters or user input)
if ([string]::IsNullOrEmpty($license) ) {
  $License = Read-Host "Please enter your license string"
}

# Check for License from Environment Variables 
if ([string]::IsNullOrEmpty($License) ) {
  $License = $env:MD_LICENSE 
}

if ([string]::IsNullOrEmpty($License)) {
  Write-Host "`nLicense String is invalid!"
  Exit
}

# Get data file path (either from parameters or user input)
if ($DataPath -eq "$ProjectPath\Data") {
  $dataPathInput = Read-Host "Please enter your data files path directory if you have already downloaded the release zip.`nOtherwise, the data files will be downloaded using the Melissa Updater (Enter to skip)"

  if (![string]::IsNullOrEmpty($dataPathInput)) {
    if (!(Test-Path $dataPathInput)) {
      Write-Host "`nData file path does not exist. Please check that your file path is correct."
      Write-Host "`nAborting program, see above.  Press any button to exit.`n"
      $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") > $null
      exit
    }
    else {
      $DataPath = $dataPathInput
    }
  }
}

# Use Melissa Updater to download data file(s) 
# Download data file(s) 
DownloadDataFiles -license $License # Comment out this line if using own release

# Download dll(s)
DownloadDlls -license $License

# Download wrapper(s)
DownloadWrapper -license $License

# Check if all dll(s) have been downloaded. Exit script if missing
$DLLsAreDownloaded = CheckDLLs

if (!$DLLsAreDownloaded) {
  Write-Host "`nAborting program, see above.  Press any button to exit."
  $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
  exit
}

Write-Host "All file(s) have been downloaded/updated! "

# Start Program
# Run project
# No input file supplied -> run interactively; otherwise pass the input file in.
# Push-Location switches into the project folder first so the script and wrapper resolve.

if ([string]::IsNullOrEmpty($file) ) {
  Push-Location MelissaProfilerObjectWindowsPython3
  python3 MelissaProfilerObjectWindowsPython3.py --license $License  --dataPath $DataPath
  Pop-Location
}
else {
  Push-Location MelissaProfilerObjectWindowsPython3
  python3 MelissaProfilerObjectWindowsPython3.py --license $License  --dataPath $DataPath --file $file
  Pop-Location
}
