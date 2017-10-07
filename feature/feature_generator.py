from feature.ad_feature import AdFeatureGenerator
from feature.document_feature import DocumentFeatureGenerator
from feature.user_feature import UserFeatureGenerator
from feature.util import feature_flatten
import time


class FeatureGenerator:
    def __init__(self, df_events, df_document_topic):
        self.df_events = df_events
        self.doc_feature_generator = DocumentFeatureGenerator(df_document_topic)
        self.ad_feature_generator = AdFeatureGenerator()
        self.user_feature_generator = UserFeatureGenerator()
        pass

    def get_feature(self, display_id, ad_id):
        start_time = time.time()
        display_id_row_info = self.df_events.loc[self.df_events['display_id'] == display_id]
        user_feature = None
        document_feature = None
        ad_feature = None
        if len(display_id_row_info) > 0:
            uuid = display_id_row_info['uuid'].values[0]
            document_id = display_id_row_info['document_id'].values[0]
            document_feature = self.doc_feature_generator.get_feature(document_id)
            user_feature = self.user_feature_generator.get_feature(uuid)
            ad_feature = self.ad_feature_generator.get_feature(ad_id)
            feature = feature_flatten([document_feature, ad_feature])
            # print('- Create feature for {0}, {1} done, {2}'.format(display_id, ad_id, (time.time()-start_time)))
            return feature
        else:
            # print('- Not found feature for {0}, {1} done, {2}'.format(display_id, ad_id, (time.time()-start_time)))
            return None
