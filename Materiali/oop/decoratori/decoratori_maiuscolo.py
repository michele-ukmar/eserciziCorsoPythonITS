from functools import wraps

def caps_lock(funzione_parametro):
    @wraps(funzione_parametro)
    def wrapper(*args, **kwargs):
        """ wrapper significa 'incarto, confezione' """
        result = ""
        for arg in args:
            result += arg
        for arg in kwargs.values():
            result += arg
        return funzione_parametro(result).upper()
    return wrapper

@caps_lock
def echo(msg):
    return msg

print(echo("Esempio"," ",decoratore="Di Decoratore ",con="con kwargs*!"))
# ESEMPIO DI DECORATORE CON KWARGS*!

print(echo("Esempio di decoratore con kwargs*!"))
# ESEMPIO DI DECORATORE CON KWARGS*!