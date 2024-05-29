# That's Not My Base

***NahamCon CTF WriteUp | Warmups - Easy***

## Énoncé

*Everyone knows about [Base64](https://en.wikipedia.org/wiki/Base64), but do you know about this one?*

_(Remember, the flag format starts with `flag{`!)_

**`F#S<YRXdP0Fd=,%J4c$Ph7XV(gF/*]%C4B<qlH+%3xGHo)\`**

## Une base, mais laquelle ?

Bon, vu le titre du challenge, il s'agit de trouver dans quelle *Base* le flag a été encodé. En recherchant comment faire pour décoder un message dans le plus de bases possible en python, je suis tombé sur [cet outil](https://github.com/mufeedvh/basecrack). Un simple `git clone`, et l'outil va s'occuper du reste :)

```bash
$ python3 basecrack.py

██████╗  █████╗ ███████╗███████╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██████╔╝███████║███████╗█████╗  ██║     ██████╔╝███████║██║     █████╔╝
██╔══██╗██╔══██║╚════██║██╔══╝  ██║     ██╔══██╗██╔══██║██║     ██╔═██╗
██████╔╝██║  ██║███████║███████╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ v4.0

                python basecrack.py -h [FOR HELP]

[>] Enter Encoded Base: F#S<YRXdP0Fd=,%J4c$Ph7XV(gF/*]%C4B<qlH+%3xGHo)\

[>] Decoding as Base92: flag{784454a9509196a33dba242c423c057a}

[-] The Encoding Scheme Is Base92
```

## Récupération du flag
 
Flag : `flag{784454a9509196a33dba242c423c057a}`


