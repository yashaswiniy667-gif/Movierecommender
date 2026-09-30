from sklearn.neighbors import NearestNeighbors

def get_recommendations(data, movie_names, movie_genres, movie_images,
                        movie_links, movie_descriptions, user_index, mood, k=2):

    mood_map = {
        "happy": ["comedy", "romance"],
        "sad": ["drama", "romance"],
        "excited": ["action", "thriller"],
        "bored": ["thriller", "comedy"]
    }

    mood = mood.strip().lower()
    preferred_genres = mood_map.get(mood, [])

    k = min(k, len(data) - 1)

    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(data)

    distances, indices = model.kneighbors([data[user_index]], n_neighbors=k+1)

    nearest_users = indices.flatten()[1:]
    similarities = 1 - distances.flatten()[1:]

    target_user = data[user_index]
    recommendations = []

    for i in range(len(movie_names)):

        if target_user[i] == 0:

            weighted_sum = 0
            sim_sum = 0

            for idx, user in enumerate(nearest_users):
                if data[user][i] > 0:
                    weighted_sum += similarities[idx] * data[user][i]
                    sim_sum += similarities[idx]

            if sim_sum > 0:
                predicted = weighted_sum / sim_sum

                bonus = 0.5 if movie_genres[i] in preferred_genres else 0
                final_score = predicted + bonus

                recommendations.append((
                    movie_names[i],
                    float(final_score),
                    movie_images[i],
                    movie_links[i],
                    movie_descriptions[i]
                ))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations