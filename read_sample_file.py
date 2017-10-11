import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.feature_extraction import FeatureHasher

from constant import get_sample_file


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


def get_hash_feature(uuid, hasher):
    return hasher.transform([uuid])


if __name__ == '__main__':
    sample_filename = get_sample_file()
    df = pd.read_csv(sample_filename, header=0)

    df_documents_topics = pd.read_csv('D:/outbrain/SAMPLE_DATA/documents_topics_sample.csv', header=0).sort_values(['document_id', 'topic_id'])
    # df_documents_topics = df_documents_topics.groupby('document_id', as_index=False).agg(lambda x: [x])

    df_documents_categories = pd.read_csv('D:/outbrain/SAMPLE_DATA/documents_categories_sample.csv', header=0)
    # df_documents_categories = df_documents_categories.groupby('document_id', as_index=False).agg(lambda x: [x])

    df_documents_entities = pd.read_csv('D:/outbrain/SAMPLE_DATA/documents_entities_sample.csv', header=0)
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
    

    X = data.drop(['clicked'], axis=1)
    Y = data['clicked']

    lr = LogisticRegression()
    result = cross_val_score(lr, X, Y, cv=7)
    print(result)
    #print(result.mean())
