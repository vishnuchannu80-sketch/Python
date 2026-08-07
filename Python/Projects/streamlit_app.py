import streamlit as st
from api_client import APIClient
from transformer import DataTransformer
from mysql_handler import MySQLHandler
import configparser
import pandas as pd

# Read DB config
config = configparser.ConfigParser()
config.read("config.ini")
db_config = dict(config["mysql"])

# Initialize
db = MySQLHandler(db_config)
api = APIClient()
transformer = DataTransformer()

st.set_page_config(page_title="Healthcare Data Dashboard", layout="centered")
st.title(" Global Healthcare Data ETL & Analysis")

# Sidebar navigation
option = st.sidebar.radio("Select Operation", (
    "Create Tables",
    "List Tables",
    "Fetch Data",
    "Query: Avg New Cases",
    "Query: Summary"
))

if option == "Create Tables":
    if st.button(" Create Tables"):
        db.create_tables()
        st.success(" Tables created successfully.")

elif option == "List Tables":
    tables = db.list_tables()
    st.write(" Tables in Database:")
    st.table(tables)

elif option == "Fetch Data":
    country_code = st.text_input("Country Code", "IND")
    start = st.date_input("Start Date")
    end = st.date_input("End Date")

    if st.button(" Fetch and Insert Data"):
        raw = api.fetch_data(country_code, str(start), str(end))
        if raw:
            for r in raw:
                r["location"] = "India" if country_code == "IND" else country_code
            df = transformer.clean_and_transform(raw)
            db.insert_data("daily_cases", df.to_dict(orient="records"))
            st.success(f" Inserted {len(df)} records.")
        else:
            st.warning(" No data found.")

elif option == "Query: Avg New Cases":
    country = st.text_input("Country", "India")
    if st.button(" Get Average New Cases"):
        result = db.query_avg_new_cases(country)
        st.metric(" Avg New Cases/Day", f"{result[0]:.2f}" if result else "0.00")

elif option == "Query: Summary":
    country = st.text_input("Country", "India")
    if st.button(" Get Summary"):
        result = db.query_summary(country)
        if result:
            st.table(pd.DataFrame({
                "Metric": [
                    "Total new cases",
                    "Total deaths",
                    "Avg new cases/day",
                    "Avg new deaths/day"
                ],
                "Value": [
                    result[0],
                    result[1],
                    f"{result[2]:.2f}",
                    f"{result[3]:.2f}"
                ]
            }))
        else:
            st.info("No data found.")

# Close connection
db.close()
