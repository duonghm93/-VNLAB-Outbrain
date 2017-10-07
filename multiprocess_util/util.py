from os import listdir


def get_list_of_file(root_folder, prefix):
    list_file = listdir(root_folder)
    list_file = list(filter(lambda x: x.startswith(prefix), list_file))
    list_file_full = list(map(lambda x: root_folder + x, list_file))
    return list_file_full