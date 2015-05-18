import webbrowser

class Movie():

    """ A simple object class to store data about movies. """

    """ Constructor. Requires 4 strings that are associated with their respective elements """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    """ Method to display the movie data in a web page provided by Udacity as part of the project """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

