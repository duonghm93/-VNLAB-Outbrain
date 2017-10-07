from feature.document_feature import DocumentFeatureGenerator
import pandas as pd
import unittest

class DocumentFeatureTestcase(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('../test_data/documents_topic_sample.csv')
        self.dfg = DocumentFeatureGenerator(self.df)


    def test_document_feature_exist_document_id(self):
        document_id = 1595802
        feature = self.dfg.get_feature(document_id)
        print(feature)
        self.assertEqual(len(feature), )