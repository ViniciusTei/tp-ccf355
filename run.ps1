param(
  [Parameter()]
  $install
)

Write-Host "Creating environment"

./venv/Scripts/Activate

if($install) {
  Write-Host "Installing dependecies..."
  pip install -r ./client/requirements.txt
}

Write-Host "Everything is ready to use!"