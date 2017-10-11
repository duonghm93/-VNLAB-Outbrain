from statistical_feature import StatisticalFeatureGenerator
import pandas as pd
import constant
import time

if __name__ == '__main__':
    program_start_time = time.time()
    df = pd.read_csv(constant.get_sample_file(), header=0)
    df_merge_train = pd.read_csv(constant.get_sample_file(), header=0)
    df_page_view = pd.read_csv('D:/outbrain/page_view_sample_merge_data.csv', header=0)

    statisticFeatureGen = StatisticalFeatureGenerator(df_merge_train, df_page_view)
    print('start extract document feature ... ')
    start_time = time.time()
    df['document_feature'] = df['document_id'].apply(lambda docId: statisticFeatureGen.get_doc_feature_from_doc_id(docId))
    df['document_feature'].to_csv('D:/outbrain/statisticFeature/document.csv', index=False)
    print('Finish extract document feature:',time.time()-start_time)

    print('start extract user feature ... ')
    start_time = time.time()
    df['user_feature'] = df['uuid'].apply(lambda uuid: statisticFeatureGen.get_user_feature_from_user_id(uuid))
    df['user_feature'].to_csv('D:/outbrain/statisticFeature/user.csv', index=False)
    print('Finish extract user feature:', time.time() - start_time)

    print('start extract ad feature ... ')
    start_time = time.time()
    df['ad_feature'] = df['ad_id'].apply(lambda adid: statisticFeatureGen.get_ad_feature_from_ad_id(adid))
    df['ad_feature'].to_csv('D:/outbrain/statisticFeature/ad.csv', index=False)
    print('Finish extract ad feature:', time.time() - start_time)

    print('EXIT SUCCESS:',time.time()-program_start_time)