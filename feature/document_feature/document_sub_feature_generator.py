from email import header
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction import FeatureHasher

import pandas as pd
import constant


class DocumentSubFeatureGenerator:
    def __init__(self, df_data, field_encoder, property_field_name, document_id_field_name ='document_id', confidence_level_field_name ='confidence_level'):
        self.__df__data = df_data
        self.__encoder = field_encoder
        self.__property__field__name = property_field_name
        self.__document__id__field__name = document_id_field_name
        self.__confidence__level__field__name = confidence_level_field_name
        self.__init__encoder()

    def __init__encoder(self):
        # categories_values = self.__df__data[self.__get__property__field__name()].values
        # categories_values = list(map(lambda x: [x], categories_values))
        # print(categories_values)
        # self.__encoder.fit(categories_values)
        pass

    def __get__df__data(self):
        return self.__df__data

    def __get__document__id__field__name(self):
        return self.__document__id__field__name

    def __get__field__encoder(self):
        return self.__encoder

    def __get__property__field__name(self):
        return self.__property__field__name

    def __get__confidence__level__field__name(self):
        return self.__confidence__level__field__name

    def set_field_encoder(self, encoder):
        self.__encoder = encoder
        self.__init__encoder()

    def get_feature(self, document_id):
        df = self.__get__df__data()
        rows = df[df[self.__get__document__id__field__name()] == document_id]
        if len(rows) > 0:
            features = []
            dict = []
            for index, row in rows.iterrows():
                field_value = int(row[self.__get__property__field__name()])
                confidence_level_value = float(row[self.__get__confidence__level__field__name()])
                dict.append({str(field_value):confidence_level_value})
            features = self.__get__field__encoder().transform(dict).toarray()
            features = [sum(x) for x in zip(*features)]
            return features
        else:

            return [0] * self.__get__field__encoder().n_features


if __name__ == '__main__':

    df_doc_cat = pd.read_csv('D:/outbrain/documents_topics.csv/documents_topics_sample.csv', header=0)
    encoder = FeatureHasher(n_features=15, non_negative=True)
    doc_sub_feature_gen = DocumentSubFeatureGenerator(
        df_doc_cat, encoder,
        constant.TOPIC_ID_COLUMN_NAME, constant.DOCUMENT_ID_COLUMN_NAME, constant.CONFIDENCE_LEVEL_COLUMN_NAME
    )
    print(doc_sub_feature_gen.get_feature(1617787))