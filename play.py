import movie # The library that contain Movie class
import fresh_tomatoes # The library to render movies data to a html page

movie1 = movie.Movie('Beauty and the Beast',
                     'The story and characters you know and love come to \
                     spectacular life in the live-action adaptation of Disneys \
                     animated classic Beauty and the Beast, a cinematic event \
                     celebrating one of the most beloved tales ever told.',
                     'https://i.ytimg.com/vi_webp/g-DkY-drN9Q/movieposter.webp',
                     'https://www.youtube.com/watch?v=g-DkY-drN9Q')
movie2 = movie.Movie('Cinderella',
                     'The story of Cinderella follows the fortunes of young \
                     Ella (Lily James) whose merchant father remarries \
                     following the death of her mother.',
                     'https://i.ytimg.com/vi_webp/UIYBoxiXsQw/movieposter.webp',
                     'https://www.youtube.com/watch?v=UIYBoxiXsQw')
movie3 = movie.Movie('Snow White And The Seven Dwarfs',
                     'Forever enchanting and inspiring, Snow White And The \
                     Seven Dwarfs embodies The Walt Disney Signature \
                     Collections legacy of animation.',
                     'https://i.ytimg.com/vi_webp/vnkf6gZ5GDY/movieposter.webp',
                     'https://www.youtube.com/watch?v=vnkf6gZ5GDY')
movie_list = [movie1, movie2, movie3]

fresh_tomatoes.open_movies_page(movie_list)
