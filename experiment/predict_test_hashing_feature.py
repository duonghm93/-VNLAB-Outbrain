import pandas as pd
import pickle
import constant
import sklearn
import time
from sklearn.feature_extraction import FeatureHasher


def convert_feature(hasher, df, field_name):
    df_tmp = pd.DataFrame(hasher.fit_transform(df[field_name]).toarray())
    df_tmp = df_tmp.reset_index(drop=True)
    return df_tmp


if __name__ == '__main__':
    start_time = time.time()
    print('Loading model ...')
    model = pickle.load(open('D:/lir_hashing_feature.model', 'rb'))
    hasher = FeatureHasher(n_features=20, input_type='string', non_negative=True)

    test_file = constant.get_test_merge_file()
    i=0
    print('Start predict test')
    for df in pd.read_csv(test_file, header=0, chunksize=100000, dtype={
        'clicked': int, 'display_id':object, 'ad_id':object, 'uuid':object, 'document_id':object, 'time_stamp':int, 'platform':object,
        'geo_location': object, 'source_id':object, 'publisher_id':object, 'campaign_id':object, 'advertiser_id':object
    }):
        print('Predict pack',i)

        display_id = convert_feature(hasher, df, 'display_id')
        ad_id = convert_feature(hasher, df, 'ad_id')
        uuid = convert_feature(hasher, df, 'uuid')
        platform = convert_feature(hasher, df, 'platform')
        # geo_location = convert_feature(hasher, df, 'geo_location')
        source_id = convert_feature(hasher, df, 'source_id')
        publisher_id = convert_feature(hasher, df, 'publisher_id')
        campaign_id = convert_feature(hasher, df, 'campaign_id')
        advertiser_id = convert_feature(hasher, df, 'advertiser_id')
        df_data = pd.concat([display_id, ad_id, uuid, platform, source_id, publisher_id, campaign_id, advertiser_id], axis=1)

        predict = model.predict(df_data)
        df_result = df[[constant.DISPLAY_ID_COLUMN_NAME, constant.AD_ID_COLUMN_NAME]]
        df_result = df_result.reset_index(drop=True)
        df_predict = pd.DataFrame(predict)
        df_result = pd.concat([df_result, df_predict], axis=1)
        out_filename = constant.get_predict_result_folder() + constant.PREDICT_RESULT_FILE_PREFIX + str(i).zfill(5)
        df_result.to_csv(out_filename, index=None, header=None)
        i=i+1

    print('Predict done:',time.time()-start_time)