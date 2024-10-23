$tool = 'C:\Program Files\gs\gs10.03.1\bin\gswin64c.exe'
$pdfs = get-childitem . -recurse | where {$_.Extension -match "pdf"}

foreach($pdf in $pdfs)
{

    $tiff = $pdf.FullName.split('.')[0] + '.tiff'
    if(test-path $tiff)
    {
        "tiff file already exists " + $tiff
    }
    else        
    {   
        'Processing ' + $pdf.Name        
        $param = "-sOutputFile=$tiff"
        & $tool -q -dNOPAUSE -sDEVICE=tiffg4 $param -r300 $pdf.FullName -c quit
    }
}