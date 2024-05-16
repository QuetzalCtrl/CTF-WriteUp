# L'absence

***404 CTF WriteUp | Stéganographie - Introduction***

## Énoncé

*Hier, Francis n'était pas là à son épreuve de barres asymétriques, il nous a envoyé une lettre d'excuse. Malheureusement, la fin de sa lettre est illisible.  
Déchiffrez la fin de ses excuses.*

Le fichier `lettre.txt` nous est fourni *(dispo sur le git)*. Voici ce qu'il contient :

```
bonsoir, désolé pour le déranGement. je n'ai pas pu Y aller hier pour l'épreuve de barres asyMétriques. désolé si je N'ai pas été à lA hauteur de voS attenTes, je feraIs mieux aux épreuves publiQUes de dEmain. 


bises.
franciS vigenere.

ps :
Kl qsfwm, r'qc hm s'ynfefmmh wej rc peahxik xi eg lmgigg i uni voqevmmem fuv vkq srnk jcy psmryurnl yiyli hkppee ehv fuck ! Syuf ahkmi orw rmztuw kmsbijifq, w'aa xvvcr ha jq eelkwkpij. Rc hbiub : 404KJZ{RwBmxrzHtaBywVxybramqAlj}
```

## Analyse du texte

Quelques indices nous saute aux yeux : 
- Le nom de famille *vigenere*, qui n'est sûrement pas ici par hasard (voir [le chiffrement de Vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re))
- Des lettres en majuscule réparties dans toute la première partie lisible du message
- Le format de flag reconnaissable, les chiffres et les crochets n'étant visiblement pas concernés par l'encodage

En résumé, nous devons déchiffrer `404KJZ{RwBmxrzHtaBywVxybramqAlj}`, en utilisant le chiffrement de Vigenère. Pour cela, une clé secrète est nécessaire. 

Et si cette clé avait un lien avec les majuscules dont nous parlions précédemment ? Lorsqu'on isole les lettres, on obtiens le mot suivant : `GYMNASTIQUES`. Cela pourrait tout à fait correspondre à notre clé, vérifions... 

## Récupération du flag

 Allons faire un tour sur le site [CyberChef](https://gchq.github.io/CyberChef/), On rajoute *Vigenère Decode* en *Recipe*, on lui fourni la clé et le message chiffré en input, voilà :)
 
Flag : `404CTF{NeVolezPasLesDrapeauxSvp}`


