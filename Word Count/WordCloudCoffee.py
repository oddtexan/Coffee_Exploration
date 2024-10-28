#  Import the Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset
df = pd.read_csv('C:\\Users\\vocat\\Desktop\\Prashant Final Project\\Word Count\\coffee_lat_lon.csv')

# Fill NaN values with an empty string
df['desc_1'] = df['desc_1'].fillna('')

# Convert all entries in 'desc_1' to strings
df['desc_1'] = df['desc_1'].astype(str)

# Combine all the text in a specific column into one large string
text = " ".join(review for review in df['desc_1'])

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Remove axes
plt.show()

# Save the word cloud image (optional)
wordcloud.to_file("WordcloudIMAGE.png")