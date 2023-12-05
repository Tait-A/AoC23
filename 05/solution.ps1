$inputTxt =  Get-Content -Path .\input.txt

$seeds = $inputTxt[0]

$rest = $inputTxt[1..$inputTxt.Count]

[System.Collections.ArrayList]$maps = @()

$seeds = $seeds.Split(" ")
$seeds = $seeds[1..$seeds.Count]

for ($i = 0; $i -lt $seeds.Count; $i++){
    $seeds[$i] = [long]$seeds[$i]
}

foreach ($line in $rest){
    if ($line -eq ""){
        [System.Collections.ArrayList]$newArray = @()
        $maps.Add($newArray)
    }
    else{
        $maps[-1].Add($line)
    }
}


[System.Collections.ArrayList]$indices = @()

foreach ($seed in $seeds){

    $index = [long]$seed
    foreach ($map in $maps){
        foreach ($line in $map[1..$map.Count]){
            $line = $line.Split(" ")
            $dest = [long]$line[0]
            $src = [long]$line[1] 
            $range = [long]$line[2]
            

            if ($index -ge $src -and $index -lt ($src + $range)){
                Write-Host $dest $src $range $index
                $index = $index + $dest - $src
                Write-Host $index
                break
            }
        }
    }
    $indices.Add($index)
}

$lowest = $indices[0]
for ($i = 0; $i -lt $indices.Count; $i++){
    if ($indices[$i] -lt $lowest){
        Write-Host $lowest
        $lowest = $indices[$i]
        $lowestseed = [long]$seeds[$i]

    }
}
Write-Host $lowest
