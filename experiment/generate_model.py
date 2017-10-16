import pandas as pd

from model_generator import ModelGenerator
from custom_verify import CustomVerifier
import sklearn
from sklearn.linear_model import SGDRegressor, SGDClassifier, LinearRegression
from sklearn.neural_network import MLPRegressor
import ast
import constant
import time

if __name__ == '__main__':
    start_program_time = time.time()
    train_file_name = constant.get_train_merge_file()
    model = LinearRegression()
    # model = SGDRegressor(alpha=0.0001, epsilon=0.1, eta0=0.01, fit_intercept=True, penalty='l2')
    # model = SGDClassifier(loss='log')
    model_generator = ModelGenerator(
        model=model, df_features=[],
        # ignore_fields_names=[
        #     constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME,
        # ],
        label_field_name=constant.CLICKED_COLUMN_NAME
    )
    print('Loading training data and Training ...')
    start_time = time.time()
    # for df in pd.read_csv(train_file_name, header=0, chunksize=10000):
    #     df = df.drop([constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME], axis=1)
    #     df = pd.DataFrame(sklearn.preprocessing.scale(df), columns=df.columns)
    #     print('- Training ...')
    #     model_generator.set_train_data(df)
    #     model_generator.partial_train()
    df_train = pd.read_csv(constant.get_sample_file(), header=0)
    df_train = df_train.drop([constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME], axis=1)
    # df_doc_stat_feature = pd.read_csv(constant.get_document_statistic_feature_file(), header=None, converters={0:ast.literal_eval})
    # df_ad_stat_feature = pd.read_csv(constant.get_ad_statistic_feature_file(), header=None, converters={0:ast.literal_eval})
    model_generator.set_train_data(df_train)
    # model_generator.set_df_features([df_doc_stat_feature, df_ad_stat_feature])
    model_generator.train_all()
    print('Finish training:', time.time()-start_time)

    model = model_generator.get_model()
    # print(model.coef_, model.intercept_[0])
    print('Exporting model ...')
    model_generator.export_model('D:/model_lir.model')

    # print('Loading testing data ...')
    # df_test = pd.read_csv(constant.get_sample_file(), header=0)
    # X_test = df_test.drop([constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME, constant.CLICKED_COLUMN_NAME], axis=1)
    # Y_test = df_test[constant.CLICKED_COLUMN_NAME]
    #
    # print('Predicting ...')
    # start_time = time.time()
    # predict = model.predict(X_test)
    # # predict = model.predict_proba(X_test)
    # # predict = list(map(lambda x: x[1], predict))
    # print('Finish predict:',time.time()-start_time)
    #
    # print('Verifying ...')
    # start_time = time.time()
    # verifier = CustomVerifier(df_test=df_test, prob_result=predict,
    #                           label_field_name=constant.CLICKED_COLUMN_NAME,
    #                           group_field_name=constant.DOCUMENT_ID_COLUMN_NAME,
    #                           result_field_name='prob')
    #
    # verifier.verify()
    # print('Finish verify:',time.time()-start_time)
    # print('EXIT SUCCESS:',time.time() - start_program_time)


