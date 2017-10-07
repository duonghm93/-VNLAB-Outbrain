import time

import pandas as pd

from constant import *
from feature import FeatureGenerator
from training_module import TrainingDataGenerator

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



if __name__ == '__main__':
    start_program_time = time.time()
    print('=== Start creating feature')
    start_time = time.time()
    feature_generator = FeatureGenerator(df_events, df_document_topic)
    training_data_generator = TrainingDataGenerator(df_raw_train, feature_generator)
    df_new_train_data = training_data_generator.generate_training_data()
    print('=== Finish creating feature', (time.time()-start_time))

    X = list(df_new_train_data[DEFAULT_FEATURE_COLUMN_NAME].values)
    Y = list(df_new_train_data[DEFAULT_LABEL_COLUMN_NAME].values)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

    print('=== Start training model')
    start_time = time.time()
    lr = LinearRegression()
    lr.fit(X_train, Y_train)
    print('=== Finish training model', (time.time()-start_time))

    print('Start evaluate')
    start_time = time.time()
    print(lr.score(X_test, Y_test))
    print('=== Finish evaluate', time.time()-start_time)

    print('EXIT SUCCESS:',(time.time()-start_program_time))