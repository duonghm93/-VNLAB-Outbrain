from feature.document_feature.document_topic_feature import DocumentTopicFeatureGenerator
import pandas as pd
import unittest


class DocumentTopicFeatureTestCase(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('../df_test/documents_topic_sample.csv')
        self.dtf = DocumentTopicFeatureGenerator(self.df)

    def test_document_topic_feature_exist_document_id(self):
        document_id = 1595802
        feature = self.dtf.get_feature(document_id)
        print(feature)
        self.assertEqual(len(feature), len(self.dtf.vectorizer.classes_))

    def test_document_topic_feature_non_exist_document_id(self):
        document_id = 0
        feature = self.dtf.get_feature(document_id)
        print(feature)
        self.assertEqual(len(feature), len(self.dtf.vectorizer.classes_))