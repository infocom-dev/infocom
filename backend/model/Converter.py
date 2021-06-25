from typing import List

import pandas as pd


def convert(customer_answers):
    columns = ["type", "purpose", "stack", "predicted_count_users", "payment_system", "geolocation",
               "budget", "design", "adaptability", "product_delivery", "integration_systems",
               "integration_systems_API", "required_DB", "languages"]
    res = {}
    for customer_answer in customer_answers:
        if customer_answer["question"] in columns:
            if customer_answer["text"]:
                res[customer_answer["question"]] = customer_answer["text"]
            elif customer_answer["date"]:
                res[customer_answer["question"]] = customer_answer["date"]
            elif customer_answer["custom_answer"]:
                res[customer_answer["question"]] = ",".join([x["value"] for x in customer_answer["custom_answer"]])
    assert len(columns) == len(res.keys()), "Нехватает вопросов!"
    return pd.DataFrame([res.values()], columns=res.keys())


