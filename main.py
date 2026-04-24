import json
import os
from datetime import datetime

# Numele fisierului pentru stocare
DATA_FILE = "expenses.json"

def load_expenses():
    """Incarca cheltuielile din fisierul JSON."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_expenses(expenses):
    """Salveaza cheltuielile in fisierul JSON."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Adauga o cheltuiala noua."""
    try:
        amount = float(input("Introdu suma: "))
        category = input("Introdu categoria (mancare, transport, etc.): ")
        date = input("Introdu data (ZZ-LL-AAAA) sau apasa Enter pentru azi: ")
        
        if not date:
            date = datetime.now().strftime("%d-%m-%Y")
            
        expense = {
            "suma": amount,
            "categorie": category,
            "data": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        print(" Cheltuiala adaugata cu succes!")
    except ValueError:
        print(" Suma invalida. Te rog introdu un numar.")

def view_expenses(expenses):
    """Afiseaza toate cheltuielile."""
    if not expenses:
        print(" Nu exista cheltuieli inregistrate.")
        return
    
    print("\n--- Lista Cheltuieli ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['data']} | {exp['categorie']} | {exp['suma']} RON")
    print("------------------------")

def calculate_total(expenses):
    """Calculeaza totalul."""
    total = sum(float(exp.get('suma', 0)) for exp in expenses)
    print(f"\n Total cheltuit: {total:.2f} RON")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n- Manager Cheltuieli Personale -")
        print("1. Adauga cheltuiala")
        print("2. Vezi cheltuieli")
        print("3. Calculeaza total")
        print("4. Iesire")
        
        choice = input("Alege o optiune (1-4): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            calculate_total(expenses)
        elif choice == '4':
            print("La revedere!")
            break
        else:
            print(" Optiune invalida.")

if __name__ == "__main__":
    main()