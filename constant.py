DATA_FOLDER = 'D:/outbrain/'

TRAIN_FOLDER = 'clicks_train.csv/'
TRAIN_SAMPLE_FOLDER = 'clicks_train.csv/sample/'
TRAIN_SAMPLE_FEATURE_FOLDER = 'clicks_train.csv/sample_feature/'
TRAIN_FEATURE_FOLDER = 'clicks_train.csv/feature/'
TRAIN_FILE = 'clicks_train.csv'
TRAIN_SAMPLE_FILE = 'clicks_train_sample.csv'

TEST_FOLDER = 'clicks_test.csv/'
TEST_FILE = 'clicks_test.csv'
TEST_SAMPLE_FILE = 'clicks_test_sample.csv'

EVENTS_FOLDER = 'events.csv/'
EVENTS_FILE = 'events.csv'
EVENTS_SAMPLE_FILE = 'events_sample.csv'

PAGE_VIEWS_FOLDER = 'page_views_sample.csv/'
PAGE_VIEWS_FILE = 'page_views_sample.csv'
PAGE_VIEWS_SAMPLE_FILE = 'page_views_sample_sample.csv'

DOCUMENT_META_FOLDER = 'documents_meta.csv/'
DOCUMENT_META_FILE = 'documents_meta.csv'
DOCUMENT_META_SAMPLE_FILE = 'documents_meta_sample.csv'

DOCUMENT_TOPIC_FOLDER = 'documents_topics.csv/'
DOCUMENT_TOPIC_FILE = 'documents_topics.csv'
DOCUMENT_TOPIC_SAMPLE_FILE = 'documents_topics_sample.csv'

DOCUMENT_ENTITIES_FOLDER = 'documents_entities.csv/'
DOCUMENT_ENTITIES_FILE = 'documents_entities.csv'
DOCUMENT_ENTITIES_SAMPLE_FILE = 'documents_entities_sample.csv'

DOCUMENT_CATEGORY_FOLDER = 'documents_categories.csv/'
DOCUMENT_CATEGORY_FILE = 'documents_categories.csv'
DOCUMENT_CATEGORY_SAMPLE_FILE = 'documents_categories_sample.csv'

PROMOTED_CONTENT_FOLDER = 'promoted_content.csv/'
PROMOTED_CONTENT_FILE = 'promoted_content.csv'
PROMOTED_CONTENT_SAMPLE_FILE = 'promoted_content_sample.csv'

STATISTIC_FEATURE_FOLDER = 'statisticFeature/'
AD_STATISTIC_FEATURE_FILE = 'ad.csv'
DOCUMENT_STATISTIC_FEATURE_FILE = 'document.csv'
USER_STATISTIC_FEATURE_FILE = 'user.csv'

ENCODING_FEATURE_FOLDER = 'encodingFeature/'
DOCUMENT_CATEGORY_ENCODING_FEATURE_FILE = 'doc_category.csv'
DOCUMENT_TOPIC_ENCODING_FEATURE_FILE = 'doc_topic.csv'


DISPLAY_ID_COLUMN_NAME = 'display_id'
AD_ID_COLUMN_NAME = 'ad_id'
AD_CAMPAIGN_ID_COLUMN_NAME = 'campaign_id'
AD_ADVERTISER_ID_COLUMN_NAME = 'advertiser_id'
CLICKED_COLUMN_NAME = 'clicked'
DOCUMENT_ID_COLUMN_NAME = 'document_id'
DOCUMENT_SOURCE_ID_COLUMN_NAME = 'source_id'
DOCUMENT_PUBLISHER_ID_COLUMN_NAME = 'publisher_id'
CONFIDENCE_LEVEL_COLUMN_NAME = 'confidence_level'
CATEGORY_ID_COLUMN_NAME = 'category_id'
USER_ID_COLUMN_NAME = 'uuid'

SAMPLE_DATA_FILE = 'sample_data.csv'

TOPIC_ID_COLUMN_NAME = 'topic_id'

DEFAULT_FEATURE_COLUMN_NAME = 'feature'
DEFAULT_LABEL_COLUMN_NAME = 'clicked'

MODEL_DATA_FOLDER = 'model_data/'
LINEAR_REGRESSION_MODEL_FILE = 'linear_regression.model'
LINEAR_SVR_MODEL_FILE = 'linear_svr.model'
POLY_SVR_MODEL_FILE = 'poly_svr.model'

DEFAULT_CLICK_RATE_OVER_APPEAR_RATE = 0.1

CHUNK_SIZE = 10**4

