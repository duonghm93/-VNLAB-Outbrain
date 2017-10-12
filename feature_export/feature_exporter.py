import constant
import pandas as pd
from feature.document_feature import DocumentCategoryFeatureGenerator, DocumentTopicFeatureGenerator
import time


class FeatureExporter:
    def __init__(self, df_merge_data):
        self.__df__merge__data = df_merge_data

    def __get__df__merge__data(self):
        return self.__df__merge__data

    def export_features_from_field(self, field_to_extract, feature_generator, export_file):
        features = self.__get__df__merge__data()[field_to_extract].apply(lambda field: feature_generator.get_feature(field))
        features.to_csv(export_file, index=False)


if __name__ == '__main__':
    print('Load sample data ...')
    df_sample_data = pd.read_csv(constant.get_sample_file())

    print('Load document_category data ...')
    df_document_category = pd.read_csv(constant.get_document_categories_sample_file(), header=0)
    doc_category_feature_gen = DocumentCategoryFeatureGenerator(df_document_category)

    print('Load document_topic data ...')
    df_document_topic = pd.read_csv(constant.get_document_topic_sample_file(), header=0)
    doc_topic_feature_gen = DocumentTopicFeatureGenerator(df_document_topic)

    print('Starting export document_category feature...')
    start_time = time.time()
    feature_exporter = FeatureExporter(df_sample_data)
    feature_exporter.export_features_from_field(
        constant.DOCUMENT_ID_COLUMN_NAME, doc_category_feature_gen,
        constant.get_document_category_encoding_feature_file()
    )
    print('Finish export document_category_feature:', (time.time()-start_time))

    print('Starting export document_topic feature...')
    start_time = time.time()
    feature_exporter = FeatureExporter(df_sample_data)
    feature_exporter.export_features_from_field(
        constant.DOCUMENT_ID_COLUMN_NAME, doc_category_feature_gen,
        constant.get_document_topic_encoding_feature_file()
    )
    print('Finish export document_topic_feature:', (time.time() - start_time))
