from feature.document_feature.document_topic_feature import DocumentTopicFeatureGenerator


class DocumentFeatureGenerator:
    def __init__(self, df_document_topic):
        self.document_topic_feature = DocumentTopicFeatureGenerator(df_document_topic)
        pass

    def get_feature(self, document_id):
        return self.document_topic_feature.get_feature(document_id)
