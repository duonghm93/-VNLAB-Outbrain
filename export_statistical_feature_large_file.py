from statistical_feature import StatisticalFeatureLargeFileGenerator
import pandas as pd
import constant
import time

if __name__ == '__main__':
    program_start_time = time.time()

    merge_data_file = constant.get_train_merge_file()
    page_view_file = constant.get_pageviews_mege_file()
    statisticFeatureGen = StatisticalFeatureLargeFileGenerator(
        merge_file_name=merge_data_file,
        page_view_file_name=page_view_file,
        merge_file_nrows=1,
        page_view_nrows=1,
        merge_data_chunk_size=1,
        page_view_chunk_size=1
    )

    print('start extract document feature ... ')
    start_time = time.time()
    document_feature_os = open('D:/outbrain/statisticFeature/document_large.csv', 'w')
    document_feature_os.close()
    document_feature_os = open('D:/outbrain/statisticFeature/document_large.csv', 'a+')
    for df in pd.read_csv(constant.get_test_merge_file(), header=0, chunksize=10000, nrows=10000):
        df['document_feature'] = df['document_id'].apply(lambda docId: statisticFeatureGen.get_doc_feature_from_doc_id(docId))
        df['document_feature'].to_csv(document_feature_os, index=False)
    document_feature_os.close()
    print('Finish extract document feature:',time.time()-start_time)

    print('start extract ad feature ... ')
    start_time = time.time()
    ad_feature_os = open('D:/outbrain/statisticFeature/ad_large.csv', 'w')
    ad_feature_os.close()
    ad_feature_os = open('D:/outbrain/statisticFeature/ad_large.csv', 'a+')
    for df in pd.read_csv(constant.get_test_merge_file(), header=0, chunksize=10000, nrows=10000):
        df['ad_feature'] = df['ad_id'].apply(lambda adid: statisticFeatureGen.get_ad_feature_from_ad_id(adid))
        df['ad_feature'].to_csv(ad_feature_os, index=False)
    ad_feature_os.close()
    print('Finish extract ad feature:', time.time() - start_time)

    print('EXIT SUCCESS:',time.time()-program_start_time)