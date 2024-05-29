# Base3200

***NahamCon CTF WriteUp | Scripting - Easy***

## Énoncé

You know what to do.  
  
**Download the file(s) below.**

**Attachments:** [theflag.xz](./theflag.xz)

## 3200, c'est 64 x 50 :)

```python
# code from https://gist.github.com/intrd/c63db7bd3d0951f0653d6fdf7ea169d6       
                                       
import base64

pontfile = 'theflag'

# Read the content of the file once
with open(pontfile, 'r') as f:
    content = f.read()

# Decode the content 50 times
for _ in range(50):
    content = base64.b64decode(content)

# Write the decoded content back to the file
with open(pontfile, 'wb') as f:
    f.write(content)
```

## Récupération du flag

```bash
$ xz -d theflag.xz # décompresser l'archive
$ python3 base3200.py # corresponds au script ci-dessus 
$ cat theflag
flag{340ff1bee05244546c91dea53fba7642}
```
 
Flag : `flag{340ff1bee05244546c91dea53fba7642}`


