
def tests_unitaires():


    save_data(data, file_path):
        assert

    # csvtxt_to_data(csvtext)
    # converts cvs line of text to header table and data tables
    
       csvtext = "A,B,C\n1,2,3\n4,5,6\n"
header, data = csvtxt_to_data(csvtext)
assert header == ["A","B","C"]
assert data == [[1,2,3],[4,5,6]]   #

csvtext = "Catastrophy, Reported, On, February, Third\n11,8,2,8\n"
header, data = csvtxt_to_data(csvtext)
assert header == ["Catastrophy", " Reported", " On", " February", " Third"]  
assert data == [[11,8,2,8]]

csvtext = "Name, Author\n Aeneid, Virgil\n Innocence, Koontz"
header, data = csvtxt_to_data(csvtext)
assert header == ["Name", " Author"]
assert data == [[" Aeneid", " Virgil"], [" Innocence", " Koontz"]]

csvtext = "x,y\n350,500\n14,30\n6,90"
header, data = csvtxt_to_data(csvtext)
assert header == ["x", "y"]
assert data == [[350, 500], [14, 30], [6,90]]
        

    # create_empty_data_header(num_cols):
    # creates column names/labels : input num_cols (int) ; output table of "Colonne i"
        
        assert create_empty_data_header(3) == ["Colonne 1", "Colonne 2", "Colonne 3"]
        assert create_empty_data_header(1) == ["Colonne 1"]
        assert create_empty_data_header(0) == []

    # create_empty_data(num_cols, num_rows)
    # creates empty grid/table for spreadsheet 
        assert create_empty_data(2, 2) == [["",""],["",""]]
        assert create_empty_data(1, 3) == [[""], [""],[""]]
        assert create_empty_data(500,0) == []
        assert create_empty_data(0, 2) == [[],[]]
        assert create_empty_data(0, 0) == []

    # create_new_header_column(header, col_idx)
    # new column name into list of column names/labels, after specific entry
    
        header1 = ['Colonne 1', 'Colonne 2', 'Colonne 3', 'Colonne 4', 'Colonne 5'] 
        assert create_new_header_column (header1, 3) == ['Colonne 1', 'Colonne 2', 'Colonne 3', "Colonne 6", 'Colonne 4', 'Colonne 5'] 
        assert create_new_header_column (header1, 0) == ["Colonne 6"'Colonne 1', 'Colonne 2', 'Colonne 3', 'Colonne 4', 'Colonne 5'] 
        header2 = []
        assert create_new_header_column (header2, 0) == ["Colonne 1"]
        assert create_new_header_column (header1, -3) == None
        assert create_new_header_column (header1, 7) == None
        

    # create_new_column(data, col_idx)
    # creates new column inside a table/grid, after specific column entry 
      
        data1 = [[1,2,3],[4,5,6]]
        assert create_new_column(data1, 3) == [[1,2,3,""],[4,5,6,""]]
        data2 = [ ["Aeneid", "Virgil"], ["Innocence", "Koontz"]]
        assert create_new_column(data2, 0) == [ ["", "Aeneid", "Virgil"], ["", "Innocence", "Koontz"]]
        data3 = [[11,8,2,8]]
        assert create_new_column(data3, 1) == [[11,"",8,2,8]]
        assert create_new_column(data3, 12) == None
        assert create_new_column(data3, -2) == None

    # create_new_row(data, row_idx)
    # creates new row inside a table/grid, after specific row entry (w same # of columns)
        data1 = [[1,2,3],[4,5,6]]
        assert create_new_row(data1, 2) == [[1,2,3],[4,5,6], ["","",""]]
        data2 = [ ["Aeneid", "Virgil"], ["Innocence", "Koontz"]]
        assert create_new_row(data2, 0) == [ ["",""],["Aeneid", "Virgil"], ["Innocence", "Koontz"]]
        data3 = [[11],[8],[2],[8]]
        assert create_new_row(data3, 3) == [[11],[8],[2],[""],[8]]
        assert create_new_row(data3, -1) == None
        assert create_new_row(data3, 9) == None
      
end 
