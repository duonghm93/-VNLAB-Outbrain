import pandas as pd
import constant
import ast
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC, SVR
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, mean_squared_log_error, median_absolute_error, r2_score

if __name__ == '__main__':
    sample_data_file = constant.get_sample_file()
    statistic_doc_feature_file = constant.get_document_statistic_feature_file()
    statistic_user_feature_file = constant.get_user_statistic_feature_file()
    statistic_ad_feature_file = constant.get_ad_statistic_feature_file()

    print('Load sample data file')
    df = pd.read_csv(sample_data_file, header=0)
    df = df.drop(['uuid', 'geo_location'], axis=1)
    # df = df.drop(['display_id', 'document_id', 'ad_id'], axis=1)
    df = df.drop(['time_stamp'], axis=1)
    # df = df.drop(['source_id', 'publisher_id', 'campaign_id', 'advertiser_id'], axis=1)
    # df = df['clicked']

    print('Load statistic document feature ...')
    df_doc_feature = pd.read_csv(statistic_doc_feature_file, header=None, converters={0:ast.literal_eval})
    # print('Load statistic user feature ...')
    # df_user_feature = pd.read_csv(statistic_user_feature_file, header=None, converters={0:ast.literal_eval})
    print('Load statistic ad feature ...')
    df_ad_feature = pd.read_csv(statistic_ad_feature_file, header=None, converters={0: ast.literal_eval})

    print('Convert list to separated columns ...')
    df_doc_feature = pd.DataFrame(df_doc_feature[0].values.tolist())
    # df_user_feature = pd.DataFrame(df_user_feature[0].values.tolist())
    df_ad_feature = pd.DataFrame(df_ad_feature[0].values.tolist())

    print('Merge to create trainable data ...')
    # df = pd.concat([df, df_doc_feature, df_user_feature, df_ad_feature], axis=1)
    df = pd.concat([df, df_doc_feature, df_ad_feature], axis=1)

    X = df.drop(['clicked'], axis=1)
    Y = df['clicked']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

    print(X.columns)
    print(X.head())

    print('Create model ...')
    # lr = SVC()
    lr = SVR()
    lr.fit(X_train, Y_train)
    print('Start predicting ...')
    predict = lr.predict(X_test)
    print(list(predict))
    # print('Accuracy score:', accuracy_score(predict, Y_test))
    # print('Precision score:', precision_score(predict, Y_test))
    # print('Recall score:', recall_score(predict, Y_test))
    print('explained_variance_score:', explained_variance_score(predict, Y_test))
    print('mean_absolute_error:', mean_absolute_error(predict, Y_test))
    print('mean_squared_error:', mean_squared_error(predict, Y_test))
    print('mean_squared_log_error:', mean_squared_log_error(predict, Y_test))
    print('median_absolute_error:', median_absolute_error(predict, Y_test))
    print('r2_score:', r2_score(predict, Y_test))


