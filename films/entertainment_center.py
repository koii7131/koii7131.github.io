import fresh_tomatoes
import media

"""This file has the information about the movies"""
betty_blue = media.Movie(
                        "37.2 le Matin",
                        "A lackadaisical handyman and \
                        aspiring novelist tries to \
                        support his younger girlfriend as \
                        she slowly succumbs to \
                        madness.",
                        "https://1.bp.blogspot.com/-htoaFeZ2rQg\
                        /UaTGuwS8GXI/AAAAAAAAewk/CuwnXWxmSBo/\
                        s1600/affiche-37d-2-le-matin-1985-1.jpg",
                        "https://youtu.be/YydulEgsTOE")

breathless = media.Movie(
                        "A Bout de Souffle",
                        "A small-time thief steals a car and \
                        impulsively murders a motorcycle policeman. \
                        Wanted by the authorities, he reunites \
                        with a hip American journalism student and \
                        attempts to persuade her to \
                        run away with him to Italy.",
                        "http://br.web.img3.acsta.net/pictures/bzp/01/29.jpg",
                        "https://youtu.be/w2hDR_e1o1M")

pont_neuf = media.Movie(
                        "Les Amants du Pont-Neuf",
                        "Alex, who's homeless and addicted to alcohol, \
                        and Michele, who's losing her sight, \
                        form a relationship while sleeping rough \
                        on Paris's Pont-Neuf bridge.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/\
                        b/b7/Amantsdupontneuf.jpg/220px-Amantsdupontneuf.jpg",
                        "https://youtu.be/lbluhzI3888")

j_et_j = media.Movie(
                    "Jules et Jim",
                    "Decades of a love triangle concerning two \
                    friends and an impulsive woman.",
                    "https://images-na.ssl-images-amazon.com/images/M/\
                    MV5BZTM1MTRiNDctMTFiMC00NGM1LTkyMWQtNTY1M2JjZD\
                    czOWQ3XkEyXkFqcGdeQXVyMDI3OTIzOA@@\
                    ._V1_UY268_CR9,0,182,268_AL_.jpg",
                    "https://youtu.be/x5IAYIUKTaI")

lmiyd = media.Movie(
                    "Jeux d'Enfants",
                    "As adults, best friends Julien and Sophie \
                    continue the odd game they started \
                    as children -- a fearless competition to outdo \
                    one another with daring and outrageous stunts. \
                    While they often act out to relieve one another's \
                    pain, their game might be a way to \
                    avoid the fact that they are truly meant for one another.",
                    "https://upload.wikimedia.org/wikipedia/en/e/\
                    e7/Love_Me_If_You_Dare_movie.jpg",
                    "https://youtu.be/ICaicXbuNSU")

apostata = media.Movie(
                    "El Apostata",
                    "An existential comedy about a Spanish man \
                    trying to apostatize from the Catholic Church.",
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcR\
                    GuYw_GzgwHJDC8PwLAXhMKbnMtPtf8sfS6F9NoqBmKWlO4HNC",
                    "https://youtu.be/rnuA5o0Bf1U")

"""Putting information on each film into an array"""
movies = [betty_blue, breathless, pont_neuf, j_et_j, lmiyd, apostata]

"""Deploying information using fresh_tomatoes"""
fresh_tomatoes.open_movies_page(movies)
