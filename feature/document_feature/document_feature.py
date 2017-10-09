from feature.document_feature.document_topic_feature import DocumentTopicFeatureGenerator
from feature.document_feature.document_category_feature import DocumentCategoryFeatureGenerator


class DocumentFeatureGenerator:
    def __init__(self, document_feature_generators):
        self.document_feature_generators = document_feature_generators
        pass

    def get_feature(self, document_id):
        features = []
        for generator in self.document_feature_generators:
            features = features + generator.get_feature(document_id)
        return features
