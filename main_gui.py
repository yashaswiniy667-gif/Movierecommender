import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import os
import webbrowser
from PIL import Image, ImageTk

from data import data, movie_names, movie_genres, movie_images, movie_links, movie_descriptions
from recommender import get_recommendations

os.makedirs("output", exist_ok=True)

root = tk.Tk()
root.title("🎬 Movie Recommender")
root.geometry("650x750")

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

tk.Label(scrollable_frame, text="Movie Recommendation System",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(scrollable_frame, text="Enter Mood (happy/sad/excited/bored):").pack()
mood_entry = tk.Entry(scrollable_frame)
mood_entry.pack(pady=5)

entries = []
tk.Label(scrollable_frame, text="Rate Movies (0 if not watched):").pack(pady=10)

for movie in movie_names:
    frame = tk.Frame(scrollable_frame)
    frame.pack(pady=2)

    tk.Label(frame, text=movie, width=22, anchor='w').pack(side=tk.LEFT)
    entry = tk.Entry(frame, width=5)
    entry.pack(side=tk.RIGHT)

    entries.append(entry)

result_text = tk.Text(scrollable_frame, height=8, width=70)
result_text.pack(pady=10)

result_frame = tk.Frame(scrollable_frame)
result_frame.pack()

def recommend_movies():

    for widget in result_frame.winfo_children():
        widget.destroy()

    try:
        mood = mood_entry.get().strip().lower()

        user_ratings = []
        for entry in entries:
            val = entry.get().strip()
            if val == "":
                val = 0
            user_ratings.append(int(val))

        new_data = np.vstack([data, user_ratings])
        user_index = len(new_data) - 1

        recommendations = get_recommendations(
            new_data, movie_names, movie_genres,
            movie_images, movie_links, movie_descriptions,
            user_index, mood
        )

        result_text.delete("1.0", tk.END)

        if not recommendations:
            result_text.insert(tk.END, "No recommendations found.\n")
            return

        for movie, rating, img_path, link, desc in recommendations[:3]:

            result_text.insert(tk.END, f"{movie} -> {round(rating,2)}\n")
            result_text.insert(tk.END, f"{desc}\n\n")

            item_frame = tk.Frame(result_frame, bd=2, relief="groove")
            item_frame.pack(pady=10)

            tk.Label(item_frame, text=movie,
                     font=("Arial", 12, "bold")).pack()

            try:
                if os.path.exists(img_path):
                    img = Image.open(img_path)
                    img = img.resize((120, 180))
                    photo = ImageTk.PhotoImage(img)

                    img_label = tk.Label(item_frame, image=photo)
                    img_label.image = photo
                    img_label.pack()
                else:
                    tk.Label(item_frame, text="Image not found").pack()
            except:
                tk.Label(item_frame, text="Image error").pack()

            tk.Label(item_frame, text=desc, wraplength=250, justify="center").pack()

            tk.Button(item_frame,
                      text="Watch Trailer",
                      command=lambda url=link: webbrowser.open(url),
                      bg="red", fg="white").pack(pady=5)

        df = pd.DataFrame(recommendations, columns=["Movie", "Rating", "Image", "Trailer", "Description"])
        df.to_csv("output/final_recommendations.csv", index=False)

    except Exception as e:
        messagebox.showerror("Error", str(e))


tk.Button(scrollable_frame, text="Get Recommendations",
          command=recommend_movies, bg="blue", fg="white").pack(pady=10)

root.mainloop()