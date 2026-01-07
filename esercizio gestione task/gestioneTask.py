"""
    esercizio - gestione task 
    obbiettivo
    lo scopo di questo esercizio è di farti esercitare con alcuni concetti fondamentali del linguaggio Python, in particolare:
    
    dati task : descrizione, contesto, scadenza, ore, priorità, 
    
    - parametri variabili di funzione (*args)
    - parametri con nome variabile(**kwargs)
    - generatori e parola chiave yeld
    - lettura e scrittura di file
    - gestione degli errori con try/except
    
    descrizione del problema
    realizzare un piccolo sistema di gestione task.
    il programma deve permettere di:
    - salvare una lista di attività su file
    - leggere le attività dal file una alla volta usando un generatore
    - gestire eventuali errori che possono verificarsi durante la lettura/scrittura del file
"""

import os
from datetime import datetime, date

def openFile(relPath, modalitaApertura):
    try:
        scriptDir = os.path.dirname(__file__)
        absFilePath = os.path.join(scriptDir, relPath)
        return open(absFilePath, modalitaApertura)
    except IOError as e:
        print(f"Errore nell'apertura del file per la scrittura: {e}")
        return None

def sceltaUtente():
    try:
        return int(input("Scegli un'opzione: (1) Aggiungi Task, (2) Leggi Task, (3) Rimuovi Task, (4) Esci: "))
    except ValueError as e:
        print("Input non valido. Per favore inserisci un numero.")
        return -1

def addTaskToFile(file, **kwargs):
    try:
        descrizione = kwargs.get("descrizione", "")
        contesto = kwargs.get("contesto", "")
        scadenza = kwargs.get("scadenza", date.today())
        ore = kwargs.get("ore", 0)
        priorita = kwargs.get("priorita", 0)
        
        taskLine = f"{descrizione},{contesto},{scadenza},{ore},{priorita}\n"
        file.write(taskLine)
    except Exception as e:
        print(f"Errore durante l'aggiunta del task: {e}")

def insertTask(file):
    descrizione = input("Inserisci la descrizione del task: ")
    contesto = input("Inserisci il contesto del task: ")
    try:
        scadenza = datetime.strptime(input("Inserisci la scadenza (YYYY-MM-DD): "), "%Y-%m-%d").date()
    except ValueError as e:
        print(f"Input non valido: {e}")
        return
    try:
        ore = float(input("Inserisci le ore stimate per il task: "))
    except ValueError as e:
        print(f"Input non valido: {e}")
        return
    try:
        priorita = int(input("Inserisci la priorità del task (1-5): "))
    except ValueError as e:
        print(f"Input non valido: {e}")
        return
    
    addTaskToFile(file, descrizione = descrizione, contesto = contesto, scadenza = scadenza, ore = ore, priorita = priorita)

def readTasksFromFile(file):
    try:
        for line in file:
            descrizione, contesto, scadenza, ore, priorita = line.strip().split(",")
            yield {
                "descrizione": descrizione,
                "contesto": contesto,
                "scadenza": scadenza,
                "ore": float(ore),
                "priorita": int(priorita)
            }
    except Exception as e:
        print(f"Errore durante la lettura dei task: {e}")

def printTaskFromFile(file):
    try:
        tasks = list(readTasksFromFile(file))
        for task in tasks:
            print(task)
    except Exception as e:
        print(f"Errore durante il salvataggio dei task: {e}")

def saveTasksToFile(tasks):
    try:
        file = openFile("tasklist.txt", "w")
        for task in tasks:
            taskLine = f"{task['descrizione']},{task['contesto']},{task['scadenza']},{task['ore']},{task['priorita']}\n"
            file.write(taskLine)
        file.close()
    except Exception as e:
        print(f"Errore nel salvataggio dei task: {e}")

def removeTaskFromFile(file):
    try:
        tasks = list(readTasksFromFile(file))
        for task in tasks:
            print(task)
        taskIndex = int(input("Inserisci l'indice del task da rimuovere: "))
        tasks.pop(taskIndex)
        saveTasksToFile(tasks)
        print("Task rimosso con successo.")
    except Exception as e:
        print(f"Errore durante la rimozione del task: {e}")

if __name__ == "__main__":
    print("Gestione Task")
    relPath = "taskList.txt"
    while True:
        scelta = sceltaUtente()
        if scelta == 4:
            print("Uscita dal programma.")
            break
        elif scelta == 1:
            file = openFile(relPath, "a")
            insertTask(file)
            file.close()
        elif scelta == 2:
            file = openFile(relPath, "r")
            printTaskFromFile(file)
            file.close()
        elif scelta == 3:
            file = openFile(relPath, "r")
            removeTaskFromFile(file)
            file.close()