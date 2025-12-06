import spreadsheet
import codeboot
from pymsgbox import prompt

# Initialise l'interface graphique, crée les éléments HTML nécessaires, lie les
# évènements aux fonctions appropriées, etc.
def init():
    sheet = document.querySelector('#spreadsheet')  # accéder à l'élément #spreadsheet
    sheet.innerHTML = "<p>blalabl</p>"     #changer le contenu de spreadsheet, on va vouloir mettre la table ici avec <tr>, <tb>

    codeboot.add_file_drop_handler(document.querySelector('#cb-body'), drop_file)

    
# il faut se définir une équivalence entre une matrice et la table html qui est affichée.

current_sheet = matrices(40,20,'')   


def read_csv(path):
    pass

def write_csv(path):
    pass

def table(cont): return '<table>' + cont + '</table>'

def tr(cont): return '<tr>' + cont + '</tr>'

def th(cont): return '<th>' + cont + '</th>'

def td(cont): return '<td>' + cont + '</td>'        

def cell(row_idx, col_idx):
    selector = f'[data-row="{row_idx}"][data-col="{col_idx}"]'
    return document.querySelector(selector)

selected_cell = None

# Gère  l'évènement de clic sur une cellule située à la position 
# (row_idx, col_idx) dans la table.
def cell_clicked(row_idx, col_idx):          # à compléter
    global selected_cell
    if selected_cell != None:
        selected_cell.classList.remove('selected')
    selected_cell = cell(row_idx, col_idx)
    selected_cell.classList.add('selected')
    pass

# Gère l'évènement de téléversement (drag-and-drop) d'un fichier CSV. Le
# paramètre files est une liste de struct avec les champs filenam et content, 
# oû content est le texte du fichier. Cette fonction doit être associée à la 
# zone de téléversement dans l'interface graphique, qui est simplement tout le
# body de la page.
def drop_file(files):
    name = files.filename
    content = files.content
    lines = content.split('\n')         # pas finit, juste un début de l'idée de ce qu'il faut faire
    # on veut lire le content et l'afficher dans une table appropriée.
    pass

# Gère l'évènement de pression d'une touche dans le champ de texte utilisé pour
# éditer une cellule de la table. Le paramètre event est une structure contenant
# la touche enfoncée, accessible via le champ event.key. Si la touche pressée 
# est "Enter", la modification de la cellule doit être sauvegardée.
def cell_editor_pressed(event):
    pass

# Gère l'évènement de clic sur le bouton "Nouvelle table". Cette fonction doit
# créer une nouvelle table vide et l'afficher dans l'interface graphique. Une 
# table vide contient par définitions 20 colonnes et 40 lignes.
def new_sheet_button_clicked():
    ligne = '<tr>' + '<td></td>'*20 + '</tr>'            # est-ce que les cells crées devraient être identifié par le selector comme décrit dans la fct cell?
    tab = 40*ligne
    return table(tab)
    pass

# Gère l'évènement de clic sur le bouton "Sauvegarder table". Cette fonction 
# doit ouvrir une boîte de dialogue pour entrer un chemin relatif vers le 
# fichier CSV, et sauvegarder les données actuelles dans ce fichier. La ligne
# qui contient les résultats des calculs ne doit pas être sauvegardée.
def save_sheet_button_clicked():
    nom_fichier = prompt('Nom du fichier')
    # quelque chose qui transforme la table de données actuelles en csv : write csv
    # utiliser codeboot.download('nomfichier', text)   oû text peut être la valeur d'une fonction
    pass

# Gère l'évènement de clic sur le bouton "Ajouter ligne avant". Cette fonction
# doit ajouter une nouvelle ligne avant la ligne sélectionnée dans la table.
def add_row_before_button_clicked():
    pass

# Gère l'évènement de clic sur le bouton "Ajouter ligne après". Cette fonction
# doit ajouter une nouvelle ligne après la ligne sélectionnée dans la table.
def add_row_after_button_clicked():
    pass

# Gère l'évènement de clic sur le bouton "Ajouter colonne avant". Cette fonction
# doit ajouter une nouvelle colonne avant la colonne sélectionnée dans la table.
def add_column_before_button_clicked():
    pass

# Gère l'évènement de clic sur le bouton "Ajouter colonne après". Cette fonction
# doit ajouter une nouvelle colonne après la colonne sélectionnée dans la table.
def add_column_after_button_clicked():
    pass

# Gère l'évènement de clic sur le bouton "Supprimer ligne". Cette fonction
# doit supprimer la ligne sélectionnée dans la table.
def delete_row_button_clicked():

    pass

# Gère l'évènement de clic sur le bouton "Supprimer colonne". Cette fonction
# doit supprimer la colonne sélectionnée dans la table.
def delete_column_button_clicked():
    pass

# Gère l'évènement de clic sur le bouton "Somme". Cette fonction soit calculer
# la somme des valeurs numériques dans toutes les colonnes et afficher le 
# résultat à l'utilisateur dans une ligne sous les lignes de la table. Si une 
# colonne ne contient pas de valeurs numériques, la cellule correspondante doit
# afficher simplement "NaN".
def sum_button_clicked():
    pass

# Gère l'évènement de clic sur le bouton "Effacer statistiques". Cette fonction
# doit effacer la ligne qui affiche les résultats des calculs (somme) sous les
# lignes de la table. Ce bouton doit être désactivé si aucune statistique n'est
# affichée.
def clear_stats_button_clicked():
    pass

# Gère l'évènement de clic sur le bouton "Grouper par". Cette fonction doit 
# regrouper les lignes de la table selon les valeurs dans la colonne 
# sélectionnée. Si les données sont déjà en mode "Grouper par", et que 
# l'utilisateur clique à ouveau sur le bouton "Grouper par" avec la même colonne
# sélectionnée, les données doivent revenir en mode normal (non groupé). L'ordre
# des lignes ne doit pas nécessairement être le même qu'avant le groupement.
# Lordque les données sont en mode "Grouper par", une ligne dans la table avant 
# chaque groupe doit afficher la valeur du groupe du format "Groupe : VALEUR", 
# oû VALEUR est la valeur partagée par les lignes du groupe.
def group_by_button_clicked():
    pass

init() # démarrer l'application web
