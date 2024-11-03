def main():
    phonebook = Phonebook()



class Phonebook:
    def __init__(self, contacts=[]):
        self.contacts = contacts
        self.menu()

    def add_contact(self):
        try:
            name, phone= input("Type contact name, phone number: ").strip().split(",")
            if name or phone:
                self.contacts.append({name: phone})
                print("Contact added")
        except: 
            print("invalid input")

    def search_contacts(self):
        contact_name = input("Type a name of your contact: ")
        for contact in self.contacts:
            if contact_name in contact:
                print(contact[contact_name])
                break
        else:
            print("Contact doesn't exist")
  


    def remove_contacts(self):
        removal = input("Type a name of contact you want to remove: ")
        for i, contact in enumerate(self.contacts):
            if contact[removal]:
                removed = self.contacts.pop(i)
                print(f"{removed[0]} {removed[1]} sucesfully deleted from phonebook")
    
    def menu(self, using=True):
        print("Welcome to Phonebook!\nWhat would you like to do?")
        print("Type add if you want to add new contact")
        print("Type remove if you want to remove existing contact")
        print("Type search if you want to search your contacts")
        print("Type q if you want to leave")
        while using:
            try:
                answer = input(": ").lower().strip()
                if answer == "add":
                    self.add_contact()
                    continue
                elif answer == "remove":
                    self.remove_contacts()
                    continue
                elif answer == "search":
                    self.search_contacts()
                    continue
                elif answer == "q":
                    using == False
                    break
                else:
                    print("invalid action key")
                    continue
            except Exception:
                using == False





if __name__ == "__main__":
    main()