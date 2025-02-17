from utils import load_data, load_template, save_data

def index():
    notes_li = [
        load_template('components/note.html').format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    notes = load_data('notes.json')
    notes.append({'titulo': titulo, 'detalhes': detalhes})
    save_data('notes.json', notes)
    return notes
