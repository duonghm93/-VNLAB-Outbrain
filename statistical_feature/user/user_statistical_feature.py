import constant


class UserStatisticalGenerator:
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