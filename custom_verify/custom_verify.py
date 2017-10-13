import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import precision_score, recall_score, accuracy_score
import constant
import ast


def convert_result(df_prob_result):
    prev_display_id = None
    converted_result = []
    current_value = []
    for index, row in df_prob_result.iterrows():
        current_display_id = int(row['display_id'])
        current_prob = float(row['prob'])
        if prev_display_id is None:
            prev_display_id = current_display_id
            current_value.append(current_prob)
        elif prev_display_id == current_display_id:
            current_value.append(current_prob)
        else:
            max_prob = max(current_value)
            current_value = list(map(lambda x: 1 if x==max_prob else 0, current_value))
            converted_result = converted_result + current_value
            current_value = [current_prob]
            prev_display_id = current_display_id
    if len(current_value) > 0:
        max_prob = max(current_value)
        current_value = list(map(lambda x: 1 if x == max_prob else 0, current_value))
        converted_result = converted_result + current_value
    return converted_result


if __name__ == '__main__':
    sample_file = constant.get_sample_file()
    statistic_doc_feature_file = constant.get_document_statistic_feature_file()
    statistic_user_feature_file = constant.get_user_statistic_feature_file()
    statistic_ad_feature_file = constant.get_ad_statistic_feature_file()
    encoding_document_topic_file = constant.get_document_topic_encoding_feature_file()
    encoding_document_category_file = constant.get_document_category_encoding_feature_file()

    df = pd.read_csv(sample_file, header=0)
    df = df.drop(['uuid', 'geo_location'], axis=1)

    print('Load statistic document feature ...')
    df_doc_feature = pd.read_csv(statistic_doc_feature_file, header=None, converters={0: ast.literal_eval})
    print('Load statistic ad feature ...')
    df_ad_feature = pd.read_csv(statistic_ad_feature_file, header=None, converters={0: ast.literal_eval})
    # print('Load document topic feature ...')
    # df_document_topic = pd.read_csv(encoding_document_topic_file, header=None, converters={0: ast.literal_eval})
    # print('Load document category feature ...')
    # df_document_category = pd.read_csv(encoding_document_category_file, header=None, converters={0: ast.literal_eval})

    print('Convert list to separated columns ...')
    df_doc_feature = pd.DataFrame(df_doc_feature[0].values.tolist())
    df_ad_feature = pd.DataFrame(df_ad_feature[0].values.tolist())
    # df_document_topic = pd.DataFrame(df_document_topic[0].values.tolist())
    # df_document_category = pd.DataFrame(df_document_category[0].values.tolist())

    print('Merge to create trainable data ...')
    df = pd.concat([df, df_doc_feature, df_ad_feature], axis=1)

    X = df.drop(['clicked'], axis=1)
    Y = df['clicked']

    split_rate = 0.7
    total_size = df.shape[0]
    train_size = int(total_size * split_rate)
    df_train = df.iloc[:train_size, :]
    df_test = df.iloc[train_size:, :]

    X_train = df_train.drop(['clicked'], axis=1)
    X_test = df_test.drop(['clicked'], axis=1)
    Y_train = df_train['clicked']
    Y_test = df_test['clicked']

    #lr = LogisticRegression(n_jobs=-1, C=0.001, class_weight={0:0.2, 1:0.8}, solver='liblinear')
    #lr.fit(X_train, Y_train)
    #predict_proba = lr.predict_proba(X_test.drop(['display_id'], axis=1))
    #click_rate = list(map(lambda x: x[1], predict_proba))
    lr = LinearRegression(n_jobs=-1)
    lr.fit(X_train, Y_train)
    predict = lr.predict(X_test)
    click_rate = predict

    df_test_data = pd.concat([X_test, Y_test], axis=1)
    df_test_data = df_test_data.reset_index()
    df_click_rate = pd.DataFrame(click_rate)
    df_click_rate.columns = ['prob']
    df_test_data = pd.concat([df_test_data, df_click_rate], axis=1)
    df_test_data = df_test_data.sort_values('display_id')

    df_test_data = df_test_data[['display_id', 'ad_id', 'clicked', 'prob']]
    convert_result_lst = convert_result(df_test_data)

    print('Accuracy score:', accuracy_score(convert_result_lst, Y_test))
    print('Precision score:', precision_score(convert_result_lst, Y_test))
    print('Recall score:', recall_score(convert_result_lst, Y_test))


