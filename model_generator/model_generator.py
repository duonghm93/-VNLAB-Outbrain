from sklearn.linear_model import LinearRegression, SGDRegressor
import constant
import pandas as pd
from custom_verify.custom_verifier import CustomVerifier
from sklearn.neural_network import MLPRegressor
import pickle


class ModelGenerator:
    def __init__(self, model, df_train_data = None, df_features = [], ignore_fields_names = [], label_field_name = 'clicked'):
        self.__model__ = model
        self.__df__train__data__ = df_train_data
        self.__ignore__fields__names__ = ignore_fields_names
        self.__label__field__name__ = label_field_name
        self.__init__features__(df_features)

    def get_model(self):
        return self.__model__

    def set_train_data(self, df_train_data):
        self.__df__train__data__ = df_train_data

    def set_df_features(self, df_features):
        self.__init__features__(df_features)

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

    def train_all(self):
        train_data = self.__df__train__data__.drop(self.__get__ignore__fields__names__(), axis=1)
        label_data = self.__df__train__data__[self.__get__label__field__name__()]
        self.__model__.fit(train_data, label_data)

    def partial_train(self):
        train_data = self.__df__train__data__.drop(self.__get__ignore__fields__names__(), axis=1)
        label_data = self.__df__train__data__[self.__get__label__field__name__()]
        self.__model__.partial_fit(train_data, label_data)

    def export_model(self, model_file_path):
        os = open(model_file_path, 'wb')
        pickle.dump(self.get_model(), os)
        os.close()

if __name__ == '__main__':
    sample_file_name = constant.get_sample_file()
    model_file = 'E:/sample_model.model'

    df_sample_data = pd.read_csv(sample_file_name)

    total_size = df_sample_data.shape[0]
    split_rate = 0.7
    train_size = int(split_rate * total_size)
    df_train = df_sample_data.iloc[:train_size, :]
    df_test = df_sample_data.iloc[train_size:, :]

    X_test = df_test.drop([constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME, constant.CLICKED_COLUMN_NAME], axis=1)
    Y_test = df_test[constant.CLICKED_COLUMN_NAME]

    # model = LinearRegression(n_jobs=-1) # Not support partial fit
    model = SGDRegressor(penalty='l2')
    # model = MLPRegressor()

    model_generator = ModelGenerator(
        model=model, df_train_data=df_train, df_features=[],
        ignore_fields_names=[constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME],
        label_field_name=constant.CLICKED_COLUMN_NAME
    )
    model_generator.train_all()
    # model_generator.export_merge(model_file)
    model = model_generator.get_model()
    # model = pickle.load(open(model_file, 'rb'))

    predict = model.predict(X_test)

    verifier = CustomVerifier(df_test=df_test, prob_result=predict,
                              label_field_name=constant.CLICKED_COLUMN_NAME,
                              group_field_name=constant.DOCUMENT_ID_COLUMN_NAME,
                              result_field_name='prob')

    verifier.verify()
