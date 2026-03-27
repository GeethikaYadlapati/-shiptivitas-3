import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to DB
conn = sqlite3.connect("shiptivity.db")

# Query 1 (BEFORE)
query_before = """
SELECT date(login_timestamp, 'unixepoch') AS day,
       COUNT(DISTINCT user_id) AS dau
FROM login_history
WHERE login_timestamp < strftime('%s', '2018-06-02')
GROUP BY day
ORDER BY day;
"""

# Query 3 (AFTER)
query_after = """
SELECT date(login_timestamp, 'unixepoch') AS day,
       COUNT(DISTINCT user_id) AS dau
FROM login_history
WHERE login_timestamp >= strftime('%s', '2018-06-02')
GROUP BY day
ORDER BY day;
"""

df_before = pd.read_sql_query(query_before, conn)
df_after = pd.read_sql_query(query_after, conn)

# Plot both lines
plt.figure()

plt.plot(df_before["day"], df_before["dau"], marker='o', label='Before')
plt.plot(df_after["day"], df_after["dau"], marker='o', label='After')

# Feature line
plt.axvline(x='2018-06-02', linestyle='--', label='Feature Launch')

# Labels
plt.xlabel("Date")
plt.ylabel("Daily Active Users")
plt.title("DAU Before vs After Feature")

plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.xticks([])
plt.show()