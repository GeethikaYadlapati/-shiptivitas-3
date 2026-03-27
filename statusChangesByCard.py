import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect to database
conn = sqlite3.connect("shiptivity.db")

# query
query = """
SELECT name, COUNT(card_change_history.id) AS changes
FROM card_change_history 
JOIN card ON card_change_history.cardID = card.id 
WHERE oldStatus IS NOT NULL 
GROUP BY cardID;
"""

# load data
df = pd.read_sql_query(query, conn)

# create bar chart
plt.figure()
plt.bar(df["name"], df["changes"])

# labels
plt.xlabel("Card Name")
plt.ylabel("Number of Status Changes")
plt.title("Status Changes by Card")

# rotate labels so they fit
plt.xticks([])

# layout fix
plt.tight_layout()

# show chart
plt.show()