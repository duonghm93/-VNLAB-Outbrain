from constant import *
import pandas as pd
import time
from multiprocessing import Process, Queue


def sample_file(data_filename, sample_filename, sample_frac = 0.2):
    print('Start sample', data_filename)
    start_time = time.time()
    chunk_size = 10 ** 6
    data_sample = pd.DataFrame()
    for df in pd.read_csv(data_filename, header=0, chunksize=chunk_size):
        sample_pd = df.sample(frac=sample_frac)
        data_sample = pd.concat([sample_pd, data_sample])
    data_sample.to_csv(sample_filename,sep=',',index=False)
    print('Finish sample',sample_filename,(time.time()-start_time))


if __name__ == '__main__':
    # sample_file(get_train_file(), get_train_sample_file())
    # sample_file(get_events_file(), get_events_sample_file())

    sample_file(get_page_view_file(), get_page_view_sample_file())
    sample_file(get_document_meta_file(), get_document_meta_sample_file())
    sample_file(get_document_topic_file(), get_document_topic_sample_file())
    sample_file(get_document_entities_file(), get_document_entities_sample_file())
    sample_file(get_document_categories_file(), get_document_categories_sample_file())
    sample_file(get_promoted_content_file(), get_promoted_content_sample_file())
    pass


