import timeimport pandas as pdfrom os import listdir# import threadingfrom multiprocessing import Process, Queueinput_folder = 'D:/outbrain/sample_test/'output_folder = 'D:/outbrain/output/'TEST_FILE_PREFIX = 'test'def get_rate_by_ad_id(df, ad_id):    result = df.loc[df['ad_id'] == ad_id]['clicked_rate'].values    if len(result) > 0:        return result[0]    else:        return 0def get_list_of_file(root_folder):    list_file = listdir(root_folder)    list_file = list(filter(lambda x: x.startswith(TEST_FILE_PREFIX), list_file))    list_file_full = list(map(lambda x: root_folder + x, list_file))    return list_file_fullad_rate_df = pd.read_csv('E:/outbrain/ad_simple_rate.csv')def map_ad_rate(queue_job):    while not queue_job.empty():        start_time = time.time()        input_file = queue_job.get()        print('Start process: ', input_file)        filename = input_file.split('/')[-1]        output_file = output_folder + filename        in_stream = open(input_file, "r")        out_stream = open(output_file, 'w')        for line in in_stream:            recom_raw = line.split(sep=',')            display_id = int(recom_raw[0])            ad_id = int(recom_raw[1])            ad_rate = get_rate_by_ad_id(ad_rate_df, ad_id)            out_stream.write('{0},{1},{2}\n'.format(display_id, ad_id, ad_rate))        in_stream.close()        out_stream.close()        process_time = time.time() - start_time        print('Finish process: ', input_file, ' - ', process_time, ' s')def init_queue(queue_job):    list_file = get_list_of_file(input_folder)    for file in list_file:        queue_job.put(file)if __name__ == '__main__':    start_time = time.time()    job_queue = Queue()    init_queue(job_queue)    number_of_process = 4    procs = []    for i in range(number_of_process):        proc = Process(target=map_ad_rate, args=(job_queue,))        proc.start()        procs.append(proc)    for p in procs:        p.join()    print('Exit Success: ', (time.time()-start_time))