from flask import Flask, render_template, request
from recommender import recommend_movies, movies

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    movie_list = movies['title'].tolist()
    recommendations = []
    selected_movie = None
    if request.method == 'POST':
        selected_movie = request.form.get('movie_name')
        recommendations = recommend_movies(selected_movie)
    return render_template('index.html', movie_list=movie_list, recommendations=recommendations, selected_movie=selected_movie)

if __name__ == '__main__':
    app.run(debug=True)
