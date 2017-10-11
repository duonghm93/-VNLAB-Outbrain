import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.feature_extraction import FeatureHasher
from feature.document_feature import DocumentTopicFeatureGenerator
from feature.document_feature import DocumentCategoryFeatureGenerator

from constant import get_sample_file
import time


def get_topic_feature_from_document_id(document_id, df_documents_topics):
    search_results = df_documents_topics[df_documents_topics['document_id'] == document_id]
    if len(search_results) > 0:
        topic_feature = []
        for index, row in search_results.iterrows():
            topic_id = int(row['topic_id'])
            confidence_level = float(row['confidence_level'])
            topic_feature.append((topic_id, confidence_level))
        return topic_feature
    else:
        return None


def get_category_feature_from_document_id(document_id, df_documents_categories):
    search_results = df_documents_categories[df_documents_categories['document_id'] == document_id]
    if len(search_results) > 0:
        category_feature = []
        for index, row in search_results.iterrows():
            topic_id = int(row['category_id'])
            confidence_level = float(row['confidence_level'])
            category_feature.append((topic_id, confidence_level))
        return category_feature
    else:
        return None


def get_entity_feature_from_document_id(document_id, df_documents_entities):
    search_results = df_documents_entities[df_documents_entities['document_id'] == document_id]
    if len(search_results) > 0:
        entity_feature = []
        for index, row in search_results.iterrows():
            entity_id = row['entity_id']
            confidence_level = float(row['confidence_level'])
            entity_feature.append((entity_id, confidence_level))
        return entity_feature
    else:
        return None

if __name__ == '__main__':
    sample_filename = get_sample_file()
    df = pd.read_csv(sample_filename, header=0)


    # df_documents_categories = df_documents_categories.groupby('document_id', as_index=False).agg(lambda x: [x])
    # df_documents_entities = df_documents_entities.groupby('document_id', as_index=False).agg(lambda x: [x])

    # Convert uuid to feature
    df_events = pd.read_csv('D:/outbrain/SAMPLE_DATA/events_sample.csv', header=0)
    uuid_hasher = FeatureHasher(n_features=25, input_type='string')
    uuids = map(lambda x: x, set(df_events['uuid'].values))
    uuid_hasher.fit(uuids)
    df['uuid_convert'] = df['uuid'].apply(lambda x: uuid_hasher.transform([x]).toarray()[0])
    uuid_feature = pd.DataFrame(df['uuid_convert'].values.tolist())
    data = pd.concat([df.drop(['uuid','geo_location', 'uuid_convert'], axis=1),uuid_feature], axis=1)

    # Get topic data from document_id
    start_time = time.time()
    df_documents_topics = pd.read_csv('D:/outbrain/SAMPLE_DATA/documents_topics_sample.csv', header=0).sort_values(['document_id', 'topic_id'])
    dtf = DocumentTopicFeatureGenerator(df_documents_topics)
    df['document_topic'] = df['document_id'].apply(lambda x: dtf.get_feature(x))
    print('finish create topic data:',time.time()-start_time)

    # Get category data from document_id
    start_time = time.time()
    df_documents_categories = pd.read_csv('D:/outbrain/SAMPLE_DATA/documents_categories_sample.csv', header=0)
    dcf = DocumentCategoryFeatureGenerator(df_documents_categories)
    df['document_category'] = df['document_id'].apply(lambda x: dcf.get_feature(x))
    print('finish create category data:', time.time() - start_time)


    # Get entity data from document_id
    # df_documents_entities = pd.read_csv('D:/outbrain/SAMPLE_DATA/documents_entities_sample.csv', header=0)
    # start_time = time.time()
    # df['document_entity'] = df['document_id'].apply(lambda x: get_entity_feature_from_document_id(x, df_documents_entities))
    # print('finish in:', time.time() - start_time)

    X = data.drop(['clicked'], axis=1)
    Y = data['clicked']

    lr = LogisticRegression()
    result = cross_val_score(lr, X, Y, cv=7)
    print(result)
    #print(result.mean())
