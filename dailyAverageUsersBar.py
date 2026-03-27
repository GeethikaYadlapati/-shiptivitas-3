import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("shiptivity.db")

# Query for average DAU before and after
query = """
SELECT 'Before' AS period, AVG(NumUsers) AS avg_dau FROM (
    SELECT date(login_timestamp, 'unixepoch') AS Day,
           COUNT(DISTINCT user_id) AS NumUsers 
    FROM login_history 
    WHERE login_timestamp < strftime('%s', '2018-06-02') 
    GROUP BY Day
)
UNION ALL
SELECT 'After' AS period, AVG(NumUsers) AS avg_dau FROM (
    SELECT date(login_timestamp, 'unixepoch') AS Day,
           COUNT(DISTINCT user_id) AS NumUsers 
    FROM login_history 
    WHERE login_timestamp >= strftime('%s', '2018-06-02') 
    GROUP BY Day
);
"""

# Load into dataframe
df = pd.read_sql_query(query, conn)

# Create bar graph
plt.figure()
plt.bar(df["period"], df["avg_dau"])

# Labels
plt.xlabel("Period")
plt.ylabel("Average Daily Users")
plt.title("Average Daily Active Users: Before vs After Feature")

# Show graph
plt.show()