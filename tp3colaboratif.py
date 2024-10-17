import random
import json

def choisir_difficulte():
    while True:
        difficulte = input("Choisissez la difficulté (facile, moyen, difficile) : ").lower()
        if difficulte in ["facile", "moyen", "difficile"]:
            return difficulte
        else:
            print("Difficulté invalide. Veuillez réessayer.")

def generer_nombre_secret(difficulte):
    if difficulte == "facile":
        max_nombre = 50
    elif difficulte == "difficile":
        max_nombre = 200
    else:
        max_nombre = 100
    return random.randint(1, max_nombre)

def enregistrer_score(nom_joueur, score, difficulte):
    try:
        with open("scores.json", "r") as f:
            score_data = json.load(f)
    except FileNotFoundError:
        score_data = {"facile": [], "moyen": [], "difficile": []} # Adapter les clés

    score_data[difficulte].append({"joueur": nom_joueur, "score": score})

    with open("scores.json", "w") as f:
        json.dump(score_data, f, indent=4)

def get_best_score(difficulty):
    try:
        with open("scores.json", "r") as f:
            score_data = json.load(f)
        if score_data and score_data[difficulty]:
            meilleur_score = min(score_data[difficulty], key=lambda x: x["score"])
            return f"Meilleur score (niveau {difficulty}) : {meilleur_score['joueur']} avec {meilleur_score['score']} tentatives."
        else:
            return "Aucun score enregistré pour ce niveau."
    except FileNotFoundError:
        return "Aucun score enregistré."


difficulte = choisir_difficulte()
secret_number = generer_nombre_secret(difficulte)
guess = None
attempts = 0



while guess != secret_number:
    try:  # Gestion des erreurs pour les entrées non numériques
        guess = int(input(f"Devinez le nombre secret (entre 1 et {max_nombre}): "))
        attempts += 1

        if guess < secret_number:
            print("Trop bas ! Réessayez.")
        elif guess > secret_number:
            print("Trop haut ! Réessayez.")
        else:
            print(f"Félicitations ! Vous avez deviné le nombre : {secret_number}")
            print(f"nombre de tentatives: {attempts}")
            nom_joueur = input("Entrez votre nom (facultatif): ")
            enregistrer_score(nom_joueur, attempts, difficulte)
            print(get_best_score(difficulte))
            break

    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")