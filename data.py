import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies = [
    ("Avengers", "action", os.path.join(BASE_DIR, "images/avengers.jpg"),
     "https://www.youtube.com/watch?v=eOrNdBpGMv8",
     "Earth's mightiest heroes unite to stop a global threat."),

    ("Titanic", "romance", os.path.join(BASE_DIR, "images/titanic.jpg"),
     "https://www.youtube.com/watch?v=kVrqfYjkTdQ",
     "A tragic love story aboard the doomed Titanic."),

    ("Avatar", "action", os.path.join(BASE_DIR, "images/avatar.jpg"),
     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
     "A soldier on an alien world chooses between duty and love."),

    ("Inception", "thriller", os.path.join(BASE_DIR, "images/inception.jpg"),
     "https://www.youtube.com/watch?v=YoHD9XEInc0",
     "A thief enters dreams to plant ideas into minds."),

    ("Deadpool", "comedy", os.path.join(BASE_DIR, "images/deadpool.jpg"),
     "https://www.youtube.com/watch?v=ONHBaC-pfsk",
     "A sarcastic anti-hero seeks revenge in hilarious ways."),

    ("Fight Club", "drama", os.path.join(BASE_DIR, "images/fightclub.jpg"),
     "https://www.youtube.com/watch?v=SUXWAEX2jlg",
     "An underground fight club evolves into something darker."),

    ("Joker", "drama", os.path.join(BASE_DIR, "images/joker.jpg"),
     "https://www.youtube.com/watch?v=zAGVQLHvwOY",
     "A struggling comedian spirals into madness."),

    ("La La Land", "romance", os.path.join(BASE_DIR, "images/lalaland.jpg"),
     "https://www.youtube.com/watch?v=0pdqf4P9MB8",
     "Two dreamers fall in love chasing their ambitions."),

    ("Mr Bean's Holiday", "comedy", os.path.join(BASE_DIR, "images/mrbeansholiday.jpg"),
     "https://www.youtube.com/watch?v=hSxLUd8aly4",
     "Mr. Bean travels to France causing chaos everywhere."),

    ("The Conjuring", "thriller", os.path.join(BASE_DIR, "images/theconjuring.jpg"),
     "https://www.youtube.com/watch?v=k10ETZ41q5o",
     "Paranormal investigators face a terrifying case.")
]

movie_names = [m[0] for m in movies]
movie_genres = [m[1] for m in movies]
movie_images = [m[2] for m in movies]
movie_links = [m[3] for m in movies]
movie_descriptions = [m[4] for m in movies]

data = np.array([
    [5, 3, 4, 0, 5, 2, 3, 4, 0, 1],
    [4, 0, 5, 1, 4, 3, 2, 0, 5, 2],
    [1, 1, 5, 5, 2, 4, 5, 3, 1, 4],
    [0, 0, 5, 4, 3, 5, 4, 2, 0, 5],
    [5, 4, 0, 0, 5, 3, 4, 5, 2, 1]
], dtype=float)