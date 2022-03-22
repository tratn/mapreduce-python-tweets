# Implement a reducer function to combine results of mapper 
def reducer_count_topic(count_dict1, count_dict2): 
    """ Combine the resulting dictionaries from mapper """
    count_dict1.update(count_dict2)
    return count_dict1