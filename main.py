from connection import Database, create
from functions import (
    add_flavor, 
    view_flavors, 
    delete_flavor,
    add_ingredient, 
    view_ingredients, 
    delete_ingredient,
    add_suggestion, 
    view_suggestions,
    delete_suggestion
)

def main():
    db_path = '/yourPath/yourDatabase.db' 
    with Database(db_path) as con:
        create(con) 

    while True:
        print("\nWelcome to the Chocolate House!")
        print("1. Add Flavor")
        print("2. View Flavors")
        print("3. Delete Flavor")
        print("4. Add Ingredient")
        print("5. View Ingredients")
        print("6. Delete Ingredient")
        print("7. Add Suggestion")
        print("8. View Suggestions")
        print("9. Delete Suggestion")
        print("10. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter flavor name: ")
            seasonal = input("Is it seasonal? (yes/no): ").lower() == 'yes'
            add_flavor(name, seasonal)
            print("Flavor added.")

        elif choice == '2':
            flavors = view_flavors()
            print("Flavors:", flavors)

        elif choice == '3':
            flavor_id = int(input("Enter flavor ID to delete: "))
            delete_flavor(flavor_id)
            print("Flavor deleted.")

        elif choice == '4':
            name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            add_ingredient(name, quantity)
            print("Ingredient added.")

        elif choice == '5':
            ingredients = view_ingredients()
            print("Ingredients:", ingredients)

        elif choice == '6':
            ingredient_id = int(input("Enter ingredient ID to delete: "))
            delete_ingredient(ingredient_id)
            print("Ingredient deleted.")

        elif choice == '7':
            customer_name = input("Enter your name: ")
            flavor_suggestion = input("Enter flavor suggestion: ")
            allergy_concern = input("Enter any allergy concern: ")
            add_suggestion(customer_name, flavor_suggestion, allergy_concern)
            print("Suggestion added.")

        elif choice == '8':
            suggestions = view_suggestions()
            print("Suggestions:", suggestions)

        elif choice == '9':
            suggestion_id = int(input("Enter suggestion ID to delete: "))
            delete_suggestion(suggestion_id)
            print("Suggestion deleted.")

        elif choice == '10':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
