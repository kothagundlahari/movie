import fresh_tomatoes
import media

toystory = media.Movie(
         "Toy Story",
         "This is the story line for toystory",
         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
         "https://www.youtube.com/watch?v=KYz2wyBy3kc")

suicide_squad = media.Movie(
              "suicide squad",
              "A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force. Their first mission: save the world from the apocalypse.",
              "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM1OTMxNzUyM15BMl5BanBnXkFtZTgwNjYzMTIzOTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noq
              "https://www.youtube.com/watch?v=CmRih_VtVAs")

The_Accountant = media.Movie(
               "The Accountant",
               "As a math savant uncooks the books for a new client, the Treasury Department closes in on his activities and the body count starts to rise.",
               "https://images-na.ssl-images-amazon.com/images/M/MV5BNDc5Mzg2NTYxNV5BMl5BanBnXkFtZTgwMjQ2ODAwOTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",   # noq
               "https://www.youtube.com/watch?v=DBfsgcswlYQ")

Mad_Max = media.Movie(
        "Mad Max",
        "This is the story line for toystory",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SY1000_CR0,0,687,1000_AL_.jpg",   # noq
        "https://www.youtube.com/watch?v=hEJnMQG9ev8")

transporter = media.Movie(
            "The Transporter",
            "Frank is hired to transport packages for unknown clients and has made a very good living doing so. But when asked to move a package that begins moving, complications arise.",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NDc2MDAxN15BMl5BanBnXkFtZTYwNDc1NDY2._V1_.jpg",   # noq
            "https://www.youtube.com/watch?v=0poXFSvX0_4")

spy = media.Movie(
    "Spy",
    "A desk-bound CIA analyst volunteers to go undercover to infiltrate the world of a deadly arms dealer, and prevent diabolical global disaster.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNjI5OTQ0MDQxM15BMl5BanBnXkFtZTgwMzcwNjMyNTE@._V1_SY1000_SX675_AL_.jpg",   # noq
    "https://www.youtube.com/watch?v=ltijEmlyqlg")

movies = [toystory, suicide_squad, The_Accountant, Mad_Max, transporter, spy]
# fresh_tomatoes is a html page which takes movies array, containg instances of movie as an element in array
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
