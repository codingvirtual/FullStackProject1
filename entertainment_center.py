import media
import fresh_tomatoes

""" Define 6 movies to display on the page """

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie(
    "Avatar",
    "A Marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch=v?-9ceBgWV8io")

school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Going back in time to meet authors",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://youtu.be/FAfR8omt-CY")

hunger_games = media.Movie(
    "The Hunger Games",
    "A really real reality show",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch=v?Pba63a7H0bo")

""" Assemble movies into an array so they can be passed to the function
provided by the Udacity starter code """

movies = [toy_story, avatar, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

""" Call provided code to display a properly formatted movies page """
fresh_tomatoes.open_movies_page(movies)
