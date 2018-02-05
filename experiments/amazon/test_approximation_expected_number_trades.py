from utilities.load_save_data import extract_degree_sequence

if __name__ == '__main__':
    filename = '/home/julien/Documents/SPPII/data/Amazon/amazon0302.txt'
    degree_left, degree_right = extract_degree_sequence(edge_list_filename=filename, sep=',')
    # computing approximation
    factor = 1. / float(len(degree_left) * len(degree_right))
    maximum_number_of_possible_trades = 0
    for i, ki in degree_left.items():
        for j, kj in degree_right.items():
            maximum_number_of_possible_trades += min(ki, kj)
    print("expected maximum number of trades: {}".format(factor * maximum_number_of_possible_trades))
