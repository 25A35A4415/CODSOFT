movies = {
    "RRR": ["Bahubali", "KGF", "Pushpa"],
    "Bahubali": ["RRR", "KGF", "Salaar"],
    "KGF": ["Salaar", "Pushpa", "RRR"],
    "Pushpa": ["KGF", "RRR", "Salaar"],
    "Salaar": ["KGF", "Bahubali", "Pushpa"]
}

print("=== Movie Recommendation System ===")
print("Available Movies:")
for movie in movies:
    print("-", movie)

user_movie = input("\nEnter a movie name: ")

if user_movie in movies:
    print("\nRecommended Movies:")
    for rec in movies[user_movie]:
        print("-", rec)
else:
    print("Movie not found in database.")
