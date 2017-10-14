import pandas as pd
from model_generator import ModelGenerator
from custom_verify import CustomVerifier
from sklearn.linear_model import SGDRegressor
from sklearn.neural_network import MLPRegressor
import constant
import time

if __name__ == '__main__':
    start_program_time = time.time()
    train_file_name = constant.get_train_merge_file()
    sgd_model = SGDRegressor()
    model_generator = ModelGenerator(
        model=sgd_model, df_features=[],
        ignore_fields_names=[constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME],
        label_field_name=constant.CLICKED_COLUMN_NAME
    )
    print('Loading training data and Training ...')
    start_time = time.time()
    for df in pd.read_csv(train_file_name, header=0, chunksize=100000):
        print('- Training ...')
        model_generator.set_train_data(df)
        model_generator.partial_train()
    print('Finish training:', time.time()-start_time)

    model = model_generator.get_model()
    print('Exporting model ...')
    model_generator.export_model(constant.get_sgd_model_file())

    print('Loading testing data ...')
    df_test = pd.read_csv(constant.get_sample_file(), header=0, nrows=100000)
    X_test = df_test.drop([constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME, constant.CLICKED_COLUMN_NAME], axis=1)
    Y_test = df_test[constant.CLICKED_COLUMN_NAME]

    print('Predicting ...')
    start_time = time.time()
    predict = model.predict(X_test)
    print('Finish predict:',time.time()-start_time)

    print('Verifying ...')
    start_time = time.time()
    verifier = CustomVerifier(df_test=df_test, prob_result=predict,
                              label_field_name=constant.CLICKED_COLUMN_NAME,
                              group_field_name=constant.DOCUMENT_ID_COLUMN_NAME,
                              result_field_name='prob')

    verifier.verify()
    print('Finish verify:',time.time()-start_time)
    print('EXIT SUCCESS:',time.time() - start_program_time)


