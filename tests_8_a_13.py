def tests_unitaires():
    # tests delete_header_column
    header = ['Colonne 1', 'Colonne 2', 'Colonne 3', 'Colonne 4', 'Colonne 4']    # might have to put the tab directly in the assert or call
    # back to it after each assert, cuz the function modifies the header

    assert delete_header_column(header, 3) == ['Colonne 1', 'Colonne 2', 'Colonne 4', 'Colonne 5']
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
    assert update_cell(data, -1,-1, 25) == [[1,2,3],[4,5,6],[7,0,9],[10,11,25]]
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
    assert get_group_by(data, 2) == [[[1,2,3,'a'],[4,5,3,'b']],[[7,8,9,'b']],[[10,11,12,'a']]]
    assert get_group_by(data, 3) == [[[1,2,3,'a'],[10,11,12,'a']],[[4,5,3,'b'],[7,8,9,'b']]]
    assert get_group_by(data, 0) == [[[1,2,3,'a']],[[4,5,3,'b']],[[7,8,9,'b']],[[10,11,12,'a']]]
    assert get_group_by(data, 1) == [[1,2,3,'a'],[4,2,3,'b'],[7,2,9,'b'],[10,2,12,'a']]
