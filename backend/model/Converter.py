import pandas as pd
import datetime


def convert(customer_answers):
    columns = ["type", "purpose", "stack", "predicted_count_users", "payment_system", "geolocation",
               "budget", "design", "adaptability", "product_delivery", "integration_systems",
               "integration_systems_API", "required_DB", "languages"]
    res = {}
    for customer_answer in customer_answers:
        if customer_answer["question"] in columns:
            if customer_answer.get("text"):
                res[customer_answer["question"]] = customer_answer["text"]
            elif customer_answer.get("date"):
                res[customer_answer["question"]] = customer_answer["date"]
            elif customer_answer.get("custom_answer"):
                res[customer_answer["question"]] = ",".join([x["value"] for x in customer_answer["custom_answer"]])
    assert len(columns) == len(res.keys()), "Нехватает вопросов!"
    return pd.DataFrame([res.values()], columns=res.keys())


def convert_hours_to_date(hours):
    return (datetime.datetime.now() + datetime.timedelta(hours=hours*3)).strftime('%Y-%m-%d')
