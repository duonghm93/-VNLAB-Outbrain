import pandas as pd

PREFIX_DATA_FOLDER = 'D:/outbrain/'
TRAIN_FOLDER = 'clicks_train.csv/'
TEST_FOLDER = 'clicks_test.csv/'

train_file = PREFIX_DATA_FOLDER + TRAIN_FOLDER + 'clicks_train.csv'
sample_train_file = PREFIX_DATA_FOLDER + TRAIN_FOLDER + 'clicks_train_sample.csv'

test_file = PREFIX_DATA_FOLDER + TEST_FOLDER + 'clicks_test.csv'
sample_test_file = PREFIX_DATA_FOLDER + TEST_FOLDER + 'clicks_test_sample.csv'

DEFAULT_COLUMNS_NAMES = ['ad_id', 'clicked_count', 'clicked_sum']
chunk_size = 10**6


def calculate_count_sum_each_ad_from_data_frame(df):
    convert_df = df[['ad_id', 'clicked']].groupby(['ad_id']).agg(['count', 'sum']).reset_index()
    convert_df.columns = DEFAULT_COLUMNS_NAMES
    return convert_df


def find_by_ad_id_from_data_frame(df, ad_id):
    return df.loc[df['ad_id'] == ad_id]


def get_rate_by_ad_id(df, ad_id):
    result = df.loc[df['ad_id'] == ad_id]['clicked_rate'].values
    if len(result) > 0:
        return result[0]
    else:
        return 0


if __name__ == '__main__':
    #all_data = pd.DataFrame()
    #for df in pd.read_csv(train_file, chunksize=chunk_size):
    #    df_calculated = calculate_count_sum_each_ad_from_data_frame(df)
    #    all_data = pd.concat([all_data, df_calculated])

    #all_data_group = all_data.groupby(['ad_id']).sum().reset_index()
    #all_data_group['clicked_rate'] = all_data_group['clicked_sum']/all_data_group['clicked_count']

    # all_data_group.to_csv('D:/ad_simple_rate.csv', sep=',', index=False)
    # all_data_group = pd.read_csv('D:/ad_simple_rate.csv')

    test_data = pd.DataFrame()
    for test_df in pd.read_csv(sample_test_file, chunksize=chunk_size):
        minimize_df = test_df.groupby('display_id').agg(lambda x: set(x)).reset_index()
        test_data = pd.concat([test_data, minimize_df])
    #df_test['ad_score'] = df_test.apply(lambda row: get_rate_by_ad_id(all_data_group, row['ad_id']), axis=1)