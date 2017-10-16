import constant
import pandas as pd

class StatisticalFeatureLargeFileGenerator:
    def __init__(self, merge_file_name, page_view_file_name, merge_data_chunk_size=10000, page_view_chunk_size=10000, merge_file_nrows=None, page_view_nrows=None):
        self.__merge__data__file__name__ = merge_file_name
        self.__page__view__file__name__ = page_view_file_name
        self.__merge__file__nrows__ = merge_file_nrows
        self.__page__view__nrows__ = page_view_nrows
        self.__merge__data__chunk__size__ = merge_data_chunk_size
        self.__page__view__chunk__size__ = page_view_chunk_size
        self.__total__pageviews__ = None
        self.__total__clicks__ = None

        self.__cache__click__ = {}
        self.__cache__appear__ = {}
        self.__cache__feature__ = {}

    def get_total_click(self):
        if self.__total__clicks__ is None:
            self.__total__clicks__ = 0
            for df in pd.read_csv(self.__merge__data__file__name__, header=0, chunksize=self.__merge__data__chunk__size__, nrows=self.__merge__file__nrows__):
                self.__total__clicks__ = self.__total__clicks__ + df[constant.CLICKED_COLUMN_NAME].sum()
        return self.__total__clicks__

    def get_total_pageviews(self):
        if self.__total__pageviews__ is None:
            self.__total__pageviews__ = 0
            for df in pd.read_csv(self.__merge__data__file__name__, header=0, chunksize=self.__page__view__chunk__size__, nrows=self.__page__view__nrows__):
                self.__total__pageviews__ = self.__total__pageviews__ + df.shape[0]
        return self.__total__pageviews__

    # Support
    def __get__click__number__(self, __id__, __field__name__):
        if __field__name__ not in self.__cache__click__:
            self.__cache__click__[__field__name__] = {}

        if __id__ not in self.__cache__click__[__field__name__]:
            click_number = 0
            for df in pd.read_csv(self.__merge__data__file__name__, header=0, chunksize=self.__merge__data__chunk__size__, nrows=self.__merge__file__nrows__):
                click_number += df[(df[__field__name__] == __id__) & (df[constant.CLICKED_COLUMN_NAME]==1)].shape[0]
            self.__cache__click__[__field__name__][__id__] = click_number

        return self.__cache__click__[__field__name__][__id__]

    def __get__appear__number__(self, __id__, __field__name__):
        if __field__name__ not in self.__cache__appear__:
            self.__cache__appear__[__field__name__] = {}

        if __id__ not in self.__cache__appear__[__field__name__]:
            appear_number = 0
            for df in pd.read_csv(self.__page__view__file__name__, header=0, chunksize=self.__page__view__chunk__size__, nrows=self.__page__view__nrows__):
                appear_number += df[df[__field__name__] == __id__].shape[0]
            self.__cache__appear__[__field__name__][__id__] = appear_number

        return self.__cache__appear__[__field__name__][__id__]

    def __get__feature__(self, __id__, __field__name__, check_in_page_view = False):
        if __field__name__ not in self.__cache__feature__:
            self.__cache__feature__[__field__name__] = {}

        if __id__ not in self.__cache__feature__[__field__name__]:
            feature = []
            number_of_click = self.__get__click__number__(__id__, __field__name__)
            click_rate_over_all_click = number_of_click / self.get_total_click()
            feature.append(click_rate_over_all_click)

            if check_in_page_view:
                number_of_appear = self.__get__appear__number__(__id__, __field__name__)
                click_rate = 0
                if number_of_appear is not 0:
                    click_rate = number_of_click / number_of_appear
                elif number_of_click is not 0:
                    click_rate = click_rate_over_all_click * constant.DEFAULT_CLICK_RATE_OVER_APPEAR_RATE
                feature.append(click_rate)
                appear_rate = number_of_appear / self.get_total_pageviews()
                feature.append(appear_rate)

            self.__cache__feature__[__field__name__][__id__] = feature

        return self.__cache__feature__[__field__name__][__id__]

    def get_doc_id_feature(self, doc_id):
        return self.__get__feature__(doc_id, constant.DOCUMENT_ID_COLUMN_NAME, check_in_page_view=True)

    def get_doc_source_id_feature(self, source_id):
        return self.__get__feature__(source_id, constant.DOCUMENT_SOURCE_ID_COLUMN_NAME, check_in_page_view=True)

    def get_doc_publisher_id_feature(self, publisher_id):
        return self.__get__feature__(publisher_id, constant.DOCUMENT_PUBLISHER_ID_COLUMN_NAME, check_in_page_view=True)

    def get_user_id_feature(self, user_id):
        return self.__get__feature__(user_id, constant.USER_ID_COLUMN_NAME, check_in_page_view=True)

    def get_ad_id_feature(self, ad_id):
        return self.__get__feature__(ad_id, constant.AD_ID_COLUMN_NAME)

    def get_ad_campaign_id_feature(self, campaign_id):
        return self.__get__feature__(campaign_id, constant.AD_CAMPAIGN_ID_COLUMN_NAME)

    def get_ad_advertiser_id_feature(self, advertiser_id):
        return self.__get__feature__(advertiser_id, constant.AD_ADVERTISER_ID_COLUMN_NAME)

    def get_doc_feature_from_doc_id(self, doc_id):
        for df in pd.read_csv(self.__merge__data__file__name__, header=0, chunksize=self.__merge__data__chunk__size__, nrows=self.__merge__file__nrows__):
            rows = df[df[constant.DOCUMENT_ID_COLUMN_NAME] == doc_id]
            if len(rows) > 0:
                row = rows.head(1)
                source_id = row[constant.DOCUMENT_SOURCE_ID_COLUMN_NAME].values[0]
                publisher_id = row[constant.DOCUMENT_PUBLISHER_ID_COLUMN_NAME].values[0]
                return self.get_doc_id_feature(doc_id) + self.get_doc_source_id_feature(source_id) + self.get_doc_publisher_id_feature(publisher_id)
            else:
                continue
        # Data error
        return None

    def get_user_feature_from_user_id(self, user_id):
        return self.get_user_id_feature(user_id)

    def get_ad_feature_from_ad_id(self, ad_id):
        for df in pd.read_csv(self.__merge__data__file__name__, header=0, chunksize=self.__merge__data__chunk__size__, nrows=self.__merge__file__nrows__):
            rows = df[df[constant.AD_ID_COLUMN_NAME] == ad_id]
            if len(rows) > 0:
                row = rows.head(1)
                campaign_id = row[constant.AD_CAMPAIGN_ID_COLUMN_NAME].values[0]
                advertiser_id = row[constant.AD_ADVERTISER_ID_COLUMN_NAME].values[0]
                return self.get_ad_id_feature(ad_id) + self.get_ad_campaign_id_feature(campaign_id) + self.get_ad_advertiser_id_feature(advertiser_id)
            else:
                continue
        # Data error
        return None

if __name__ == '__main__':
    merge_data_file = constant.get_train_merge_file()
    page_view_file = constant.get_pageviews_mege_file()
    feature_gen = StatisticalFeatureLargeFileGenerator(
        merge_file_name = merge_data_file,
        page_view_file_name = page_view_file,
        merge_file_nrows=None,
        page_view_nrows=None
    )
    doc_id = 778157
    user_id = '79a85fa78311b9'
    ad_id = 125211

    print(feature_gen.get_doc_feature_from_doc_id(doc_id))
    print(feature_gen.get_user_id_feature(user_id))
    print(feature_gen.get_ad_feature_from_ad_id(ad_id))