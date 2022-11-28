import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-by-top-10-genres.csv")

# Group by metrics
df_genre_follow = df.groupby.rename(["genre_name"])["follow_count"].sum().reset_index()

df_genre_follow = df_genre_follow.rename(columns = {"follow_count": "total_follows" })

df_genre_hype = df.groupby(["genre_name"])["hype_count"].sum().reset_index()

df_genre_hype = df_genre_hype.rename(columns = {"hype_count": "total_hype" })

#Analyze data
BAR_WIDTH = 0.4

plt.bar(df_genre_follow.index - BAR_WIDTH / 2, df_genre_follow["total_follows"], color = "blue", label = "Number of follows", width = BAR_WIDTH )
plt.bar(df_genre_hype.index + BAR_WIDTH / 2, df_genre_hype["total_hype"], color = "red", label = "Number of Hypes", width = BAR_WIDTH)

plt.xticks(df.genre_follows.index, df_genre_follow["genre_name"])

plt.legend(loc = "upper left ")

plt.show()

