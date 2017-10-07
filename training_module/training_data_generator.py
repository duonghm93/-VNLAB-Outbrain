from feature.feature_generator import FeatureGenerator
import pandas as pd
from constant import *


class TrainingDataGenerator:
    def __init__(self, df_raw_train_data, feature_generator):
        self.df_raw_train_data = df_raw_train_data
        self.feature_generator = feature_generator

    def generate_training_data(self):
        train_data = []
        for index, row in self.df_raw_train_data.iterrows():
            display_id = row[DISPLAY_ID_COLUMN_NAME]
            ad_id = row[AD_ID_COLUMN_NAME]
            clicked = row[CLICKED_COLUMN_NAME]
            feature = self.feature_generator.get_feature(display_id, ad_id)
            if feature is not None:
                train_data.append([feature, [clicked]])
        df_new_train_data = pd.DataFrame(train_data)
        df_new_train_data.columns = [DEFAULT_FEATURE_COLUMN_NAME, DEFAULT_LABEL_COLUMN_NAME]
        return df_new_train_data
