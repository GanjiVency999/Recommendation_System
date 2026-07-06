import pandas as pd

# Load the movie data
movies = pd.read_csv("movies.csv")

print("=== Movie Recommendation System ===")
print("Available Genres:")
print(movies["Genre"].unique())

genre = input("\nEnter your favorite genre: ")

recommended = movies[movies["Genre"].str.lower() == genre.lower()]

if not recommended.empty:
    print("\nRecommended Movies:")
    for movie in recommended["Movie"]:
        print("-", movie)
else:
    print("\nSorry! No movies found for that genre.")