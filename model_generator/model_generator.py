from sklearn.linear_model import LinearRegression
import constant
import pandas as pd
import pickle


class ModelGenerator:
    def __init__(self, model, df_train_data, df_features, ignore_fields_names, label_field_name = 'clicked'):
        self.__model__ = model
        self.__df__train__data__ = df_train_data
        self.__ignore__fields__names__ = ignore_fields_names
        self.__label__field__name__ = label_field_name
        self.__init__features__(df_features)

    def __get__model__(self):
        return self.__model__

    def __get__df__train__data__(self):
        return self.__df__train__data__

    def __get__ignore__fields__names__(self):
        return self.__ignore__fields__names__ + [self.__get__label__field__name__()]

    def __get__label__field__name__(self):
        return self.__label__field__name__

    def __init__features__(self, df_features):
        for df_feature in df_features:
            df_converted_feature = pd.DataFrame(df_feature[0].values.tolist())
            self.__df__train__data__ = pd.concat([self.__df__train__data__, df_converted_feature], axis=1)

    def train(self):
        train_data = self.__df__train__data__.drop(self.__get__ignore__fields__names__())
        label_data = self.__df__train__data__[self.__get__label__field__name__()]
        self.__model__.fit(train_data, label_data)

    def export_merge(self, model_file_path):
        os = open(model_file_path, 'wb')
        pickle.dump(self.__get__model__(), os)
        os.close()

if __name__ == '__main__':
    pass