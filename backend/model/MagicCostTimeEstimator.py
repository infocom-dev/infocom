import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler


class MagicCostTimeEstimator:
    def __init__(self, dataset_path="dataset.csv"):
        self.price_model = KNeighborsRegressor(algorithm='ball_tree', leaf_size=41, n_neighbors=3)
        self.time_model = KNeighborsRegressor(algorithm='kd_tree', leaf_size=6, metric='euclidean', n_neighbors=4)
        self.ss = StandardScaler()
        self.data = pd.read_csv(dataset_path)

        self.one_label_features = ["stack", "type", "purpose", "design", "adaptability", "product_delivery"]
        self.multi_label_features = ["languages"]
        self.range_features = ["budget"]
        self.need_to_be_scaled_features = (["predicted_count_users"]
                                           + self.get_new_range_features(self.range_features))
        self.drop_features = ["Unnamed: 17", "id", "development_time", "final_price"]

        self.development_time = self.data["development_time"]
        self.final_price = self.data["final_price"]
        self.data = self.cook_data(self.data, train=True)
        self.fit(self.data)

    def cook_data(self, data, train=False):
        try:
            data = data.drop(columns=self.drop_features)
        except KeyError as e:
            print(e)

        data.replace("no", False, inplace=True)
        data.replace("yes", True, inplace=True)

        data = self.encode_one_label(data)
        data = self.encode_multi_label(data)
        data = self.transform_ranges(data)
        if train:
            data = self.scale_train_data(data)
        else:
            data = self.add_up_test_data(data)
            data = self.scale_test_data(data)
        return data

    def fit(self, data):
        self.price_model.fit(data, self.final_price)
        self.time_model.fit(np.array(self.final_price).reshape(-1, 1), self.development_time)

    def predict(self, x):
        price = self.price_model.predict(x)
        return price[0], self.time_model.predict(np.array(price).reshape(-1, 1))[0]

    def encode_one_label(self, data):
        dummies = pd.get_dummies(data[self.one_label_features])
        data = pd.concat([data, dummies], axis=1)
        return data.drop(self.one_label_features, axis=1)

    def encode_multi_label(self, data):
        for feature in self.multi_label_features:
            types_list = data[feature].apply(lambda x: list(map(lambda i: i.strip(), x.split(","))))

            mlb = MultiLabelBinarizer()
            types_encoded = pd.DataFrame(mlb.fit_transform(types_list), columns=f"{feature}_" + mlb.classes_)
            data = pd.concat([data, types_encoded], axis=1)
            return data.drop(columns=feature)

    def transform_ranges(self, data):
        for feature in self.range_features:
            data[self.get_new_range_features([feature])] = data[feature]. \
                str.split('-', 1, expand=True)
            return data.drop(feature, axis=1)

    @staticmethod
    def get_new_range_features(features: list[str]) -> list[str]:
        features_list = []
        for feature in features:
            features_list += [f'start_{feature}', f'end_{feature}']
        return features_list

    def scale_test_data(self, data):
        data.loc[:, self.need_to_be_scaled_features] = self.ss.transform(
            data.loc[:, self.need_to_be_scaled_features])
        return data

    def scale_train_data(self, data):
        data.loc[:, self.need_to_be_scaled_features] = self.ss.fit_transform(
            data.loc[:, self.need_to_be_scaled_features])
        return data

    def add_up_test_data(self, data: pd.DataFrame):
        columns = [c for c in self.data.columns if c not in data.columns]
        return pd.concat([data, pd.DataFrame(0, index=np.arange(len(data)), columns=columns)], axis=1)


if __name__ == "__main__":
    from time import time
    mcte = MagicCostTimeEstimator()
    df = pd.DataFrame([["site", "web_application", "Tilda", "1000", "yes", "yes", "1000-5000", "individual", "adaptive", "Saas",
                        "yes", "no", "yes", "fr"]],
                      columns=["type", "purpose", "stack", "predicted_count_users", "payment_system", "geolocation",
                               "budget", "design", "adaptability", "product_delivery", "integration_systems",
                               "integration_systems_API", "required_DB", "languages"])
    st = time()
    df = mcte.cook_data(df)
    print(mcte.predict(df))
    print(time() - st, "sec")
