names = ['Tom', 'Gin', 'Sara', 'Tim']
surmanes = ['Smith', 'Doe', 'Black', 'White']
ages = [20, 30, 40, 50]

contacts = []

for name, surname, age in zip(names, surnames,ages):
    contacts.append({'nome': name, 'cognome':surname, 'eta': age})

print(contacts)