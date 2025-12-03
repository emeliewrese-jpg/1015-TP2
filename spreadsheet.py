# Auteurs : Clémence Plourde et Émelie Wrese Garand
# Date : 21 décembre 2025

# Ce programme implémente la logique des opérations du tableur. Il est importé
# par le programme interface.py pour accéder à ses fonctionnalités.

# À noter que les descriptions de fonctions viennent en partie ou en totalité
# des descriptions fournies dans les specs du TP2 pour le cours IFT1015-A25.


# Procédure qui vérifie si les indices de lignes et de colonnes sont valides. 
# À appeler dans chaque fonctions/procédures qui suit.
def validate_idx(idx):
    pass

# Sauvegarde la table data dans un fichier CSV situé à l'emplacement file_path.
def save_data(data, file_path):
    pass

# Convertit le texte CSV csvtext en une structure de données qui représente la 
# table.
def csvtxt_to_data(csvtext):
    pass

# Crée et retourne un tableau de textes du format 'colonne x' oû x est le 
# numéro de la colonne pour num_cols (int) colonnes (avec 1 = la première 
# colonne).
def create_empty_data_header(num_cols):
    pass

# Crée et retourne un tableau de tableaux de tetes représentant une table vide 
# avec num_cols (int) colonnes et num_rows (int) lignes.
def create_empty_data(num_cols, num_rows):
    pass

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
    pass

# Crée et retourne un nouvel en-tête de colonne en supprimant la colonne à la 
# position col_idx dans l'en-tête header.
def delete_header_column(header, col_idx):
    pass

# Crée et retourne une nouvelle table en supprimant la colonne à la position
# col_idx dans la table data.
def delete_column(data, col_idx):
    pass

# Crée et retourne une nouvelle table en supprimant la ligne à la position
# row_idx dans la table data.
def delete_row(data, row_idx):
    pass

# Crée et retourne une nouvelle table en mettant à jour la cellule à la position
# (row_idx, col_idx) dans la table data avec la nouvelle valeur new_value.
def update_cell(data, row_idx, col_idx, new_value):
    pass

# Calcule et retourne la somme des valeurs numériques dans la colonne col_idx
# de la table data. Si la colonne ne contient pas de valeurs numériques, 
# retourne None.
def get_sum(data, col_idx):
    pass

# Crée et retourne un tableau de tableaux oû chaque sous-tableau représente 
# un groupe de lignes de la table data qui partagent la même valeur dans la
# colonne col_idx.
def get_group_by(data, col_idx):
    pass
