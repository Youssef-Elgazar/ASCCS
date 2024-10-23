# Set the path to the directory where the .tiff files are located
$directoryPath = "C:\Users\youssef\~Joe\Projects\AIU\ASCCS\Docs"

# Set the path to the tesseract executable
$tesseractPath = "tesseract.exe"

# Get all .tiff files in the directory and its subdirectories
$tiffFiles = Get-ChildItem -Path $directoryPath -Recurse -Filter *.tiff

# Loop through each .tiff file
foreach ($file in $tiffFiles) {
    # Get the full path of the file
    $inputFilePath = $file.FullName

    # Set the output file path (same as input but with .txt extension)
    $outputFilePath = [System.IO.Path]::ChangeExtension($inputFilePath, ".txt")

    # Run tesseract on the .tiff file
    & $tesseractPath $inputFilePath $outputFilePath
}
