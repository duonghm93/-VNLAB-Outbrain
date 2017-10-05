import time
import pandas as pd
from os import listdir

input_folder = 'D:/outbrain/clicks_test.csv/'
input_file = 'D:/outbrain/clicks_test.csv/testaa'
output_file = 'D:/test_output.csv'
TEST_FILE_PREFIX = 'test'


def get_rate_by_ad_id(df, ad_id):
    result = df.loc[df['ad_id'] == ad_id]['clicked_rate'].values
    if len(result) > 0:
        return result[0]
    else:
        return 0


def get_list_of_file(root_folder):
    list_file = listdir(root_folder)
    list_file = list(filter(lambda x: x.startswith(TEST_FILE_PREFIX), list_file))
    list_file_full = list(map(lambda x: root_folder + x, list_file))
    return list_file_full


start_time = time.time()
in_stream = open(input_file, "r")
out_stream = open(output_file, 'w')
ad_rate_df = pd.read_csv('D:/ad_simple_rate.csv')
for line in in_stream:
    recom_raw = line.split(sep=',')
    display_id = int(recom_raw[0])
    ad_id = int(recom_raw[1])
    ad_rate = get_rate_by_ad_id(ad_rate_df, ad_id)
    out_stream.write('{0},{1},{2}\n'.format(display_id,ad_id,ad_rate))
in_stream.close()
out_stream.close()
print("end time: ", (time.time()-start_time))