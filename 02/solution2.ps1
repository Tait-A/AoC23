

$inputTxt =  Get-Content -Path .\input.txt

$sum = 0

foreach ($line in $inputTxt) {
    $line = $line.Split(":")
    $id = [int]$line[0].Split(" ")[1]

    $game = $line[1].Split(";")

    $red = 0
    $green = 0
    $blue = 0

    foreach ($round in $game){
        $round = $round.Split(",")

        foreach ($set in $round){
            $no, $colour = $set.Split(" ")[1..2]
            $no = [int]$no
            if ($colour -eq "red" -and $no -gt $red){
                $red = [int]$no
            }
            elseif ($colour -eq "green" -and $no -gt $green){
                $green = [int]$no
            }
            elseif ($colour -eq "blue" -and $no -gt $blue) {
                $blue = [int]$no
            }
        }
    }

    $power = $red * $green * $blue
    $sum += $power

}
Write-Host $sum
