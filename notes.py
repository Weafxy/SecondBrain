import uuid
from datetime import datetime
from storage import Storage
from ai import suggest_links

class NotesManager:
    def __init__(self, filename="notes.json"):
        self.storage = Storage(filename)
        self.notes = self.storage.load()

    def add_note(self, title, content, tags=[]):
        note_id = str(uuid.uuid4())
        note = {
            "id": note_id,
            "title": title,
            "content": content,
            "tags": tags,
            "links": [],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        self.notes.append(note)
        self.auto_link(note)
        self.storage.save(self.notes)
        return note_id

    def list_notes(self):
        return self.notes

    def search_notes(self, query):
        return [n for n in self.notes if query.lower() in n["title"].lower() or query.lower() in n["content"].lower()]

    def tag_notes(self, tag):
        return [n for n in self.notes if tag in n["tags"]]
    
    def link_notes(self, id1, id2):
        # beide Notizen gegenseitig verlinken
        for n in self.notes:
            if n["id"] == id1 and id2 not in n["links"]:
                n["links"].append(id2)
            if n["id"] == id2 and id1 not in n["links"]:
                n["links"].append(id1)
        self.storage.save(self.notes)


    def auto_link(self, new_note):
        """AI-basierte Verknüpfungsvorschläge"""
        suggested_ids = suggest_links([n for n in self.notes if n["id"] != new_note["id"]], new_note)
        for sid in suggested_ids:
            new_note["links"].append(sid)
            for n in self.notes:
                if n["id"] == sid and new_note["id"] not in n["links"]:
                    n["links"].append(new_note["id"])