import time

import pandas as pd

import constant
from feature import FeatureGenerator
from feature.document_feature import DocumentCategoryFeatureGenerator, DocumentTopicFeatureGenerator
from training_module import TrainingDataGenerator

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, cross_val_score

from multiprocessing import Manager, Process
import multiprocess_util

import ast
import pickle


train_file = constant.get_train_sample_file()
events_file = constant.get_events_sample_file()
# page_views_file = constant.get_page_view_sample_file()
# document_meta_file = constant.get_document_meta_sample_file()
document_topic_file = constant.get_document_topic_sample_file()
# document_entities_file = constant.get_document_entities_sample_file()
document_categories_file = constant.get_document_categories_sample_file()
# promoted_content_file = constant.get_promoted_content_sample_file()
#
df_raw_train = pd.read_csv(train_file, header=0)
df_events = pd.read_csv(events_file, header=0)
# df_page_views = pd.read_csv(page_views_file, header=0)
# df_document_meta = pd.read_csv(document_meta_file, header=0)
df_document_topic = pd.read_csv(document_topic_file, header=0)
# df_document_entities = pd.read_csv(document_entities_file, header=0)
df_document_categories = pd.read_csv(document_categories_file, header=0)
# df_promoted_content = pd.read_csv(promoted_content_file, header=0)


def process_generate_train_data(queue_job, feature_gen):
    while not queue_job.empty():
        part_file = queue_job.get()
        print('Process',part_file)
        df_train_part = pd.read_csv(part_file)
        df_train_part.columns = \
            [constant.DISPLAY_ID_COLUMN_NAME, constant.AD_ID_COLUMN_NAME, constant.CLICKED_COLUMN_NAME]
        training_data_generator = TrainingDataGenerator(df_train_part, feature_gen)
        train_data_part = training_data_generator.generate_training_data()

        file_name = part_file.split('/')[-1]
        file_name = constant.get_train_sample_Feature_folder() + file_name
        train_data_part.to_csv(file_name, sep=',', index=None, header=None)
        # X_part = list(train_data_part[constant.DEFAULT_FEATURE_COLUMN_NAME].values)
        # Y_part = list(train_data_part[constant.DEFAULT_LABEL_COLUMN_NAME].values)


if __name__ == '__main__':
    start_program_time = time.time()

    # === Create feature from separated train data ===
    document_topic_generator = DocumentTopicFeatureGenerator(df_document_topic)
    document_category_generator = DocumentCategoryFeatureGenerator(df_document_categories)
    document_feature_generators = [document_topic_generator]
    feature_generator = FeatureGenerator(df_events, document_feature_generators)

    queue_job = multiprocess_util.create_queue_job(constant.get_train_sample_folder(), prefix='train')

    processes = []
    for i in range(constant.NUMBER_OF_PROCESSES):
        process = Process(target=process_generate_train_data, args=(queue_job, feature_generator, ))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    # === Train Linear Regression Model ===
    X = []
    Y = []
    feature_files = multiprocess_util.get_list_of_file(constant.get_train_sample_Feature_folder(), prefix='train')
    for feature_file in feature_files:
        print('Load',feature_file)
        df = pd.read_csv(feature_file, header=None, converters={0:ast.literal_eval, 1:ast.literal_eval})
        df.columns = [constant.DEFAULT_FEATURE_COLUMN_NAME, constant.DEFAULT_LABEL_COLUMN_NAME]
        X_part = list(df[constant.DEFAULT_FEATURE_COLUMN_NAME].values)
        Y_part = list(df[constant.DEFAULT_LABEL_COLUMN_NAME].values)
        X = X + X_part
        Y = Y + Y_part

    # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

    # print('=== Start training model')
    # start_time = time.time()
    model = LinearRegression()
    # model = LogisticRegression()
    # model = SVR(kernel='linear', C=1e3)
    # model.fit(X_train, Y_train)

    # print('=== Finish training model', (time.time()-start_time))
    # pickle.dump(model, open(constant.get_linear_regression_model_file(), 'wb'))

    # === Evaluate model ===
    # lr_model = pickle.load(open(constant.get_linear_regression_model_file(), 'rb'))
    print('Start evaluate')
    start_time = time.time()
    scores = cross_val_score(model, X, Y, cv=5)
    print(scores)
    print(scores.mean(), scores.std())
    # print(model.score(X_test, Y_test))
    print('=== Finish evaluate', time.time()-start_time)

    print('EXIT SUCCESS:',(time.time()-start_program_time))