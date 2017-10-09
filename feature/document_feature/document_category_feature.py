from sklearn.preprocessing import LabelBinarizer
import constant
import operator


class DocumentCategoryFeatureGenerator:
    def __init__(self, df_document_category):
        self.df_document_category = df_document_category
        self.vectorizer = LabelBinarizer()
        self.vectorizer.fit(self.df_document_category[constant.CATEGORY_ID_COLUMN_NAME].values)

    def get_df_document_category(self):
        return self.df_document_category

    def __get_topic_confidence_from_document_id_and_catergory_id(self, document_id, category_id):
        df = self.get_df_document_category()
        result = df[(df[constant.DOCUMENT_ID_COLUMN_NAME]==document_id) & (df[constant.CATEGORY_ID_COLUMN_NAME]==category_id)][constant.CONFIDENCE_LEVEL_COLUMN_NAME]
        if len(result) > 0:
            return result.values[0]
        else:
            return 0

    def __get_categories_from_document_id(self, document_id):
        df = self.get_df_document_category()
        return list(df[df[constant.DOCUMENT_ID_COLUMN_NAME] == document_id][constant.CATEGORY_ID_COLUMN_NAME].values)

    def get_feature(self, document_id):
        # return [document_id]
        categories = self.__get_categories_from_document_id(document_id)
        if len(categories) > 0:
            features = []
            for category_id in categories:
                category_vector = self.vectorizer.transform([category_id])
                category_confidence = \
                    self.__get_topic_confidence_from_document_id_and_catergory_id(document_id, category_id)
                features.append(category_confidence * category_vector)
            feature = [sum(x) for x in zip(*features)]
            return list(feature[0])
        else:
            return [0] * len(self.vectorizer.classes_)
