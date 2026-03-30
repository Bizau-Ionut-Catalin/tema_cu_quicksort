import json
def incarca_date(fisier):
    try:
        with open(fisier, 'r') as f:
            return json.load(f)
    except:
        print("Eroare la citirea fișierului.")
        return []
def compara(a, b):
    # punctaj descrescător
    if a["punctaj"] != b["punctaj"]:
        return a["punctaj"] > b["punctaj"]
    # timp crescător
    if a["timp"] != b["timp"]:
        return a["timp"] < b["timp"]
    # nume alfabetic
    return a["nume"] < b["nume"]
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]
    stanga = []
    dreapta = []

    for elem in lista[1:]:
        if compara(elem, pivot):
            stanga.append(elem)
        else:
            dreapta.append(elem)

    return quicksort(stanga) + [pivot] + quicksort(dreapta)

def afisare(lista):
    if not lista:
        print("Lista este goală.")
        return

    print(f"{'Nume':20} {'Punctaj':10} {'Timp':5}")
    for c in lista:
        print(f"{c['nume']:20} {c['punctaj']:10} {c['timp']:5}")

def adauga(lista):
    nume = input("Nume: ").strip()
    if not nume:
        print("Numele nu poate fi gol!")
        return

    try:
        punctaj = int(input("Punctaj: "))
        timp = int(input("Timp: "))
    except:
        print("Date invalide!")
        return

    lista.append({
        "nume": nume,
        "punctaj": punctaj,
        "timp": timp
    })
    print("Competitor adăugat.")

def actualizeaza(lista):
    nume = input("Numele competitorului: ")

    for c in lista:
        if c["nume"].lower() == nume.lower():
            try:
                c["punctaj"] = int(input("Nou punctaj: "))
                c["timp"] = int(input("Nou timp: "))
                print("Actualizare realizată.")
            except:
                print("Date invalide.")
            return

    print("Competitor inexistent!")

def clasament(lista):
    if not lista:
        print("Lista este goală.")
        return

    sortata = quicksort(lista)

    print(f"{'Loc':5} {'Nume':20} {'Punctaj':10} {'Timp':5}")

    loc = 1
    for i in range(len(sortata)):
        if i > 0:
            prev = sortata[i - 1]
            curent = sortata[i]

            if (prev["punctaj"], prev["timp"]) != (curent["punctaj"], curent["timp"]):
                loc = i + 1

        print(f"{loc:<5} {sortata[i]['nume']:20} {sortata[i]['punctaj']:10} {sortata[i]['timp']:5}")

def statistici(lista):
    if not lista:
        print("Lista este goală.")
        return

    punctaje = [c["punctaj"] for c in lista]
    timpi = [c["timp"] for c in lista]

    print("Statistici:")
    print("Număr competitori:", len(lista))
    print("Punctaj maxim:", max(punctaje))
    print("Punctaj minim:", min(punctaje))
    print("Media punctajelor:", sum(punctaje) / len(lista))
    print("Cel mai bun timp:", min(timpi))

def meniu():
    lista = incarca_date("competitori.json")

    while True:
        print("\n--- MENIU ---")
        print("1. Afișare competitori")
        print("2. Adăugare competitor")
        print("3. Actualizare competitor")
        print("4. Sortare (Quicksort)")
        print("5. Clasament")
        print("6. Statistici")
        print("0. Ieșire")

        opt = input("Alege opțiunea: ")

        if opt == "1":
            afisare(lista)
        elif opt == "2":
            adauga(lista)
        elif opt == "3":
            actualizeaza(lista)
        elif opt == "4":
            lista = quicksort(lista)
            print("Lista sortată.")
        elif opt == "5":
            clasament(lista)
        elif opt == "6":
            statistici(lista)
        elif opt == "0":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă!")

if __name__ == "__main__":
    meniu()
