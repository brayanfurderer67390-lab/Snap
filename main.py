#!/usr/bin/env python3
"""
Snapchat SS06 Appeal Helper
A small local helper for preparing an appeal when Snapchat reports SS06.
It does not bypass or remove Snapchat device bans.
"""

import webbrowser

SNAPCHAT_HELP = "https://help.snapchat.com/hc/fr-fr"
SNAPCHAT_LOGIN = "https://accounts.snapchat.com/"

def build_message():
    username = input("Nom d'utilisateur Snapchat : ").strip()
    email = input("E-mail associé au compte (facultatif) : ").strip()

    return f"""Objet : Demande de réexamen – appareil bloqué (SS06)

Bonjour l'équipe Snapchat,

Je rencontre le code d'assistance SS06 lors de la connexion à mon compte Snapchat.

Nom d'utilisateur : {username}
E-mail associé : {email or "Non renseigné"}

Je souhaite demander un réexamen de ce blocage. Si ce blocage résulte d'une erreur, pourriez-vous vérifier mon compte et mon appareil et m'indiquer la procédure à suivre pour retrouver l'accès ?

Je suis disponible pour fournir toute information nécessaire.

Merci pour votre aide.
Cordialement,
{username}
"""

def main():
    print("=" * 55)
    print("        Snapchat SS06 - Assistant d'appel")
    print("=" * 55)
    print()
    print("Ce programme prépare un message d'appel.")
    print("Il ne contourne pas le blocage SS06 et ne modifie pas Snapchat.")
    print()

    message = build_message()

    print("\n--- MESSAGE À COPIER ---\n")
    print(message)
    print("------------------------\n")

    choice = input("Ouvrir le centre d'aide Snapchat ? [O/n] ").strip().lower()
    if choice != "n":
        webbrowser.open(SNAPCHAT_HELP)

if __name__ == "__main__":
    main()
