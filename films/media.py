import webbrowser


class Movie:
    """This class provides information about the movies"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
            self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Initiating with the matched information

        :param movie_title: The title of the movie.
        :param movie_storyline: The storyline of the movie.
        :param poster_image: The poster image of the movie.
        :param trailer_youtube: The trailer video of the movie.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Showing the website on google chrome with the given youtube url"""
        webbrowser.get("open -a /Applications\
        /Google\ Chrome.app %s").open(self.trailer_youtube_url)
