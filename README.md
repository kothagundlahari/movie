#Synopsis
This project opens a web page( Fresh Tomatoes!) displays movie posters when you click any one of the posters it plays a
youtube trailer for that particular poster.

###movie/media.py:
Class Movie() will be used to instantiated objects for each movie with param movie_title, movie_storyline, poster_image, trailer_youtube. The function show_trailer() will be used to open youtube trailer.


###movie/entertainment_center.py:
Each movie is instantiated with media.Movie() and all the movies which are instantiated are arranged in an array(movies) and is passed as a parameter for fresh_tomatoes.open_movies_page(movies), to display an HTML page.

###movie/fresh_tomatoes.html:
Takes the movies array in entertainment_center.py and display the HTML page

How to run the code
Go to movie/entertainment_center.py and run it in your environment

Installation
move to the location in System and type
git clone https://github.com/kothagundlahari/movie.git

License
This project is licensed under the MIT License - see the LICENSE.md file for details
