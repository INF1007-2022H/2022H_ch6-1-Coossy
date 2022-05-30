#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pkgutil import iter_modules
from re import X


def order(values: list = None) -> list:
    lettre, nombre = [], []
    if values is None:
        values = []
        while len(values) != 10:
            valeur = input("Entrez une valeur :")
            values.append(valeur)

    for elem in values:
        if elem.isalpha():
            lettre.append(elem)
        else:
            nombre.append(float(elem))

    return sorted(nombre) + sorted(lettre)



def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        while len(words) != 2:
            mot = input("Entrez un mot : ")
            words.append(mot)
    
    return sorted(words[0]) == sorted(words[1])

    
def contains_doubles(items: list) -> bool:
    print(items)
    return len(set(items)) != len(items)
        
        
def best_grades(student_grades: dict) -> dict:
    Meilleur_étudiant = dict()
    for key, value in student_grades.items():
        moyenne = sum(value) / len(value)
        Meilleur_étudiant = { key : moyenne}
    return Meilleur_étudiant

    
def frequence(sentence: str) -> dict:
    dictionnaire = dict()
    for char in sentence:
        if (sentence.count(char)) > 5:
            dictionnaire[char] = sentence.count(char)
    
    return (sorted(dictionnaire, key=dictionnaire.__getitem__, reverse = True))

    


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    # print(f"On essaie d'ordonner les valeurs...")
    # print(order())

    #print(f"On vérifie les anagrammes...")
    #print(anagrams())

    #my_list = [3, 3, 5, 6, 1, 1]
    #print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
