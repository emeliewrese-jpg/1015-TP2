# Auteurs : Clémence Plourde et Émelie Wrese Garand
# Date : 21 décembre 2025

# Ce programme implémente la logique des opérations du tableur. Il est importé
# par le programme interface.py pour accéder à ses fonctionnalités.

# À noter que les descriptions de fonctions viennent en partie ou en totalité
# des descriptions fournies dans les specs du TP2 pour le cours IFT1015-A25.

import functools
import codeboot

# Procédure qui vérifie si les indices de lignes et de colonnes sont valides. 
# À appeler dans chaque fonctions/procédures qui suit.
def validate_idx(idx):
    pass

# Fonction qui fait l'équivalent de deepcopy(), mais qui va fonctionner dans
# codeboot. Retourne un tableau de tableaux complètement indépendant du 
# tableau original.
def my_deepcopy(tab):
    new_tab = list(map(lambda x: x.copy(), tab))
    return new_tab
    

# Sauvegarde la table data dans un fichier CSV situé à l'emplacement file_path.
def save_data(data, file_path):
    text = ''
    for ligne in data:
        text += ','.join(ligne) + '\n'

    return codeboot.download(file_path, text)

# Convertit le texte CSV csvtext en une structure de données qui représente la 
# table.
def csvtxt_to_data(csvtext):
    def csvtxt_to_data(csvtext):
    lines = csvtext.split("\n")     # seulement nécessaire pour moi que je travaille avec windows, mette \n pour unix
    if lines[-1] == "" : lines.pop()
    if not lines:                 # si lines/csvtext entré est vide
        return [],[]
    header = lines[0].split(",")
    data = [] 
    for line in lines[1:]:
        val = line.split(",")    # liste de toutes ligne
        row_i = []          
   # conversion des données nombres     
        for i in val:
            try:
                row_i.append(int(i))
            except:
                try:
                    row_i.append(float(i))
                except: 
                    row_i.append(i)    
        data.append(row_i)
        print(header)
    return header, data

# Crée et retourne un tableau de textes du format 'colonne x' oû x est le 
# numéro de la colonne pour num_cols (int) colonnes (avec 1 = la première 
# colonne).
def create_empty_data_header(num_cols):
    header = []
    for i in range(num_cols):
        header.append(f'Colonne {i+1}')
    return header


# Crée et retourne un tableau de tableaux de tetes représentant une table vide 
# avec num_cols (int) colonnes et num_rows (int) lignes.
def create_empty_data(num_rows, num_cols):
    return matrices(num_rows, num_cols, '')
    

# Crée et retourne un nouvel en-tête de colonne en insérante une nouvelle 
# colonne à la position col_idx dans l'en-tête header. Le nom de la nouvelle
# colonne doit être "colonne x" oû x est le numéro de la nouvelle colonne.
def create_new_header_column(header, col_idx):
    pass

# Crée et retourne une nouvelle table en insérant une nouvelle colonne à la 
# position col_idx dans la table data. Les cellules de la nouvelle colonne
# doivent être initialisées à des textes vides.
def create_new_column(data, col_idx):
    pass

# Crée et retourne une nouvelle table insérant une nouvelle ligne à la position
# row_idx dans la table data. Les cellules de la nouvelle ligne sont initialisée
# à des textes vides.
def create_new_row(data, row_idx):
    data.insert(row_idx-1, ['']*len(data[0]))
    return data

# Crée et retourne un nouvel en-tête de colonne en supprimant la colonne à la 
# position col_idx dans l'en-tête header.
def delete_header_column(header, col_idx):
    if col_idx in range(len(header)) or col_idx in range(-1, -(len(header)),-1):   # pour prendre des index positifs et négatifs
        new_header = header.copy()
        new_header.pop(col_idx) 
        return new_header
    else : return None

# Crée et retourne une nouvelle table en supprimant la colonne à la position
# col_idx dans la table data.
def delete_column(data, col_idx):                                                    
    def delete_element(ligne):
        ligne.pop(col_idx)
        return ligne
    
    if col_idx in range(len(data[0])) or col_idx in range(-1, -(len(data[0])),-1):
        new_data = my_deepcopy(data)
        new_data_mod = list(map(delete_element, new_data))     
        return new_data_mod
    else : return None


# Crée et retourne une nouvelle table en supprimant la ligne à la position
# row_idx dans la table data.
def delete_row(data, row_idx):
    if row_idx in range(len(data)) or row_idx in range(-1, -(len(data)),-1):
        new_data = data.copy()
        new_data.pop(row_idx)
        return new_data
    else : return None

# Crée et retourne une nouvelle table en mettant à jour la cellule à la position
# (row_idx, col_idx) dans la table data avec la nouvelle valeur new_value.
def update_cell(data, row_idx, col_idx, new_value):               
    if (row_idx in range(len(data)) or row_idx in range(-1, -(len(data)),-1)) and (col_idx in range(len(data[0])) or col_idx in range(-1, -(len(data[0])),-1)):
        new_data = my_deepcopy(data)
        new_data[row_idx][col_idx] = new_value
        return new_data
    else : return None


