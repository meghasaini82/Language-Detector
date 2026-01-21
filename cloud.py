import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

# -------------------------------
# 1. Load the hotel review dataset
# -------------------------------
df = pd.read_csv("hotel_reviews.csv")   # Make sure file is in the SAME folder

# -----------------------------------
# 2. Combine all reviews into one text
# -----------------------------------
text = " ".join(str(review) for review in df['Review'])

# -----------------------
# 3. Clean the text
# -----------------------
text = re.sub("[^a-zA-Z]", " ", text).lower()

# -----------------------
# 4. Tokenization
# -----------------------
tokens = nltk.word_tokenize(text)

# -----------------------
# 5. Remove stopwords
# -----------------------
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w not in stop_words]

# -----------------------
# 6. Lemmatization
# -----------------------
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]

# -----------------------
# 7. Join text again
# -----------------------
clean_text = " ".join(lemmatized_tokens)

# -----------------------
# 8. Generate word cloud
# -----------------------
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(clean_text)

# -----------------------
# 9. Display
# -----------------------
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
