from .models import AddressBook, Record, Name, Phone, Birthday
from .storage import load_data, save_data, DEFAULT_FILE

class App:
    def __init__(self):
        self.book = load_data(DEFAULT_FILE)

    def add(self, name: str, phone: str):
        rec = self.book.find(name)
        if rec:
            rec.add_phone(Phone(phone))
        else:
            rec = Record(Name(name), [Phone(phone)])
            self.book.add_record(rec)
        print(f"OK: {rec}")

    def show(self, name: str):
        rec = self.book.find(name)
        print(rec if rec else "Not found")

    def delete(self, name: str):
        print("Deleted" if self.book.delete(name) else "Not found")

def main():
    app = App()
    print("AddressBook loaded.\nType 'help' to see commands, 'exit' to quit.")
    try:
        while True:
            cmd = input("> ").strip()
            if cmd in ("exit", "quit"):
                break
            if cmd.startswith("add "):
                _, name, phone = cmd.split(maxsplit=2)
                app.add(name, phone)
            elif cmd.startswith("show "):
                _, name = cmd.split(maxsplit=1)
                app.show(name)
            elif cmd.startswith("del "):
                _, name = cmd.split(maxsplit=1)
                app.delete(name)
            elif cmd == "help":
                print("add <name> <phone> | show <name> | del <name> | exit")
            else:
                print("Unknown command. Type 'help'.")
    finally:
        save_data(app.book, DEFAULT_FILE)
        print("Saved. Bye!")

if __name__ == "__main__":
     main()