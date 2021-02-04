#**********************************************#
# Premiers essais en Perl de Guillaume Bourlet #
# Auteur : Guillaume Bourlet                   #
# Date 22/08/2010			       #
# Boucles		                       #
#**********************************************#

# Affichage de la table de 7

print "\n\nAffichage de la table de 7 avec une boucle for";
for ($c= 1 ; $c<=10 ; $c++)
	{
	print "\n$c x 7 = " , $c*7;
	}

print "\n\nAffichage de la table de 7 avec une boucle while";
$c=1;
while ($c<=10)
	{
	print "\n$c x 7 = " , $c*7;
	$c++;
	}

print "\n\nAffichage de la table de 7 avec une boucle until";
$c=1;
until ($c==11)
	{
	print "\n$c x 7 = " , $c*7;
	$c++;
	}

# raccourcis du Perl :
print "\n\nAffichage de la table de 7 avec des raccourcis";
print "\n$_ x 7 = " , $_*7 for (1..10);
# $_ est la variable magique, Perl la comprend dans le contexte

print "\n\n";

$c=0;
print "\n$c x 7 = " , $c*7 while ($c++<10);
# attention, bien que while arrive en fin d'insctruction, la condition est évaluée avant

print "\n\nAu revoir\n\n";


