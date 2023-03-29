# kert vare
# kuupaev 29.03.2023


$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
# teeme siis muutuja mis hoiab nende nimesi et me saaksime neid hiljem sorteerida

$meeste_nimed = @()
$naiste_nimed = @()

$andmed = Import-Csv -Path "$dir/gender.csv"



foreach ($rida in $andmed) {

    # vaatab iga reaga kas on mees või naine ja lisab vastavalt meeste või naiste failidesse

    if ($rida.gender -eq "Male") {

        $meeste_nimed += "$($rida.first_name) $($rida.last_name)"

    } elseif ($rida.gender -eq "Female") {

        $naiste_nimed += "$($rida.first_name) $($rida.last_name)"

    }

}


$meeste_nimed >> "$dir/mehed.txt"
$naiste_nimed >> "$dir/naised.txt"


$jai_sorteerimata = $andmed.Count - ($meeste_nimed.Count + $naiste_nimed.Count)



Write-Output "Mehed ja naised on sorteeritud, sorteerimata jai $($jai_sorteerimata) nime."