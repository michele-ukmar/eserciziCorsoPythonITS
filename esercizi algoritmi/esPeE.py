"""controllo password lunga almeno 8 caratteri, almeno un carattere maiuscolo alfanumerica e un carattere speciale e avere numero finale
controllo email valido con espressione regolare deve contenere @, il dominio dela mail alla fine della stringa, il dominio preceduto da un punto. e dopo devono esserci almeno due caratteri
i simboli iniziali possono essere _%+-. lettere e numeri
"""
import string

def controllo_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_special = False
    hasFinalNumber = password[-1].isdigit()

    for char in password:
        if char.isupper():
            has_upper = True
        if char in string.punctuation:
            has_special = True

    return has_upper and has_special and hasFinalNumber

def controllo_email(email):
    import re
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    password = input("Inserisci una password: ")
    if controllo_password(password):
        print("Password valida")
    else:
        print("Password non valida")
    email = input("Inserisci una email: ")
    if controllo_email(email):
        print("Email valida")
    else:
        print("Email non valida")

