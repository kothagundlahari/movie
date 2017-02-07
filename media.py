import webbrowser


class Movie():
    """This class provides a way to store movie  related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # function __init__ Creates Instance for each movie
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyLine = movie_storyline
        self.poster_image_url =  poster_image
        self.trailer_youtube_url = trailer_youtube

    # function show_trailer()  will use variable(self.trailer_youtube_url) from __init__ and plays youtube trailer
    def show_trailer(self):
        webbrowser.open( self.trailer_youtube_url)
