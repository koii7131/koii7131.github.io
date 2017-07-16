import fresh_tomatoes
import media2

betty_blue = media2.Movie("37.2 le Matin",
                        "A lackadaisical handyman and aspiring novelist tries to support his younger girlfriend as she slowly succumbs to madness.",
                        "http://img.soundtrackcollector.com/movie/large/37_2_Le_Matin_(1986).jpg",
                        "https://youtu.be/YydulEgsTOE")

breathless = media2.Movie("A Bout de Souffle",
                         "A small-time thief steals a car and impulsively murders a motorcycle policeman. Wanted by the authorities, he reunites with a hip American journalism student and attempts to persuade her to run away with him to Italy.",
                         "http://br.web.img3.acsta.net/pictures/bzp/01/29.jpg",
                         "https://youtu.be/w2hDR_e1o1M")

pont_neuf = media2.Movie("Les Amants du Pont-Neuf",
                        "Alex, who's homeless and addicted to alcohol, and Michele, who's losing her sight, form a relationship while sleeping rough on Paris's Pont-Neuf bridge.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/Amantsdupontneuf.jpg/220px-Amantsdupontneuf.jpg",
                        "https://youtu.be/lbluhzI3888")

j_et_j = media2.Movie("Jules et Jim",
                     "Decades of a love triangle concerning two friends and an impulsive woman.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BZTM1MTRiNDctMTFiMC00NGM1LTkyMWQtNTY1M2JjZDczOWQ3XkEyXkFqcGdeQXVyMDI3OTIzOA@@._V1_UY268_CR9,0,182,268_AL_.jpg",
                     "https://youtu.be/x5IAYIUKTaI")

lmiyd = media2.Movie("Jeux d'Enfants",
                    "As adults, best friends Julien and Sophie continue the odd game they started as children -- a fearless competition to outdo one another with daring and outrageous stunts. While they often act out to relieve one another's pain, their game might be a way to avoid the fact that they are truly meant for one another.",
                    "https://upload.wikimedia.org/wikipedia/en/e/e7/Love_Me_If_You_Dare_movie.jpg",
                    "https://youtu.be/ICaicXbuNSU")

apostata = media2.Movie("El Apostata",
                       "An existential comedy about a Spanish man trying to apostatize from the Catholic Church.",
                       "http://t0.gstatic.com/images?q=tbn:ANd9GcRGuYw_GzgwHJDC8PwLAXhMKbnMtPtf8sfS6F9NoqBmKWlO4HNC",
                       "https://youtu.be/rnuA5o0Bf1U")

movies = [betty_blue, breathless, pont_neuf, j_et_j, lmiyd, apostata]
fresh_tomatoes.open_movies_page(movies)

#print(media2.Movie.VALID_RATINGS)
#print(media2.Movie.__doc__)
#print(media2.Movie.__name__)
#print(media2.Movie.__module__)