NUMBER_OF_PROCESSES = 4


def get_train_file():
    return DATA_FOLDER + TRAIN_FOLDER + TRAIN_FILE


def get_train_sample_file():
    return DATA_FOLDER + TRAIN_FOLDER + TRAIN_SAMPLE_FILE


def get_train_sample_folder():
    return DATA_FOLDER + TRAIN_SAMPLE_FOLDER


def get_train_sample_Feature_folder():
    return DATA_FOLDER + TRAIN_SAMPLE_FEATURE_FOLDER


def get_test_file():
    return DATA_FOLDER + TEST_FOLDER + TEST_FILE


def get_test_sample_file():
    return DATA_FOLDER + TEST_FOLDER + TEST_SAMPLE_FILE


def get_events_file():
    return DATA_FOLDER + EVENTS_FOLDER + EVENTS_FILE


def get_events_sample_file():
    return DATA_FOLDER + EVENTS_FOLDER + EVENTS_SAMPLE_FILE


def get_train_folder():
    return DATA_FOLDER + TRAIN_FOLDER


def get_test_folder():
    return DATA_FOLDER + TEST_FOLDER


def get_page_view_file():
    return DATA_FOLDER + PAGE_VIEWS_FOLDER + PAGE_VIEWS_FILE


def get_page_view_sample_file():
    return DATA_FOLDER + PAGE_VIEWS_FOLDER + PAGE_VIEWS_SAMPLE_FILE


def get_document_meta_file():
    return DATA_FOLDER + DOCUMENT_META_FOLDER + DOCUMENT_META_FILE


def get_document_meta_sample_file():
    return DATA_FOLDER + DOCUMENT_META_FOLDER + DOCUMENT_META_SAMPLE_FILE


def get_document_topic_file():
    return DATA_FOLDER + DOCUMENT_TOPIC_FOLDER + DOCUMENT_TOPIC_FILE


def get_document_topic_sample_file():
    return DATA_FOLDER + DOCUMENT_TOPIC_FOLDER + DOCUMENT_TOPIC_SAMPLE_FILE


def get_document_entities_file():
    return DATA_FOLDER + DOCUMENT_ENTITIES_FOLDER + DOCUMENT_ENTITIES_FILE


def get_document_entities_sample_file():
    return DATA_FOLDER + DOCUMENT_ENTITIES_FOLDER + DOCUMENT_ENTITIES_SAMPLE_FILE


def get_document_categories_file():
    return DATA_FOLDER + DOCUMENT_CATEGORY_FOLDER + DOCUMENT_CATEGORY_FILE


def get_document_categories_sample_file():
    return DATA_FOLDER  + DOCUMENT_CATEGORY_FOLDER + DOCUMENT_CATEGORY_SAMPLE_FILE


def get_promoted_content_file():
    return DATA_FOLDER + PROMOTED_CONTENT_FOLDER + PROMOTED_CONTENT_FILE


def get_promoted_content_sample_file():
    return DATA_FOLDER + PROMOTED_CONTENT_FOLDER + PROMOTED_CONTENT_SAMPLE_FILE


def get_linear_regression_model_file():
    return DATA_FOLDER + MODEL_DATA_FOLDER + LINEAR_REGRESSION_MODEL_FILE


def get_linear_svr_model_file():
    return DATA_FOLDER + MODEL_DATA_FOLDER + LINEAR_SVR_MODEL_FILE


def get_poly_svr_model_file():
    return DATA_FOLDER + MODEL_DATA_FOLDER + POLY_SVR_MODEL_FILE


def get_sample_file():
    return DATA_FOLDER + SAMPLE_DATA_FILE


def get_user_statistic_feature_file():
    return DATA_FOLDER + STATISTIC_FEATURE_FOLDER + USER_STATISTIC_FEATURE_FILE


def get_document_statistic_feature_file():
    return DATA_FOLDER + STATISTIC_FEATURE_FOLDER + DOCUMENT_STATISTIC_FEATURE_FILE


def get_ad_statistic_feature_file():
    return DATA_FOLDER + STATISTIC_FEATURE_FOLDER + AD_STATISTIC_FEATURE_FILE


def get_document_category_encoding_feature_file():
    return DATA_FOLDER + ENCODING_FEATURE_FOLDER + DOCUMENT_CATEGORY_ENCODING_FEATURE_FILE


def get_document_topic_encoding_feature_file():
    return DATA_FOLDER + ENCODING_FEATURE_FOLDER + DOCUMENT_TOPIC_ENCODING_FEATURE_FILE
