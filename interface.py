# Auteurs : Clémence Plourde et Emelie Wrese Garand
# Date : 21 décembre 025

import spreadsheet
import codeboot
from pymsgbox import prompt
from pymsgbox import alert
from spreadsheet import matrices, update_cell, save_data, csvtxt_to_data, create_empty_data_header, create_empty_data, create_new_row
from codeboot import write_file



# Initialise l'interface graphique, crée les éléments HTML nécessaires, lie les
# évènements aux fonctions appropriées, etc.
def init():
    sheet = document.querySelector('#spreadsheet')  # accéder à l'élément #spreadsheet

    tab = '<table>' + header(20) 
    for row_idx in range(1,41):
        tab += '<tr>'
        for col_idx in range(1,21):
            tab += f'<td id="r{row_idx}c{col_idx}" onclick="cell_clicked({row_idx},{col_idx})" ></td>'             
        tab += '</tr>'
    tab += '</table>'

    sheet.innerHTML = tab     

    codeboot.add_file_drop_handler(document.querySelector('#cb-body'), drop_file)

    

def header(nb_col):
    header = '<tr>'
    for col_idx in range(1,nb_col + 1):
        header += f'<th id="r{-1}c{col_idx}" onclick="cell_clicked({-1},{col_idx})">Colonne {col_idx}</th>'
    header += '</tr>'
    return header


#def header_mat(nb_col):
    #header = []
    #for i in range(nb_col):
        #header.append(f'Colonne {i+1}')
    #return header

# il faut se définir une équivalence entre une matrice et la table html qui est affichée.

current_sheet = create_empty_data(40,20)   # une matrice
current_header = header(20)          # un text, c'est pas très cute d'avoir 2 type différents ici
current_header_mat = create_empty_data_header(20)

# On va faire nos manipulations sur current_sheet, on va ensuite vouloir les transférer vers le doc html ?
# per_head est un booléen disant s'il y a un header personnalisé à inclure ou simplement un header classique 
def update_table_html(mat, per_head):
    # première ligne devient le header ?
    # transférer le contenu de chaque case de la matrice vers le innerhtml de la cellule associée
    if not per_head:
        titres = header(len(mat[0]))                
    else:
        noms = current_header_mat
        titres = '<tr>'
        for i in range(len(noms)):
            titres += f'<th id="r{-1}c{i+1}" onclick="cell_clicked({-1},{i+1})">{noms[i]}</th>'
        titres += '</tr>'

    tab = '<table>'
    for j in range(len(mat)):
        tab += '<tr>'
        for i in range(len(mat[j])):
            tab += f'<td id="r{j+1}c{i+1}" onclick="cell_clicked({j+1},{i+1})" >{mat[j][i]}</td>'
        tab += '</tr>'
    tab += '</table>'        
    document.querySelector('#spreadsheet').innerHTML = titres + tab

    


def read_csv(path):
    pass

# inspiré du code des ndc de Marc Feeley
#def write_csv(tab):
    #text = ''
    #for ligne in tab:
        #text += ','.join(ligne) + '\n'
    #return text


# I haven't actually used these, maybe they could be good pour éviter de la répétition de code ?
def table(cont): return '<table>' + cont + '</table>'

def tr(cont): return '<tr>' + cont + '</tr>'

def th(cont): return '<th>' + cont + '</th>'

def td(cont): return '<td>' + cont + '</td>'      




def cell(row_idx, col_idx):
    selector = f'#r{row_idx}c{col_idx}'
    return document.querySelector(selector)


selected_cell = None
working_selected_cell = struct(r = 0, c = 0)

# Gère  l'évènement de clic sur une cellule située à la position 
# (row_idx, col_idx) dans la table.
def cell_clicked(row_idx, col_idx):          # à compléter
    global selected_cell

    if selected_cell != None:
        selected_cell.classList.remove('selected')
    selected_cell = cell(row_idx, col_idx)
    selected_cell.classList.add('selected')

    working_selected_cell.r = row_idx
    working_selected_cell.c = col_idx
    
    document.querySelector('#selected-cell').innerHTML = f'({row_idx},{col_idx})'





