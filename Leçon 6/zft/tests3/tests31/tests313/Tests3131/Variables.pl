#**********************************************#
# Premiers essais en Perl de Guillaume Bourlet #
# Auteur : Guillaume Bourlet                   #
# Date 10/08/2010                              #
# Variables scalaires			       #
#**********************************************#

# les variables scalaires (chaines et nombres) sont préfixées par le $

#**********************************************#
# 		    numérique		       #
#**********************************************#	

$Pht = 153 ; # prix hors taxe
$TTva = 19.6 ; # taux de tva

$Pttc = $Pht * (1+$TTva/100) ; # calcul du prix TTC

print "\nLe prix TTC est $Pttc €\n"; 

# troncage au centime d'euro le plus proche
$NbMillime = int($Pttc*1000); # nb de millimes d'euros
$Millime = $NbMillime % 10 ; # chiffre des millimes
if ($Millime >=5 ) 
	{
	$Pttc = int($Pttc*100+1)/100 ; 
	}
else
	{
	$Pttc = int($Pttc*100)/100 ; 
	}

print "\nLe prix TTC est $Pttc €\n"; 
# la présence du dollar force l'évaluation de la variable

#**********************************************#
# 		 alphanumérique		       #
#**********************************************#

$c1 = "Toto" ;
$c2 = "va à la plage";
print "\n$c1 $c2";

print "\n\nAu revoir";


