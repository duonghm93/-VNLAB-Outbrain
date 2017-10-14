import pandas as pd
import pickle
import constant
import sklearn
import time

if __name__ == '__main__':
    start_time = time.time()
    print('Loading model ...')
    model = pickle.load(open(constant.get_sgd_model_file(), 'rb'))

    test_file = constant.get_test_merge_file()
    i=0
    print('Start predict test')
    for df in pd.read_csv(test_file, header=0, chunksize=100000):
        print('Predict pack',i)
        df = df.drop([constant.DOCUMENT_GEO_LOCATION_COLUMN_NAME, constant.USER_ID_COLUMN_NAME], axis=1)
        df_scale = pd.DataFrame(sklearn.preprocessing.scale(df), columns=df.columns)
        predict = model.predict(df_scale)
        df_result = df[[constant.DISPLAY_ID_COLUMN_NAME, constant.AD_ID_COLUMN_NAME]]
        df_result = df_result.reset_index(drop=True)
        df_predict = pd.DataFrame(predict)
        df_result = pd.concat([df_result, df_predict], axis=1)
        out_filename = constant.get_predict_result_folder() + constant.PREDICT_RESULT_FILE_PREFIX + str(i).zfill(5)
        df_result.to_csv(out_filename, index=None, header=None)
        i=i+1

    print('Predict done:',time.time()-start_time)
