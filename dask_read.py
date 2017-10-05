import dask.dataframe as dd

PREFIX_DATA_FOLDER = 'D:/outbrain/'
TRAIN_FOLDER = 'clicks_train.csv/'
TEST_FOLDER = 'clicks_test.csv/'

test_file = PREFIX_DATA_FOLDER + TEST_FOLDER + 'clicks_test.csv'
sample_test_file = PREFIX_DATA_FOLDER + TEST_FOLDER + 'clicks_test_sample.csv'

chunk_size = 10**6

df_test = dd.read_csv(test_file)
df_test.head()


