class Movies:
    def __init__(self, movie):
        self.movies = []
        self.movie = movie
    
    def add_movie(self, movie):
        self.movie = movie
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедия: {movie}"

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драма: {movie}"


comedy = Comedy("")
drama = Drama("")

print(comedy.add_movie("Большой куш"))
print(drama.add_movie("Оружейный барон"))

