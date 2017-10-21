 
import webbrowser

#declare class
class Movie():
    """description of class"""
    """ This class provides a way to store movie related information. """
    
    #class variable
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    #constructor of the class
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        
        #instance Variable
        #can be access only inside the class with self 
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    #instance methods
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


