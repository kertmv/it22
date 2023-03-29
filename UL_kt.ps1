# ÜL kt
# kert markus vare
# kuupäev jaanuar 29.03.2023

#küsib csv faili


#vaatab kas on csv fail
$loop = 1
while($loop -eq 1 ){
$fileName = Read-Host "anna mulle csv fail"
if ($fileName -notmatch ".csv$") {
  Write-Host "fail pole csv fail"
  #STOP, FAIL POLE CSV
 
 

}

else
{
$loop = 0

#csv fail on nyyd $names sees
$names = Import-Csv -Path $fileName

#domeen küs
$domain = Read-Host "anna domeen palun"

#output txt fail
$outputFile = "emails.txt"

#loop
foreach ($name in $names) {
  #väiksed tähed
  $firstName = $name.FirstName.ToLower()
  $lastName = $name.LastName.ToLower()

  #tee email adress
  $email = "$firstName.$lastName@$domain"

  #salvesta faili
  Add-Content -Path $outputFile -Value $email
}
}
}