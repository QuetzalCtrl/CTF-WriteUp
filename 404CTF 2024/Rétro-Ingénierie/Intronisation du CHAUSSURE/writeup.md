# Intronisation du CHAUSSURE

***404 CTF WriteUp | Rétro-Ingénierie - Facile***

## Énoncé

*Montrez votre valeur*

*Le CHAUSSURE, cette fameuse entité pionnière dans le domaine du sport de combat a ouvert un tournoi pour tous les chat-diateurs qui souhaiteraient se mesurer au reste du monde. Les présélections commencent et un premier défi a été publié par le CHAUSSURE. Ce dernier semble très cryptique, à vous d'en déceler les secrets!*

*Format de flag : `404CTF{mot-de-passe}`*

Le fichier `intronisation` nous est fourni *(dispo sur le git)*. 

## Décompilons tout ça !

Avant tout, un peu de collecte d'infos sur ce fichier : 

```
$ file intronisation
intronisation: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped

$ chmod +x intronisation && ./intronisation
Bienvenue, rétro-ingénieur en herbe!
Montre moi que tu es à la hauteur :
>>> test
Mauvaise réponse...
```

Qui dit reverse, dit *GHidra* ! Voici à quoi ressemble notre point d'entrée : 

```c
void processEntry entry(void)

{
  size_t sVar1;
  char local_28;
  char local_27;
  char local_26;
  char local_25;
  char local_24;
  char local_23;
  char local_22;
  char local_21;
  char local_20;
  char local_1f;
  char local_1e;
  char local_1d;
  char local_1c;
  
  syscall();
  syscall();
  sVar1 = _strlen(&local_28);
  if (((((sVar1 == 0xe) && (local_27 == 't')) && (local_21 == 'r')) &&
      ((((local_1e == '1' && (local_1d == 's')) &&
        ((local_23 == 'n' && ((local_24 == '1' && (local_26 == 'u')))))) && (local_28 == '5')))) &&
     ((((local_1f == 'n' && (local_1c == '3')) && (local_20 == '0')) &&
      ((local_25 == 'p' && (local_22 == 't')))))) {
    syscall();
  }
  else {
    syscall();
  }
  syscall();
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}
```

Parfait, en fait on n'a plus qu'à lire dans l'ordre la valeur de chaque variable :

```
  local_28 -> '5'
  local_27 -> 't'
  local_26 -> 'u'
  [...]
  local_1d -> 's'
  local_1c -> '3'
```

## Récupération du flag

Le mot de passe valide : `5tup1ntr0n1s3`

```bash
$ ./intronisation
Bienvenue, rétro-ingénieur en herbe!
Montre moi que tu es à la hauteur :
>>> 5tup1ntr0n1s3
Bravo !!!
```
 
Flag : `404CTF{5tup1ntr0n1s3}`


