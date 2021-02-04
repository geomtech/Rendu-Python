#**********************************************#
# Premiers essais en Perl de Guillaume Bourlet #
# Auteur : Guillaume Bourlet                   #
# Date 10/08/2010                              #
# Fonctions de chaines			       #
#**********************************************#

$P1 = "Toto va à la plage" ;

# length : la longueur d'une chaine
print "\n\nlength donne la longueur d'une chaine";
print "\nLa chaine \"$P1\" contient " , length($P1) , " caractères";

# chop : suppression du dernier caractère
print "\n\nchop supprime le dernier caractère et le retourne";
$temp = $P1; # copie
$dernier = chop($temp);
print "\nLe dernier caractère de \"$P1\" est $dernier";
print "\nLa chaine \"$P1\" tronquée est $temp"; 

# chomp : supprime le dernier caractère d'une chaine uniquement si c'est un retour à la ligne
# \n sous Unix et \n\r sous Windows
print "\n\nchomp supprime le dernier caractère d'une chaine uniquement si c'est un retour à la ligne";
$P2 = "Toto va à la plage\n" ;
$P3 = "Toto va à la plages" ;
chomp($P2);chomp($P3);
if ($P1 eq $P2)
	{ print "\nchomp a bien fonctionné";}
if ($P1 ne $P3)
	{ print "\nchomp a bien fonctionné";}

# répétition (déjà vu), l'opérateur x répète une chaine
$P5 = "kikou";
$P6 = $P5 x 5 ;
print "\n\n$P6"; #affiche kikoukikoukikoukikoukikou




print "\n\nAu revoir";


