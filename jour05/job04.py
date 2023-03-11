def caesar(msg="", clef=0):
    alphabet="abcdefghijklmnoprstuvwyz"
    chiffre=""

    for l in msg.lower():
        pos=alphabet.find(l)

        if pos != -1:
            chiffre+=alphabet[(pos+clef) % len(alphabet)]
        else:
                chiffre+=1
        return chiffre

message="SENATVS POPVLVSQVE ROMANVS"
chiffre = caesar(message, 5)
dechiffre = caesar(chiffre, -5)
print(message, "=>", chiffre, "=>", dechiffre)
