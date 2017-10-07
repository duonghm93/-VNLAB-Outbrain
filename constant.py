DATA_FOLDER = 'E:/outbrain/'

TRAIN_FOLDER = 'clicks_train.csv/'
TRAIN_FILE = 'clicks_train.csv'
TRAIN_FILE_SAMPLE = 'clicks_train_sample.csv'

TEST_FOLDER = 'clicks_test.csv/'
TEST_FILE = 'clicks_test.csv'
TEST_FILE_SAMPLE = 'clicks_test_sample.csv'

EVENTS_FOLDER = 'events.csv/'
EVENTS_FILE = 'events.csv'
EVENTS_FILE_SAMPLE = 'events_sample.csv'

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


def get_train_file():
    return DATA_FOLDER + TRAIN_FOLDER + TRAIN_FILE


def get_train_sample_file():
    return DATA_FOLDER + TRAIN_FOLDER + TRAIN_FILE_SAMPLE


def get_test_file():
    return DATA_FOLDER + TEST_FOLDER + TEST_FILE


def get_test_sample_file():
    return DATA_FOLDER + TEST_FOLDER + TEST_FILE_SAMPLE


def get_events_file():
    return DATA_FOLDER + EVENTS_FOLDER + EVENTS_FILE


def get_events_sample_file():
    return DATA_FOLDER + EVENTS_FOLDER + EVENTS_FILE_SAMPLE


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
