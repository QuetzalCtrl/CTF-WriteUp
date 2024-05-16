# Légende

***404 CTF WriteUp | ### Renseignement en sources ouvertes - Introduction***

## Énoncé

*Sur cette photo, une des premières légendes du ski français s'apprête à franchir la ligne d'arrivée et remporter son troisième titre de champion du monde cette année. Saurez-vous retrouver son nom et prénom ainsi que le nom de la ville dans laquelle ces compétitions ont eu lieu ?*

***Format du flag** : 404CTF{jean-michel-dupont_tokyo}*

Le fichier `photo.png` nous est fourni *(dispo sur le git)*. Voici à quoi il ressemble :

![photo](photo.png)

## Sacré palmarès

Basons les débuts de nos recherches sur cette image, et voyons ce que *Google Lens* a à nous dire : 

![reverse image search](reverse-image-search.png)

Pas mal de sites qui parlent de ski, mais aucun lien direct avec un championnat du monde, ou d'un français triplement médaillé. Changement de stratégie : vu la description de son palmarès, il serait peut-être plus pertinent de le rechercher directement dans la liste des champions du monde de ski. Direction [Wikipédia](https://fr.wikipedia.org/wiki/Championnats_du_monde_de_ski_alpin), qui nous a gentiment répertorié le palmarès hommes des champions de ski.

![palmares](palmares.png)

Pas besoin de chercher plus loin, le premier nom qui corresponds à nos 2 critères (triplé + français) est *Émile Allais*. Il a réalisé cette performance en 1937.

![chamonix](chamonix.png)

Le lieu de chaque édition des championnats est également indiqué sur cette même page. La ville est donc Chamonix. 

## Récupération du flag

On a tout ce qu'il faut pour former notre flag : *Emile Allais à Chamonix*.
 
Flag : `404CTF{emile-allais_chamonix}`


