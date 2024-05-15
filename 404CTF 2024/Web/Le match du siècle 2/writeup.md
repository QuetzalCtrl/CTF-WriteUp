# Le match du siècle [2/2]

***404 CTF WriteUp | Web - Moyen***

## Énoncé

*Vous avez déjà en votre possession un billet, néanmoins, pour impressionner votre famille, vous souhaiteriez des places VIP.*


Bon, nous voilà de retour sur notre site préféré, **[https://exploit-mag.challenges.404ctf.fr](https://exploit-mag.challenges.404ctf.fr)**. Comme indiqué dans l'énoncé, cette fois-ci ce sont les tickets VIP qui nous intéressent. Cette catégorie de billet est épuisé et n'est plus dispo à la vente, il ne va donc sûrement pas s'agir de modifier notre solde pour cette fois.

![page accueil](home-page.png)

## Il y avait un autre token, non ?

Rapelez-vous, dans la première partie de ce challenge, nous avions modifié notre solde grâce à un token de session *balance*. Mais ce n'était pas le seul token présent :  

![token](token.png)

Lorsqu'on se connecte, 2 tokens sont créés, penchons-nous sur ce 2e token :

```
token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlRlc3RldXV1dXV1MSIsImJpbGxldHMiOnsiVklQIjowLCJMYXRlcmFsZSI6MSwiRmFtaWxpYWxlIjowLCJFc3QiOjAsIk91ZXN0IjowLCJOb3JkIGV0IFN1ZCI6MH0sImlhdCI6MTcxNTY3MzUwNX0.tHzu2Sw9Bf_aHZfS6lzLrRd2-4xSVSE7pl7dA-vcKOQ
```

Vu le format, c'est clairement un [JWT](https://datatracker.ietf.org/doc/html/rfc7519) (JSON Web Token), utilisons le super site https://jwt.io/ pour le décoder: 

![jwt](jwt.png)

Le token semble stocker pas mal d'informations relatives à l'utilisateur, son nombre de billets y compris ! Essayons de modifier notre token à notre avantage, en changeant la valeur du billet VIP dans notre payload. 
Problème: l'application utilise des tokens signés en HS256, et il nous est impossible de créer ces mêmes tokens sans connaître la signature secrète utilisée. 
Il y a cependant 2 moyens de pallier à ce problème : 
- Bruteforcer la signature du JWT
- Essayer le None Algorithm (voir [l'article de PortSwigger](https://portswigger.net/kb/issues/00200901_jwt-none-algorithm-supported)) 

Dans le cadre de ce CTF, tout bruteforce est prohibé, on va donc tester si le serveur est vulnérable aux JWTs sans signature.  

## Création d'un nouveau token

Un JWT, c'est 3 parties différentes (*Header*, *Payload* et *Signature*) séparés par des points, et encodés en Base64. Avec l'algorithme *none*, aucune signature n'est nécessaire, nous n'avons donc besoin d'encoder quel le header et le payload souhaité, et de les séparer par un point : 
```bash
$ echo -n '{"typ": "JWT","alg": "none"}' | base64
eyJ0eXAiOiAiSldUIiwiYWxnIjogIm5vbmUifQ==
$ echo -n '{"username": "Testeuuuuuu1","billets": {"VIP": 1,"Laterale": 1,"Familiale": 0,"Est": 0,"Ouest": 0,"Nord et Sud": 0},"iat": 1715673505}' | base64 -i
eyJ1c2VybmFtZSI6ICJUZXN0ZXV1dXV1dTEiLCJiaWxsZXRzIjogeyJWSVAiOiAxLCJMYXRlcmFs
ZSI6IDEsIkZhbWlsaWFsZSI6IDAsIkVzdCI6IDAsIk91ZXN0IjogMCwiTm9yZCBldCBTdWQiOiAw
fSwiaWF0IjogMTcxNTY3MzUwNX0=

# Pas besoin de garder le padding (charactère '=' en b64) pour le format JWT, notre token modifé ressemble donc à ça : 
eyJ0eXAiOiAiSldUIiwiYWxnIjogIm5vbmUifQ.eyJ1c2VybmFtZSI6ICJUZXN0ZXV1dXV1dTEiLCJiaWxsZXRzIjogeyJWSVAiOiAxLCJMYXRlcmFs
ZSI6IDEsIkZhbWlsaWFsZSI6IDAsIkVzdCI6IDAsIk91ZXN0IjogMCwiTm9yZCBldCBTdWQiOiAw
fSwiaWF0IjogMTcxNTY3MzUwNX0.
``` 

> **Note :** n'oubliez pas le dernier point après la partie *payload*, car même si il n'y a pas de *signature*, il est important de respecter le format JWT imposé pour avoir un token valide. 

Vérifions rapidement notre nouveau token sur JWT.io :

![new jwt](new-jwt.png)

Tout est ok, il n'y a plus qu'à remplacer notre JWT par ce nouveau token : 

![denied](denied.png)

Il semblerai que nous sommes sur la bonne piste, mais qu'une forme de protection a été mise en place. Cette protection nous bloque l'accès au endpoint pour récupérer nos billets (le bouton *Obtenir*), il nous reste encore à savoir si ce endpont a lui aussi une protection ou si la *seule* protection est d'empêcher l'utilisateur d'accéder au endpoint depuis l'application web. 

En se reconnectant, notre JWT est réinitialisé, ce qui nous permets d'avoir de nouveau accès à la page */billets*. Il est temps de sortir BurpSuite pour mieux comprendre ! Voici donc ce qu'il se passe quand on clique sur *Obtenir* :

![api](api.png)

Intéressant, un *POST* vers une API est fait, voyons comment celle-ci se comporte avec notre JWT modifié !
 
## Récupération du flag

L'idée est de proxifier notre *POST* vers l'API, pour lui demander un billet VIP, et en lui confirmant qu'on a bien le droit de le demander en lui passant notre JWT modifié dans la même requête.
Dans BurpSuite, on intercepte le *POST*, puis on remplace le *body* de la requête `{"token":"Laterale"}` par `{"token":"VIP"}`. Il ne reste plus qu'à remplacer la valeur du `Cookie` (dans le header de notre requête) par notre *None Alg. token*, dans mon cas : 
`Cookie: token= eyJ0eXAiOiAiSldUIiwiYWxnIjogIm5vbmUifQ.eyJ1c2VybmFtZSI6ICJUZXN0ZXV1dXV1dTEiLCJiaWxsZXRzIjogeyJWSVAiOiAxLCJMYXRlcmFs
ZSI6IDEsIkZhbWlsaWFsZSI6IDAsIkVzdCI6IDAsIk91ZXN0IjogMCwiTm9yZCBldCBTdWQiOiAw
fSwiaWF0IjogMTcxNTY3MzUwNX0.;`

On envoie la requête... Et hop ! Le fichier *flag.png* se télécharge, avec notre nouveau flag en clair dedans :)

Flag : `404CTF{b7554ee60d0020216749d428830a55f1}`


