import pandas as pd
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

# Download the stopwords if you haven't already
nltk.download('stopwords')

# Load your CSV file
df = pd.read_csv('C:\Users\vocat\Desktop\Prashant Final Project\Word Count\coffee_lat_lon.csv')

# Assuming your description column is named 'desc_1'
descriptions = df['desc_1'].astype(str)

# Combine all descriptions into one large text
all_text = " ".join(descriptions)

# Remove punctuation and convert to lowercase
all_text = re.sub(r'[^\w\s]', '', all_text).lower()

# Split the text into individual words
words = all_text.split()

# Filter out stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Count the frequency of each word
word_counts = Counter(filtered_words)

# Get the 50 most common words
top_50_words = word_counts.most_common(50)

# Convert the list of tuples to a DataFrame
df_top_words = pd.DataFrame(top_50_words, columns=['Word', 'Frequency'])

# Print the DataFrame
print(df_top_words)

# Optionally, save the DataFrame to a CSV file
df_top_words.to_csv('top_50_words_filtered.csv', index=False)