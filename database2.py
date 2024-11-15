import psycopg

conn = psycopg.connect(host="localhost", dbname="datalol", user="postgres", password="@dmin1", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Players (
  puuid INT PRIMARY KEY,
  player_name VARCHAR(255),
  gameName VARCHAR(255),
  tagLine VARCHAR(255)
);
""")


conn.commit()

cur.close()
conn.close()