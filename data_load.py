# ### Use psycopg2 & pandas to load csv files to postgresql
# * database name = voice_recognition
# * schema = public
# * table name = cv_tbl

### import dependencies
from sqlalchemy import create_engine
from config import username, password
import pandas as pd
import psycopg2
import os

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS
con_str = psycopg2.connect(f"user={username} password={password}")
con_str.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = con_str.cursor()

# drop and create database
cursor.execute('DROP DATABASE IF EXISTS voice_recognition')
cursor.execute('CREATE DATABASE voice_recognition')

# connect to the database
connection = psycopg2.connect(
    f"dbname=voice_recognition user={username} host=localhost                             password={password}")

cursor1 = connection.cursor()

# Create a table if it does exist
cursor1.execute(
    "CREATE TABLE IF NOT EXISTS cv_tbl (csv_name VARCHAR(20), category VARCHAR(5),                npy_name VARCHAR(35), gender VARCHAR(6));")

cursor1.execute("TRUNCATE cv_tbl;")

connection.commit()

# Retrieve csv file names into a list
all_files = os.listdir("./")
csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))

csv_files

# Upload the csv data into table
for csvName in csv_files:
    array = csvName.split("-")
#     print(array)

    if array[1] != "invalid.csv":
        if array[2] == "dev.csv":
            category = "dev"
#             print(category)
        elif array[2] == "test.csv":
            category = "test"
#             print(category)
        elif array[2] == "train.csv":
            category = "train"
#             print(category)

        csv_df = pd.read_csv(csvName, index_col=False)

        for row in csv_df.iterrows():
            sqlInsertRow = "INSERT INTO cv_tbl values('" + csvName + "', '" + \
                category + "', '" + row[1][0] + "', '" + row[1][1] + "');"
            # print(sqlInsertRow)

            cursor1.execute(sqlInsertRow)

        connection.commit()

    print("Done!")

cv_count_df = pd.read_sql('select count(*) from cv_tbl', connection)
cv_count_df


# ### Use sqlalchemy & pandas to load csv files to postgresql
# * database name = voice_recognition
# * schema = public
# * table name = npy_tbl

### import dependencies


# postgresql info
url = f'postgresql://{username}:{password}@localhost:5432/voice_recognition'

# Create an engine object.
engine = create_engine(url, echo=True)

# Retrieve csv file names into a list
all_files = os.listdir("./cv-valid-test")
npy_files = list(filter(lambda f: f.endswith('.npy'), all_files))

print(npy_files)

npy_df = pd.DataFrame(npy_files, columns=["npy_name"])
npy_df.to_sql('npy_tbl', con=engine, if_exists='replace', index=False)

npy_tbl_count = pd.read_sql('select count(*) from npy_tbl', con=engine)
print(npy_tbl_count)


# In[ ]:
