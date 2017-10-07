from os import listdir
import constant
from multiprocessing import Queue


def get_list_of_file(root_folder, prefix):
    list_file = listdir(root_folder)
    list_file = list(filter(lambda x: x.startswith(prefix), list_file))
    list_file_full = list(map(lambda x: root_folder + x, list_file))
    return list_file_full


def create_queue_job(input_folder, prefix):
    queue_job = Queue()
    list_file = get_list_of_file(input_folder, prefix)
    for file in list_file:
        queue_job.put(file)
    return queue_job