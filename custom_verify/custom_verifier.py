import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score


class CustomVerifier:
    def __init__(self, df_test, prob_result, label_field_name='clicked', group_field_name='display_id', result_field_name='prob'):
        self.__df__test__ = df_test.reset_index()
        self.__result__field__name__ = result_field_name

        self.__df__prob__result__ = pd.DataFrame(prob_result)
        self.__df__prob__result__.columns = [self.__result__field__name__]

        self.__df__test__ = pd.concat([self.__df__test__, self.__df__prob__result__], axis=1)

        self.__label__field__name__ = label_field_name
        self.__group__field__name__ = group_field_name
        self.__result__field__name__ = result_field_name

        self.__converted__result__ = None

    def get_df_test_with_prob_result(self):
        return self.__df__test__

    def get_Y_test(self):
        return self.__df__test__[self.__label__field__name__]

    def get_convert_result(self):
        if self.__converted__result__ is None:
            prev_display_id = None
            converted_result = []
            current_value = []
            for index, row in self.get_df_test_with_prob_result().iterrows():
                current_display_id = int(row[self.__group__field__name__])
                current_prob = float(row[self.__result__field__name__])
                if prev_display_id is None:
                    prev_display_id = current_display_id
                    current_value.append(current_prob)
                elif prev_display_id == current_display_id:
                    current_value.append(current_prob)
                else:
                    max_prob = max(current_value)
                    current_value = list(map(lambda x: 1 if x == max_prob else 0, current_value))
                    converted_result = converted_result + current_value
                    current_value = [current_prob]
                    prev_display_id = current_display_id
            if len(current_value) > 0:
                max_prob = max(current_value)
                current_value = list(map(lambda x: 1 if x == max_prob else 0, current_value))
                converted_result = converted_result + current_value
            self.__converted__result__ = converted_result
        return self.__converted__result__

    def verify(self):
        convert_result_lst = self.get_convert_result()
        Y_test = self.get_Y_test()
        print('Accuracy score:', accuracy_score(convert_result_lst, Y_test))
        print('Precision score:', precision_score(convert_result_lst, Y_test))
        print('Recall score:', recall_score(convert_result_lst, Y_test))