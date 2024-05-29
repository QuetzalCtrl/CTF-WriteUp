# Twine

***NahamCon CTF WriteUp | Warmups - Easy***

## Énoncé

Google tells me that twine means: _"strong thread or string consisting of two or more strands of hemp, cotton, or nylon twisted together."_


**Download the file(s) below.**

**Attachments:** [twine.jpg](./twine.jpg)

## Strings rules

Par réflexe, quand je télécharge un fichier en CTF, je fais toujours les commandes `file` et `strings` pour savoir à quel fichier j'ai affaire. Ici, ça a payé apparemment :

```bash
$ strings twine.jpg | grep flag
flag{4ac54e3ba5f8f09049f3ad62403abb25}
```

## Récupération du flag
 
Flag : `flag{4ac54e3ba5f8f09049f3ad62403abb25}`


