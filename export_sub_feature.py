import constant
import pandas as pd
from feature_export import FeatureExporter
from feature.document_feature import DocumentSubFeatureGenerator
from sklearn.feature_extraction import FeatureHasher
import time


if __name__ == '__main__':
    print('Load sample data ...')
    df_sample_data = pd.read_csv(constant.get_sample_file())

    print('Load document_category data ...')
    df_document_category = pd.read_csv(constant.get_document_categories_sample_file(), header=0)

    print('Load document_topic data ...')
    df_document_topic = pd.read_csv(constant.get_document_topic_sample_file(), header=0)

    print('Init document category feature extractor ...')
    encoder = FeatureHasher(n_features=constant.NUMBER_OF_SUB_FEATURE_SIZE, non_negative=True)
    feature_generator = DocumentSubFeatureGenerator(
        df_data=df_document_category, field_encoder=encoder,
        property_field_name=constant.CATEGORY_ID_COLUMN_NAME,
        document_id_field_name=constant.DOCUMENT_ID_COLUMN_NAME,
        confidence_level_field_name=constant.CONFIDENCE_LEVEL_COLUMN_NAME
    )

    print('Starting export document_category feature...')
    start_time = time.time()
    feature_exporter = FeatureExporter(df_sample_data)
    feature_exporter.export_features_from_field(
        constant.DOCUMENT_ID_COLUMN_NAME, feature_generator,
        constant.get_document_category_encoding_feature_file()
    )
    print('Finish export document_category_feature:', (time.time()-start_time))

    feature_generator = DocumentSubFeatureGenerator(
        df_data=df_document_topic, field_encoder=encoder,
        property_field_name=constant.TOPIC_ID_COLUMN_NAME,
        document_id_field_name=constant.DOCUMENT_ID_COLUMN_NAME,
        confidence_level_field_name=constant.CONFIDENCE_LEVEL_COLUMN_NAME
    )
    print('Starting export document_topic feature...')
    start_time = time.time()
    feature_exporter.export_features_from_field(
        constant.DOCUMENT_ID_COLUMN_NAME, feature_generator,
        constant.get_document_topic_encoding_feature_file()
    )
    print('Finish export document_topic feature:', (time.time() - start_time))
