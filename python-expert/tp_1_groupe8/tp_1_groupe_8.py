# GROUPE 8 : MADEC Salman Ali; CHENNAF Ianis; SAMAALI Mohamed Amine; OMRANE Sadek; BELKASSEH Alae

# 1, 2




def replaceLetterByFrequency(word, charToReplace):

    letterFreq = {}  # initialisation d'un dictionnaire qui va stocké la fréquence des lettres
    # boucle pour parcourir le mot
    for letter in word:
        if letter.isalpha():  # check si la lettre est bien alphabétique et ajout au dictio
            letterFreq[letter] = letterFreq.get(letter, 0) + 1

    # relever la lettre qui à la fréquence la plus élevée
    maxFreq = max(letterFreq.values())

    finaleWord = ''
    for letter in word:
        # check de la fréquence max
        if letter.isalpha() and letterFreq[letter] == maxFreq:
            # Ajout du caractère spécifé "CharToReplace" à la variable "finalWord"
            finaleWord += charToReplace
        else:
            finaleWord += letter

    return finaleWord, letterFreq


initialWord = "Mississippi"
replaceLetter = "e"  

updatedWord, frequence = replaceLetterByFrequency(initialWord, replaceLetter)

# Affichage finale
print("Mot initiale : ", initialWord, ", mot modifié :", updatedWord)
print("Fréquence des lettres :", frequence)


# 3

text = """
Je vois là-bas un être sans tête qui grimpe à une perche sans fin.

Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement
soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment
grimpe, et s'en va grimpant sur son terrible chemin vertical.

Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une
position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours.

Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter
et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas.

Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace
lui doive être plus haïssable encore.

Henri Michaux
"""
wordToCount = " le "
charToCount = "e"
wordToReplace = " "

# compteur des différentes variables spécifiés
nbLe = text.lower().count(wordToCount)
nbE = text.lower().count(charToCount)

# Remplace toutes les occurrences du pronom par le mot de remplacement
finalText = text.replace(wordToCount, wordToReplace)

# Affichage finale
print(f"Nombre d'occurrences du pronom {wordToCount}: {nbLe}")
print(f"Nombre de lettres 'e': {nbE}")
print(f"\nTexte sans le pronom {wordToCount}:\n", finalText)


# 4
import json

def countPronounsAndE(texte, charCount):
    pronouns = ["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"]

    # Compte le nombre d'occurrences de chaque pronom dans le texte
    countPronouns = {pronom: texte.lower().count(pronom)
                     for pronom in pronouns}
    # Ajoute le nombre d'occurrences de la lettre spécifiée dans le texte
    countPronouns["nombre_e"] = texte.lower().count(charCount)

    return countPronouns


characterCount = "e"

if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as file:  # lecture d'un fichier en read
        text = file.read()

    # Appel de la fonction pour compter les pronoms et la lettre spécifiée
    resultats = countPronounsAndE(text, characterCount)

    path = "pronouns.json"

    # Enregistre les résultats dans un fichier JSON avec une mise en forme lisible
    with open(path, "w", encoding="utf-8") as fileJson:
        json.dump(resultats, fileJson, indent=4)

    # Affichage finale
    print(f"Résultat stocké dans '{path}'.")
