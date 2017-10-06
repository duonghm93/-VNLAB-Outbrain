import time

import pandas as pd

from constant import *
from feature.document_feature.document_topic_feature import DocumentTopicFeatureGenerator
from feature.document_feature import DocumentFeatureGenerator
from feature.ad_feature import AdFeatureGenerator
from feature.user_feature import UserFeatureGenerator

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


train_file = get_train_sample_file()
events_file = get_events_sample_file()
# page_views_file = get_page_view_sample_file()
# document_meta_file = get_document_meta_sample_file()
document_topic_file = get_document_topic_sample_file()
# document_entities_file = get_document_entities_sample_file()
# document_categories_file = get_document_categories_sample_file()
# promoted_content_file = get_promoted_content_sample_file()
#
df_raw_train = pd.read_csv(train_file, header=0)
df_events = pd.read_csv(events_file, header=0)
# df_page_views = pd.read_csv(page_views_file, header=0)
# df_document_meta = pd.read_csv(document_meta_file, header=0)
df_document_topic = pd.read_csv(document_topic_file, header=0)
# df_document_entities = pd.read_csv(document_entities_file, header=0)
# df_document_categories = pd.read_csv(document_categories_file, header=0)
# df_promoted_content = pd.read_csv(promoted_content_file, header=0)

document_feature_generator = DocumentFeatureGenerator(df_document_topic)
user_feature_generator = UserFeatureGenerator()
ad_feature_generator = AdFeatureGenerator()


def convert_recommendation_pair_to_feature(display_id, ad_id, df_part_events):
    display_id_row_info = df_part_events.loc[df_part_events['display_id'] == display_id]
    user_feature = None
    document_feature = None
    ad_feature = None
    if len(display_id_row_info) > 0:
        uuid = display_id_row_info['uuid'].values[0]
        document_id = display_id_row_info['document_id'].values[0]
        document_feature = document_feature_generator.get_feature(document_id)
        user_feature = user_feature_generator.get_feature(uuid)
        ad_feature = ad_feature_generator.get_feature(ad_id)
    else:
        pass
    return [document_feature, ad_feature]

if __name__ == '__main__':
    start_time = time.time()
    new_train_data = []
    for index, row in df_raw_train.iterrows():
        display_id = row['display_id']
        ad_id = row['ad_id']
        clicked = row['clicked']
        feature = convert_recommendation_pair_to_feature(display_id, ad_id, df_events)
        if feature != [None, None, None]:
            new_train_data.append([feature[0], feature[1], feature[2], clicked])
    df_new_train_data = pd.DataFrame(new_train_data)
    df_new_train_data.columns = ['user_feature', 'document_feature', 'ad_feature', 'clicked']

    X = df_new_train_data[['user_feature', 'document_feature', 'ad_feature']]
    Y = df_new_train_data['clicked']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

    lr = LinearRegression()
    lr.fit(X_train, Y_train)
    print('EXIT SUCCESS:',(time.time()-start_time))