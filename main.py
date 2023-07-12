import utilities

# Load the data
data = utilities.load_data('AB_NYC_2019.csv')

print("Analyzing AirBnB Prices in New York City")
print("For Tourists' Future Trip Planning")
print("")

#Neighborhoods with the highest average price
top_neighborhoods = utilities.get_top_neighborhoods(data, 10)
print(top_neighborhoods)
print("")

#Neighborhoods with the lowest average price
lowest_priced_neighborhoods = utilities.get_low_neighborhoods(data, 10)
print(lowest_priced_neighborhoods)
print("")

#Histogram of the prices of all listings
utilities.plot_price_histogram(data)
print("")

#Summary statistics about the reviews per listing
review_stats = utilities.calculate_review_stats(data)
print(review_stats)

#Average price per room type
avg_prices = utilities.display_avg_price_per_room_type(data)





