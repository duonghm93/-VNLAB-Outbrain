from os import listdir
import time
import pandas as pd
from multiprocessing import Process, Queue, Manager

input_folder = 'D:/outbrain/sort_input/'
output_folder = 'D:/outbrain/output_sort/'
inaccuracy_ranking_file = 'D:/outbrain/inaccurate.csv'
final_output_file = 'D:/outbrain/submit.csv'
TEST_FILE_PREFIX = 'test'
LINE_PER_FILE = 100000
RESULT_FILE_COLUMNS_NAME = ['display_id', 'ad_id', 'recommend_rate']


def get_list_of_file(root_folder):
    list_file = listdir(root_folder)
    list_file = list(filter(lambda x: x.startswith(TEST_FILE_PREFIX), list_file))
    list_file_full = list(map(lambda x: root_folder + x, list_file))
    return list_file_full


def write_ranking_recommend_to_file(os, display_id, ad_rate_pairs):
    ad_rate_pairs.sort(key=lambda pair: pair[1], reverse=True)
    ranking_ad_export = list(map(lambda pair: pair[0], ad_rate_pairs))
    os.write('{0},'.format(display_id))
    for ad_id in ranking_ad_export[:-1]:
        os.write('{0} '.format(ad_id))
    os.write('{0}'.format(ranking_ad_export[-1]))


def write_inaccurate_recom(display_id, ad_rate_pair):
    os = open(inaccuracy_ranking_file, 'a+')
    for ad_id, rate in ad_rate_pair:
        os.write('{0},{1},{2}\n'.format(display_id, ad_id, rate))
    os.close()


def sort_in_each_file(input_file):
    start_time = time.time()
    print('Start process file: ', input_file)
    df = pd.read_csv(input_file, header=None)
    is_first_ad_id = True
    df.columns = RESULT_FILE_COLUMNS_NAME
    df = df.sort_values(['display_id', 'recommend_rate'], ascending=[True, False])

    filename = input_file.split('/')[-1]
    output_file = output_folder + filename
    os = open(output_file, 'w')

    prev_display_id = None
    current_ad_rate_pairs = []
    for index, row in df.iterrows():
        current_display_id = int(row['display_id'])
        current_ad_id = int(row['ad_id'])
        current_rate = row['recommend_rate']
        if prev_display_id is None:
            # may_be_inaccurate_ranking_results.append((current_display_id, current_ad_rate_pairs))
            write_inaccurate_recom(current_display_id, current_ad_rate_pairs)
            prev_display_id = current_display_id
            current_ad_rate_pairs.append((current_ad_id, current_rate))
        elif prev_display_id == current_display_id:
            current_ad_rate_pairs.append((current_ad_id, current_rate))
        else:
            # writing file there
            if not is_first_ad_id:
                os.write('\n')
            else:
                is_first_ad_id = False
            write_ranking_recommend_to_file(os, prev_display_id, current_ad_rate_pairs)
            # init for new record
            prev_display_id = current_display_id
            current_ad_rate_pairs = [(current_ad_id, current_rate)]

    os.write('\n')
    write_ranking_recommend_to_file(os, prev_display_id, current_ad_rate_pairs)
    # may_be_inaccurate_ranking_results.append((prev_display_id, current_ad_rate_pairs))
    write_inaccurate_recom(prev_display_id, current_ad_rate_pairs)
    os.close()
    print('Finish process file: ', input_file, ' - ', (time.time() - start_time), ' s')


def sort_each_file_with_queue(queue_job):
    while not queue_job.empty():
        input_file = queue_job.get()
        sort_in_each_file(input_file)


def init_queue(queue_job):
    list_file = get_list_of_file(input_folder)
    for file in list_file:
        queue_job.put(file)


def load_inaccurate_line_and_repair():
    repairs_result = []
    df = pd.read_csv(inaccuracy_ranking_file, header=None)
    df.columns = RESULT_FILE_COLUMNS_NAME
    df = df.sort_values(['display_id', 'recommend_rate'], ascending=[True, False])
    prev_display_id = None
    current_ad_rate_pairs = []
    for index, row in df.iterrows():
        current_display_id = int(row['display_id'])
        current_ad_id = int(row['ad_id'])
        current_rate = row['recommend_rate']
        if prev_display_id is None:
            prev_display_id = current_display_id
            current_ad_rate_pairs.append((current_ad_id, current_rate))
        elif prev_display_id == current_display_id:
            current_ad_rate_pairs.append((current_ad_id, current_rate))
        else:
            repairs_result.append((prev_display_id, current_ad_rate_pairs))
            prev_display_id = current_display_id
            current_ad_rate_pairs = [(current_ad_id, current_rate)]
    return repairs_result


def merge_result_file(result_folder, output_file):
    out_stream = open(output_file, 'w')
    list_file = get_list_of_file(result_folder)
    prev_last_line = None
    prev_last_display_id = None
    repair_ranks = load_inaccurate_line_and_repair()
    for filename in list_file:
        in_stream = open(filename, 'r')
        lines = in_stream.readlines()
        first_line = lines[0]
        done_lines = lines[1:-1]
        last_line = lines[-1]
        if prev_last_display_id is None:
            out_stream.write(first_line)
        else:
            first_display_id = int(first_line.split(sep=',')[0])
            if first_display_id == prev_last_display_id:
                # TODO Need ad_rate_pairs
                find_ad_rate_pair = [x[1] for x in repair_ranks if x[0] == first_display_id]
                if len(find_ad_rate_pair) > 0:
                    write_ranking_recommend_to_file(out_stream, first_display_id, find_ad_rate_pair[0])
                    out_stream.write('\n')
                else:
                    print('*** something error prev: ', prev_last_display_id)
                    print('line: ',first_line)
            else:
                out_stream.write(prev_last_line)
                out_stream.write('\n')
                out_stream.write(first_line)
        for line in done_lines:
            out_stream.write(line)
        prev_last_line = last_line
        prev_last_display_id = int(last_line.split(sep=',')[0])
        in_stream.close()
    out_stream.close()


if __name__ == '__main__':
    start_time = time.time()
    job_queue = Queue()
    init_queue(job_queue)

    number_of_process = 4
    procs = []
    for i in range(number_of_process):
        proc = Process(target=sort_each_file_with_queue, args=(job_queue, ))
        proc.start()
        procs.append(proc)

    for p in procs:
        p.join()
    print('Group result Success: ', (time.time() - start_time))

    print('Start merging result ...')
    start_time = time.time()
    merge_result_file(output_folder, final_output_file)
    print('Merge Success: ', (time.time()-start_time), ' s')


