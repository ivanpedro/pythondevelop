import media
import fresh_tomatoes

#Instances
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

#print(avatar.storyline)
#avatar.show_trailer()

Lion_Kind = media.Movie ("Lion Kind",
             "The Lion King tells the story of Simba, a young lion who is to succeed his father, Mufasa, as King of the Pride Lands",
             "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
             "https://www.youtube.com/watch?v=GibiNy4d4gc&feature=player_embedded")

#print(Lion_Kind.storyline)
#Lion_Kind.show_trailer()

#update the list and run next line to regenerate the website
movies = [toy_story, avatar, Lion_Kind]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
