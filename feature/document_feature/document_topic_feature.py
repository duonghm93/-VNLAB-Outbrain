from sklearn.preprocessing import LabelBinarizer
import operator


class DocumentTopicFeatureGenerator:
    def __init__(self, df_document_topic):
        self.df_document_topic = df_document_topic
        self.vectorizer = LabelBinarizer()
        self.vectorizer.fit(self.df_document_topic['topic_id'].values)

    def get_df_document_topic(self):
        return self.df_document_topic

    def __get_topic_confidence_from_document_id_and_topic_id(self, document_id, topic_id):
        df = self.get_df_document_topic()
        result = df[(df['document_id']==document_id) & (df['topic_id']==topic_id)]['confidence_level']
        if len(result) > 0:
            return result.values[0]
        else:
            return 0

    def __get_topics_from_document_id(self, document_id):
        df = self.get_df_document_topic()
        return list(df[df['document_id'] == document_id]['topic_id'].values)

    def get_feature(self, document_id):
        topics = self.__get_topics_from_document_id(document_id)
        if len(topics) > 0:
            features = []
            for topic_id in topics:
                topic_vector = self.vectorizer.transform([topic_id])
                topic_confidence = self.__get_topic_confidence_from_document_id_and_topic_id(document_id, topic_id)
                features.append(topic_confidence*topic_vector)
            feature = [sum(x) for x in zip(*features)]
            return list(feature[0])
        else:
            return [0] * len(self.vectorizer.classes_)
