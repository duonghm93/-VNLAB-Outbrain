import constant
import pandas as pd


class StatisticalFeatureGenerator:
    def __init__(self, df_merge_train, df_page_views):
        self.df_page_views = df_page_views
        self.df_merge_train = df_merge_train
        self.total_pageviews = None
        self.total_click = None

    def get_total_click(self):
        if self.total_click is None:
            self.total_click = self.df_merge_train[constant.CLICKED_COLUMN_NAME].sum()
        return self.total_click

    def get_total_pageviews(self):
        if self.total_pageviews is None:
            self.total_pageviews = self.df_page_views.shape[0]
        return self.total_pageviews

    # Support
    def __get__click__number(self, __id, __field__name):
        return self.df_merge_train[(self.df_merge_train[__field__name] == __id) & (self.df_merge_train[constant.CLICKED_COLUMN_NAME] == 1)].shape[0]

    def __get__appear__number(self, __id, __field__name):
        return self.df_page_views[self.df_page_views[__field__name] == __id].shape[0]

    def __get__feature(self, __id, __field__name, check_in_page_view = False):
        feature = []
        number_of_click = self.__get__click__number(__id, __field__name)
        click_rate_over_all_click = number_of_click / self.get_total_click()
        feature.append(click_rate_over_all_click)

        if check_in_page_view:
            number_of_appear = self.__get__appear__number(__id, __field__name)
            click_rate = 0
            if number_of_appear is not 0:
                click_rate = number_of_click / number_of_appear
            elif number_of_click is not 0:
                click_rate = click_rate_over_all_click * constant.DEFAULT_CLICK_RATE_OVER_APPEAR_RATE
            feature.append(click_rate)
            appear_rate = number_of_appear / self.get_total_pageviews()
            feature.append(appear_rate)

        return feature

    def get_doc_id_feature(self, doc_id):
        return self.__get__feature(doc_id, constant.DOCUMENT_ID_COLUMN_NAME, check_in_page_view=True)

    def get_doc_source_id_feature(self, source_id):
        # TODO when page_view data merge with document_meta_data, it is able turn check_in_page_view on
        return self.__get__feature(source_id, constant.DOCUMENT_SOURCE_ID_COLUMN_NAME, check_in_page_view=True)

    def get_doc_publisher_id_feature(self, publisher_id):
        # TODO when page_view data merge with document_meta_data, it is able turn check_in_page_view on
        return self.__get__feature(publisher_id, constant.DOCUMENT_PUBLISHER_ID_COLUMN_NAME, check_in_page_view=True)

    def get_user_id_feature(self, user_id):
        return self.__get__feature(user_id, constant.USER_ID_COLUMN_NAME, check_in_page_view=True)

    def get_ad_id_feature(self, ad_id):
        return self.__get__feature(ad_id, constant.AD_ID_COLUMN_NAME)

    def get_ad_campaign_id_feature(self, campaign_id):
        return self.__get__feature(campaign_id, constant.AD_CAMPAIGN_ID_COLUMN_NAME)

    def get_ad_advertiser_id_feature(self, advertiser_id):
        return self.__get__feature(advertiser_id, constant.AD_ADVERTISER_ID_COLUMN_NAME)

    def get_doc_feature_from_doc_id(self, doc_id):
        row = self.df_merge_train[self.df_merge_train[constant.DOCUMENT_ID_COLUMN_NAME] == doc_id].head(1)
        source_id = row[constant.DOCUMENT_SOURCE_ID_COLUMN_NAME].values[0]
        publisher_id = row[constant.DOCUMENT_PUBLISHER_ID_COLUMN_NAME].values[0]
        return self.get_doc_id_feature(doc_id) + self.get_doc_source_id_feature(source_id) + self.get_doc_publisher_id_feature(publisher_id)

    def get_user_feature_from_user_id(self, user_id):
        return self.get_user_id_feature(user_id)

    def get_ad_feature_from_ad_id(self, ad_id):
        row = self.df_merge_train[self.df_merge_train[constant.AD_ID_COLUMN_NAME] == ad_id].head(1)
        campaign_id = row[constant.AD_CAMPAIGN_ID_COLUMN_NAME].values[0]
        advertiser_id = row[constant.AD_ADVERTISER_ID_COLUMN_NAME].values[0]
        return self.get_ad_id_feature(ad_id) + self.get_ad_campaign_id_feature(campaign_id) + self.get_ad_advertiser_id_feature(advertiser_id)


if __name__ == '__main__':
    df_merge_train = pd.read_csv('D:/outbrain/sample_data.csv', header=0)
    df_page_view = pd.read_csv('D:/outbrain/page_view_sample_merge_data.csv', header=0)
    docMining = StatisticalFeatureGenerator(df_merge_train, df_page_view)
    doc_id = 778157
    user_id = '79a85fa78311b9'
    ad_id = 125211

    print(docMining.get_doc_feature_from_doc_id(doc_id))
    print(docMining.get_user_id_feature(user_id))
    print(docMining.get_ad_feature_from_ad_id(ad_id))