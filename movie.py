import webbrowser

class Movie():
    """Describe Movie objects

    Instance variables:
    title -- the title of a movie
    storyline -- the description of the movie storyline
    poster_image_url --  the url of poster image
    trailer_youtube_url -- the url to play the movie trailer

    Public methods:
    show_trailer -- open browser to play trailer for a movie
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        """Form a movie object

        Positional arguments:

        1. title -- the title of a movie
        2. storyline -- the description of the movie storyline
        3. poster_image_url --  the url of poster image
        4. trailer_youtube_url -- the url to play the movie trailer
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Open browser to play trailer for a movie
        """
        webbrowser.open(self.trailer_youtube_url)
