import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Load the Airbnb dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

#Get top N neighborhoods
def get_top_neighborhoods(df, n):
    neighborhoods = df.groupby('neighbourhood').mean()
    neighborhoods = neighborhoods.sort_values('price', ascending=False).head(n)
    neighborhoods = neighborhoods[['price']]
    neighborhoods = neighborhoods.round(2)
    neighborhoods['price'] = neighborhoods['price'].apply(lambda x: '${:,.2f}'.format(x))
    neighborhoods.index.name = 'Most Expensive Neighborhoods'
    neighborhoods.columns = ['Average Price per Night']
    return neighborhoods

#Get bottom N neighborhoods
def get_low_neighborhoods(df, n):
    neighborhoods = df.groupby('neighbourhood').mean()
    neighborhoods = neighborhoods.sort_values('price').head(n)
    neighborhoods = neighborhoods[['price']]
    neighborhoods = neighborhoods.round(2)
    neighborhoods['price'] = neighborhoods['price'].apply(lambda x: '${:,.2f}'.format(x))
    neighborhoods.index.name = 'Least Expensive Neighborhoods'
    neighborhoods.columns = ['Average Price per Night']
    return neighborhoods


#Price distribution
def plot_price_histogram(df):
    plt.hist(df['price'], bins=100, range=(0, 1500))
    plt.title('Price Distribution')
    plt.xlabel('Price ($)')
    plt.ylabel('Price ($) Frequency')
    plt.show()


#Calculate basic statistics about the reviews in the dataset. 
def calculate_review_stats(df):
    stats = {
        'mean_reviews': np.mean(df['number_of_reviews']),
        'median_reviews': np.median(df['number_of_reviews']),
        'min_reviews': np.min(df['number_of_reviews']),
        'max_reviews': np.max(df['number_of_reviews'])
    }
    #Formatting
    output = "Number of Reviews Summary Statistics:\n"
    output += f"Mean # of Reviews: {stats['mean_reviews']:.2f}\n"
    output += f"Median # of Reviews: {stats['median_reviews']}\n"
    output += f"Minimum # of Reviews: {stats['min_reviews']}\n"
    output += f"Maximum # of Reviews: {stats['max_reviews']}\n"
    return output


#Display the average price per room type in the dataset.
def display_avg_price_per_room_type(df):
    avg_prices = df.groupby('room_type')['price'].mean().sort_values(ascending=False)
    print("Average Price Per Room Type:")
    for room_type, avg_price in avg_prices.iteritems():
        print(f"{room_type}: ${avg_price:.2f}")



