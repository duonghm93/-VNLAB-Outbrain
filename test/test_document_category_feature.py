from feature.document_feature import DocumentCategoryFeatureGenerator
import pandas as pd
import unittest


class DocumentCategoryFeatureTestcase(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('../df_test/documents_categories_sample.csv')
        self.dcf = DocumentCategoryFeatureGenerator(self.df)

    def test_document_category_feature_exist_document_id(self):
        document_id = 1595802
        feature = self.dcf.get_feature(document_id)
        print(feature)
        self.assertEqual(len(feature), len(self.dcf.vectorizer.classes_))


    def test_document_category_feature_non_exist_document_id(self):
        document_id = 0
        feature = self.dcf.get_feature(document_id)
        print(feature)
        self.assertEqual(len(feature), len(self.dcf.vectorizer.classes_))