# Calcule et retourne la somme des valeurs numériques dans la colonne col_idx
# de la table data. Si la colonne ne contient pas de valeurs numériques, 
# retourne None.
def get_sum(data, col_idx):
    def is_decimal(n):
        text = str(n)
        if text[0] == '-': text = text[1:]
        if text.isdecimal() :
            return 1
        else : return 0
    
    if col_idx in range(len(data[0])) or col_idx in range(-1, -(len(data[0])),-1):
        new_data = my_deepcopy(data)
        col = list(map(lambda x: x.pop(col_idx), new_data))
        if functools.reduce(lambda x,y: x + is_decimal(y), col, 0) == len(col):
            somme = functools.reduce(lambda x,y: x + y, col, 0)
            return somme
        else : return None
    else : return None   
    



# Retourne un tableau contenant les différentes valeurs présentent dans list.
def get_categories(list):
    resultat = []
    for i in list:
        if i not in resultat:
            resultat.append(i)
    return resultat

# Retourne la position de element dans list.
def get_position(list,element):
    for i in range(len(list)):
        if list[i] == element:
            return i

# Retourne une matrice nbLignes x nbColonnes, remplies de None.      
# Inspiré des notes de cours de Marc Feeley  
def matrices(nbLignes, nbColonnes,init):
    resultat = [init]*nbLignes
    
    for i in range(nbLignes):
        resultat[i] = [init]*nbColonnes
        
    return resultat

# Crée et retourne un tableau de tableaux oû chaque sous-tableau représente 
# un groupe de lignes de la table data qui partagent la même valeur dans la
# colonne col_idx.            
def get_group_by(data, col_idx):
    new_data = my_deepcopy(data)
    col_values = list(map(lambda x: x.pop(col_idx), new_data))
    categories = get_categories(col_values)
    resultat = matrices(len(categories),1, None)
    for ligne in data:
        for cat in categories:
            if ligne[col_idx] == cat:
                idx = get_position(categories, cat)
                if resultat[idx] == [None]:
                    resultat[idx] = [ligne]
                else :
                    resultat[idx].append(ligne)
    return resultat    



def tests_unitaires():
    # tests delete_header_column
    header = ['Colonne 1', 'Colonne 2', 'Colonne 3', 'Colonne 4', 'Colonne 5']    # might have to put the tab directly in the assert or call
    # back to it after each assert, cuz the function modifies the header

    assert delete_header_column(header, 2) == ['Colonne 1', 'Colonne 2', 'Colonne 4', 'Colonne 5']
    assert delete_header_column(header, 0) == ['Colonne 2', 'Colonne 3', 'Colonne 4', 'Colonne 5']
    assert delete_header_column(header, -1) == ['Colonne 1', 'Colonne 2', 'Colonne 3', 'Colonne 4']
    assert delete_header_column(header, 7) == None

    # tests delete_column
    data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    assert delete_column(data, 1) == [[1,3],[4,6],[7,9],[10,12]]
    assert delete_column(data, 0) == [[2,3],[5,6],[8,9],[11,12]]
    assert delete_column(data, -1) == [[1,2],[4,5],[7,8],[10,11]]
    assert delete_column(data, 5) == None

    # tests delete_row
    data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    assert delete_row(data, 2) == [[1,2,3],[4,5,6],[10,11,12]]
    assert delete_row(data, 0) == [[4,5,6],[7,8,9],[10,11,12]]
    assert delete_row(data, -1) == [[1,2,3],[4,5,6],[7,8,9]]
    assert delete_row(data, 7) == None

    # tests update_cell
    data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    assert update_cell(data, 2,1, 0) == [[1,2,3],[4,5,6],[7,0,9],[10,11,12]]
    assert update_cell(data, 1,2, 'bonjour') == [[1,2,3],[4,5,'bonjour'],[7,8,9],[10,11,12]]
    assert update_cell(data, 0,0, 100) == [[100,2,3],[4,5,6],[7,8,9],[10,11,12]]
    assert update_cell(data, -1,-1, 25) == [[1,2,3],[4,5,6],[7,8,9],[10,11,25]]
    assert update_cell(data, 2,7, 0) == None

    # tests get_sum
    data = [[1,'a',3],[4,'b',6],[7,'c',9],[10,'d',12]]
    assert get_sum(data, 2) == 30
    assert get_sum(data, 1) == None
    data = [[1,'a',3],[4,5,6],[7,6,9],[10,11,12]]
    assert get_sum(data,1) == None
    data = [[1,2,3],[-4,5,6],[7,8,9],[-10,11,12]]
    assert get_sum(data, 0) == -6
    # faire des tests si les données sont groupées

    # tests get_group_by
    data = [[1,2,3,'a'],[4,2,3,'b'],[7,2,9,'b'],[10,2,12,'a']]
    assert get_group_by(data, 2) == [[[1,2,3,'a'],[4,2,3,'b']],[[7,2,9,'b']],[[10,2,12,'a']]]
    assert get_group_by(data, 3) == [[[1,2,3,'a'],[10,2,12,'a']],[[4,2,3,'b'],[7,2,9,'b']]]
    assert get_group_by(data, 0) == [[[1,2,3,'a']],[[4,2,3,'b']],[[7,2,9,'b']],[[10,2,12,'a']]]
    assert get_group_by(data, 1) == [[[1,2,3,'a'],[4,2,3,'b'],[7,2,9,'b'],[10,2,12,'a']]]

    print('Tous les tests sont satisfaits!')




tests_unitaires()
