import psycopg 
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("data/hour.csv")

print(df.head(3))
print(df.shape)
df.info()
print(df.columns)
print(df.isna().sum())
print(df.dtypes)
df["dteday"] = pd.to_datetime(df["dteday"])
print(df["dteday"].dtype)

print(df.columns)

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="bike_project",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

cur.execute(
    "SELECT 1;"
)

cur.fetchall()

rows = df.itertuples(index = False, name = None)


cur.executemany(
    """
    INSERT INTO bicycle_rental (
    instant, 
    dteday,
    season,
    yr,
    mnth,
    hr,
    holiday,
    weekday,
    workingday,
    weathersit,
    temp,
    atemp,
    hum,
    windspeed,
    casual,
    registered,
    cnt
    )
    VALUES (
    %s,
    %s,
    %s,SELECT dteday, SUM(cnt)
FROM bicycle_rental
GROUP BY dteday
ORDER BY SUM(cnt) DESC
LIMIT 5;
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
    );
    """,
    rows
)

conn.commit()