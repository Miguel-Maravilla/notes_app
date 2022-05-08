
import notes.note as model




class Actions:

    def create(self, user):
        print(f"\nOk {user[1]}, Let's create a new Note!!")
        
        title = input("Introduce the title of your note: ")
        description = input("Introduce the content of your note: ")
        
        note = model.Note(user[0], title, description)
        to_save = note.to_save()

        if to_save[0] >= 1:
            print(f"\nGreat! You've saved the note: {note.title}") #Access to the "title property" of the Notes object
        else:
            print(f"Sorry, note hasn't been saved {user[1]}")

    def show(self, user): # is the user of the nextactions() formula
        print(f"\nOk, {user[1]}, These are your notes: ")

        note = model.Note(user[0], "", "") # We create an object (instance of the "Note" class), but the last two parameters (title and descroiption) are not necessary in this case. We could make them optonal, but I want to see where they come from
        notes = note.to_list() #This return as a  type_list, all your notes

        for note in notes:
            print("\n**************************")
            print(f"Title: {note[2]}")
            print(note[3])
            print("**************************")

    
    def delete(self, user):
        print(f"\nOk {user[1]} let's delete data")
        
        title = input("Introduce the title of the note to delete: ")
        note = model.Note(user[0], title, "")
        delete = note.to_delete()

        if delete[0] >= 1: # Si me ha modificado una fila
            print(f"We've deleted the note: {note.title}")
        
        else:
            print("Note hasn't been deleted, please try later")



