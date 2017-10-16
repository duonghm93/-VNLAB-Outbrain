import pandas as pd
import numpy as np
import constant
from sklearn.feature_extraction import FeatureHasher
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle


def convert_feature(hasher, df, field_name):
    df_tmp = pd.DataFrame(hasher.fit_transform(df[field_name]).toarray())
    df_tmp = df_tmp.reset_index(drop=True)
    return df_tmp

if __name__ == '__main__':
    # dfs = pd.read_csv(
    #     constant.get_train_merge_file(), nrows=1000000, chunksize=100000,
    #     dtype={
    #         'clicked':int, 'display_id':object, 'ad_id':object, 'uuid':object, 'document_id': object, 'time_stamp':int, 'platform':object,
    #         'geo_location':object, 'source_id':object, 'publisher_id':object, 'campaign_id':object, 'advertiser_id':object}
    # )

    df_data = []
    hasher = FeatureHasher(n_features=20, input_type='string', non_negative=True)
    model = LinearRegression()

    # for df in pd.read_csv(constant.get_train_merge_file(), nrows=1000000, chunksize=10000, dtype={
    #     'clicked': int, 'display_id':object, 'ad_id':object, 'uuid':object, 'document_id':object, 'time_stamp':int, 'platform':object,
    #     'geo_location': object, 'source_id':object, 'publisher_id':object, 'campaign_id':object, 'advertiser_id':object
    # }):
    df = pd.read_csv(constant.get_train_merge_file(), nrows=100000, dtype={
        'clicked': int, 'display_id': object, 'ad_id': object, 'uuid': object, 'document_id': object,
        'time_stamp': int, 'platform': object,
        'geo_location': object, 'source_id': object, 'publisher_id': object, 'campaign_id': object,
        'advertiser_id': object
    })
    print('Training ...')
    label = df['clicked']
    label = label.reset_index(drop=True)
    display_id = convert_feature(hasher, df, 'display_id')
    ad_id = convert_feature(hasher, df, 'ad_id')
    uuid = convert_feature(hasher, df, 'uuid')
    platform = convert_feature(hasher, df, 'platform')
    # geo_location = convert_feature(hasher, df, 'geo_location')
    source_id = convert_feature(hasher, df, 'source_id')
    publisher_id = convert_feature(hasher, df, 'publisher_id')
    campaign_id = convert_feature(hasher, df, 'campaign_id')
    advertiser_id = convert_feature(hasher, df, 'advertiser_id')

    df_data = pd.concat([label, display_id, ad_id, uuid, platform, source_id, publisher_id, campaign_id, advertiser_id], axis=1)
    X = df_data.drop(['clicked'], axis=1)
    Y = df_data['clicked']
    model.fit(X, Y)

    pickle.dump(model, open('D:/lir_hashing_feature.model', 'wb'))
    print('Training done')


