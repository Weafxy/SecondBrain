from notes import NotesManager
from graph import draw_graph

manager = NotesManager("notes.json")

print("Second Brain CLI (AI Extended) - type 'help' for commands")

while True:
    cmd = input("brain> ").strip().split()
    if not cmd:
        continue
    action = cmd[0]

    if action == "add":
        title = input("Title: ")
        content = input("Content: ")
        tags = input("Tags (comma separated): ").split(",") if input("Add tags? (y/n) ")=="y" else []
        note_id = manager.add_note(title, content, tags)
        print(f"Note added! ID: {note_id}")

    elif action == "list":
        for note in manager.list_notes():
            print(f"{note['id']} - {note['title']} [{', '.join(note['tags'])}] Links: {len(note['links'])}")

    elif action == "search":
        query = " ".join(cmd[1:])
        results = manager.search_notes(query)
        for note in results:
            print(f"{note['id']} - {note['title']} [{', '.join(note['tags'])}]")

    elif action == "suggest":
        note_id = cmd[1] if len(cmd) > 1 else None
        note = next((n for n in manager.list_notes() if n["id"] == note_id), None)
        if note:
            from ai import suggest_links
            suggestions = suggest_links([n for n in manager.list_notes() if n["id"] != note_id], note)
            print(f"Suggested links for '{note['title']}':")
            for sid in suggestions:
                linked_note = next(n for n in manager.list_notes() if n["id"] == sid)
                print(f"- {linked_note['title']} ({sid})")
        else:
            print("Note ID not found.")

    elif action == "graph":
        draw_graph(manager.list_notes())

    elif action == "help":
        print("Commands: add, list, search <query>, tag <tag>, link <id1> <id2>, suggest <id>, graph, exit")

    elif action == "exit":
        break