# Gère l'évènement de téléversement (drag-and-drop) d'un fichier CSV. Le
# paramètre files est une liste de struct avec les champs filenam et content, 
# oû content est le texte du fichier. Cette fonction doit être associée à la 
# zone de téléversement dans l'interface graphique, qui est simplement tout le
# body de la page.
def drop_file(files):
    global current_sheet, current_header_mat

    for file in files:
        name = file.filename  # le programme ne trouve pas filename ?
        content = file.content 
                             
    document.querySelector('#file-name').innerHTML = name

    #lines = content.split('\r\n')     # seulement nécessaire pour moi que je travaille avec windows, mette \n pour unix

    #if lines[-1] == '' : lines.pop()

    lines = csvtxt_to_data(content)
             
    # on veut lire le content et l'afficher dans une table appropriée.
    
    # check for header
    h = 0
    maybe_titles = lines[0].split(',')
    for element in maybe_titles:             # pas idéal, si on a juste du text dans le csv on va directement assumer qu'il y a un header
        if element.isalpha() : h += 1

    if h == len(maybe_titles) : 
        current_sheet = list(map(lambda x: x.split(','), lines[1:]))
        current_header_mat = maybe_titles
        update_table_html(current_sheet, True)
    else :
        current_sheet = list(map(lambda x: x.split(','), lines))
        current_header_mat = create_empty_data_header(len(maybe_titles))
        update_table_html(current_sheet, False)


    # il faut quelque chose qui vérifie si on a un header

codeboot.add_file_drop_handler(document.querySelector('#cb-body'),drop_file)



text = ''


# Gère l'évènement de pression d'une touche dans le champ de texte utilisé pour
# éditer une cellule de la table. Le paramètre event est une structure contenant
# la touche enfoncée, accessible via le champ event.key. Si la touche pressée 
# est "Enter", la modification de la cellule doit être sauvegardée.
def cell_editor_pressed(event):
    global text, current_sheet, current_header_mat, selected_cell
    if event.key == "Enter" :
        selected_cell.innerHTML = text

        row = working_selected_cell.r
        col = working_selected_cell.c
        if row != -1:
            #current_sheet[row-1][col-1] = text
            current_sheet = update_cell(current_sheet, row-1, col-1, text)
        else : current_header_mat[col] = text

        text = ''
        document.querySelector('#cell-editor').value = ''


        #update_table_html(current_sheet, True)

    else : 
        text += event.key
    pass







# Gère l'évènement de clic sur le bouton "Nouvelle table". Cette fonction doit
# créer une nouvelle table vide et l'afficher dans l'interface graphique. Une 
# table vide contient par définitions 20 colonnes et 40 lignes.
def new_sheet_button_clicked():
    current_sheet = create_empty_data(40,20)
    update_table_html(current_sheet, False)
    document.querySelector('#file-name').innerHTML = 'Aucun fichier chargé'
    document.querySelector('#selected-cell').innerHTML = '(X,X)'

    


# Gère l'évènement de clic sur le bouton "Sauvegarder table". Cette fonction 
# doit ouvrir une boîte de dialogue pour entrer un chemin relatif vers le 
# fichier CSV, et sauvegarder les données actuelles dans ce fichier. La ligne
# qui contient les résultats des calculs ne doit pas être sauvegardée.
def save_sheet_button_clicked():
    nom_fichier = prompt('Nom du fichier')
    # quelque chose qui transforme la table de données actuelles en csv : write csv
    if nom_fichier != None:
        save_data(current_sheet, nom_fichier)
        #text = write_csv(current_sheet)
        #codeboot.download(nom_fichier, text)
        document.querySelector('#file-name').innerHTML = nom_fichier
        alert('Fichier téléchargé!')    

    # utiliser codeboot.download('nomfichier', text)   oû text peut être la valeur d'une fonction



# ON PEUT PROBABLEMENT FAIRE UNE FONCTION GÉNÉRALE POUR LES 6 FONCTIONS
# SUIVANTES POUR AVOIR UNE MEILLEURE ABSTRACTION PROCÉDURALE


# Gère l'évènement de clic sur le bouton "Ajouter ligne avant". Cette fonction
# doit ajouter une nouvelle ligne avant la ligne sélectionnée dans la table.
def add_row_before_button_clicked():
    global current_sheet, current_header_mat
    row = working_selected_cell.r
    #current_sheet.insert(row-1, ['']*len(current_header_mat))
    current_sheet = create_new_row(current_sheet, row)
    update_table_html(current_sheet, True)

# Gère l'évènement de clic sur le bouton "Ajouter ligne après". Cette fonction
# doit ajouter une nouvelle ligne après la ligne sélectionnée dans la table.
def add_row_after_button_clicked():
    global current_sheet, current_header_mat
    row = working_selected_cell.r
    #current_sheet.insert(row, ['']*len(current_header_mat))
    current_sheet = create_new_row(current_sheet, row+1)
    update_table_html(current_sheet, True)
    

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
