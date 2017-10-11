import constant
import pandas as pd


class DocumentMining:
    def __init__(self, df_merge_train, df_pageviews):
        self.df_pageviews = df_pageviews
        self.df_merge_train = df_merge_train
        self.total_pageviews = None
        self.total_click = None

    def get_total_click(self):
        if self.total_click is None:
            self.total_click = self.df_merge_train[constant.CLICKED_COLUMN_NAME].sum()
        return self.total_click

    def get_total_pageviews(self):
        if self.total_pageviews is None:
            self.total_pageviews = df_page_view.shape[0]
        return self.total_pageviews

    # Support
    def __get__click__number(self, __id, __field__name):
        return self.df_merge_train[(self.df_merge_train[__field__name] == __id) & (self.df_merge_train[constant.CLICKED_COLUMN_NAME] == 1)].shape[0]

    def __get__appear__number(self, __id, __field__name):
        return self.df_pageviews[self.df_pageviews[__field__name] == __id].shape[0]

    def __get__feature(self, __id, __field__name):
        number_of_click = self.__get__click__number(__id, __field__name)
        number_of_appear = self.__get__appear__number(__id, __field__name)
        print(number_of_click, number_of_appear)
        click_rate_over_all_click = number_of_click / self.get_total_click()
        click_rate = 0
        if number_of_appear is not 0:
            click_rate = number_of_click / number_of_appear
        elif number_of_click is not 0:
            click_rate = click_rate_over_all_click * constant.DEFAULT_CLICK_RATE_OVER_APPEAR_RATE
        else:
            click_rate = 0
        appear_rate = number_of_appear / self.get_total_pageviews()
        return [click_rate_over_all_click, click_rate, appear_rate]

    def get_doc_id_feature(self, doc_id):
        return self.__get__feature(doc_id, constant.DOCUMENT_ID_COLUMN_NAME)

    def get_source_id_feature(self, source_id):
        return self.__get__feature(source_id, constant.DOCUMENT_SOURCE_ID_COLUMN_NAME)

    def get_publisher_id_feature(self, publisher_id):
        return self.__get__feature(publisher_id, constant.DOCUMENT_PUBLISHER_ID_COLUMN_NAME)


if __name__ == '__main__':
    df_merge_train = pd.read_csv('D:/outbrain/sample_data.csv', header=0)
    df_page_view = pd.read_csv(constant.get_page_view_sample_file(), header=0)
    docMining = DocumentMining(df_merge_train, df_page_view)
    doc_id = 778157
    print(docMining.get_doc_id_feature(doc_id))