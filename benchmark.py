from util import print_and_compare, description

"""
    THE ultimate test benchmark
"""

if __name__ == '__main__':

    #keep track of the number of test cases
    num_case = 1
    
    """
        Test init method
    """
    description(num_case, "init")
    from developed import developed_table_1 
    from expected import expected_table_1
    print_and_compare(developed_table_1, expected_table_1, num_case, "init")
    num_case += 1

    description(num_case, "init", table_size=15)
    from developed import developed_table_2 
    from expected import expected_table_2
    print_and_compare(developed_table_2, expected_table_2, num_case, "init")
    num_case += 1

    """
        Test insert method
    """
    input_param = [(20, 'Vue'), (3, "React")]
    description(num_case, "insert", table_size=6, input_param=input_param)
    from developed import developed_table_3
    from expected import expected_table_3
    print_and_compare(developed_table_3, expected_table_3, num_case, "insert")
    num_case += 1

    input_param = [(20, 'Vue'), (3, "React"), (5, "Angular")]
    description(num_case, "insert", table_size=6, input_param=input_param)
    from developed import developed_table_4
    from expected import expected_table_4
    print_and_compare(developed_table_4, expected_table_4, num_case, "insert")
    num_case += 1

    input_param = [(20, 'Vue'), (3, "React"), (5, "Angular"), (39, "Express")]
    description(num_case, "insert", table_size=6, input_param=input_param)
    from developed import developed_table_5
    from expected import expected_table_5
    print_and_compare(developed_table_5, expected_table_5, num_case, "insert")
    num_case += 1

    """
        Test retrieve method
    """
    input_param = [(20, 'Vue'), (3, "React"), (5, "Angular"), (39, "Express"), "retrieve 3"]
    description(num_case, "retrieve", table_size=6, input_param=input_param)
    from developed import developed_table_6, developed_return_6
    from expected import expected_table_6, expected_return_6
    print_and_compare(developed_table_6, expected_table_6, num_case, "retrieve", developed_return_6, expected_return_6)
    num_case += 1

    input_param = [(20, 'Vue'), (3, "React"), (5, "Angular"), (39, "Express"), "retrieve 39"]
    description(num_case, "retrieve", table_size=6, input_param=input_param)
    from developed import developed_table_7, developed_return_7
    from expected import expected_table_7, expected_return_7
    print_and_compare(developed_table_7, expected_table_7, num_case, "retrieve", developed_return_7, expected_return_7)
    num_case += 1

    input_param = [(20, 'Vue'), (3, "React"), (5, "Angular"), (39, "Express"), "retrieve 5"]
    description(num_case, "retrieve", table_size=6, input_param=input_param)
    from developed import developed_table_8, developed_return_8
    from expected import expected_table_8, expected_return_8
    print_and_compare(developed_table_8, expected_table_8, num_case, "retrieve", developed_return_8, expected_return_8)
    num_case += 1
    
    """
        Test member method
    """
    input_param = [(20, 'Vue'), (3, "React"), (5, "Angular"), (39, "Express"), "member 20"]
    description(num_case, "member", table_size=6, input_param=input_param)
    from developed import developed_table_9, developed_return_9
    from expected import expected_table_9, expected_return_9
    print_and_compare(developed_table_9, expected_table_9, num_case, "member", developed_return_9, expected_return_9)
    num_case += 1

    input_param = [(20, 'Vue'), (3, "React"), (5, "Angular"), (39, "Express"), "member 39"]
    description(num_case, "member", table_size=6, input_param=input_param)
    from developed import developed_table_10, developed_return_10
    from expected import expected_table_10, expected_return_10
    print_and_compare(developed_table_10, expected_table_10, num_case, "member", developed_return_10, expected_return_10)
    num_case += 1

    input_param = [(20, 'Vue'), (3, "React"), (5, "Angular"), (39, "Express"), "member 1024"]
    description(num_case, "member", table_size=6, input_param=input_param)
    from developed import developed_table_11, developed_return_11
    from expected import expected_table_11, expected_return_11
    print_and_compare(developed_table_11, expected_table_11, num_case, "member", developed_return_11, expected_return_11)
    num_case += 1
