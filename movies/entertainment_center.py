import fresh_tomatoes
import media


toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://ingresso-a.akamaihd.net/img/" +
    "cinema/cartaz/12264-cartaz.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A story of a marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/" +
    "pt/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

les_miserables = media.Movie(
    "Les Miserables",
    "Set in France, Jean Valjean breaks parole" +
    " after being released and runs from the grip" +
    " of Inspector Javert. The story reaches" +
    " resolution against the background of the" +
    " June Rebellion.",
    "https://upload.wikimedia.org/wikipedia/" +
    "en/b/b0/Les-miserables-movie-poster1.jpg",
    "https://www.youtube.com/watch?v=OSjbdufL828")

moulin_rouge = media.Movie(
    "Moulin Rouge",
    "A poet falls for a beautiful courtesan whom a" +
    " jealous duke covets.",
    "https://upload.wikimedia.org/wikipedia/pt/8/" +
    "8b/Moulin_Rouge%21.jpg",
    "https://www.youtube.com/watch?v=2PpgPxjzbkA")

school_of_rock = media.Movie(
    "School of Rock",
    "After being kicked out of a rock band, Dewey" +
    " Finn becomes a substitute teacher of a strict" +
    " elementary private school, only to try and" +
    " turn it into a rock band.",
    "https://upload.wikimedia.org/wikipedia/pt/1/" +
    "1b/Schoolrockposter.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat who can cook makes an unusual alliance with" +
    " a young kitchen worker at a famous restaurant.",
    "https://upload.wikimedia.org/wikipedia/pt/8/82/" +
    "Ratatouille_p%C3%B4ster.jpg",
    "https://www.youtube.com/watch?v=ALUmKa_mpik")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "While on a trip to Paris with his fiancée's" +
    " family, a nostalgic screenwriter finds" +
    " himself mysteriously going back to the" +
    " 1920s everyday at midnight.",
    "https://upload.wikimedia.org/wikipedia/" +
    "pt/b/be/Meia-noite-em-paris-poster1.jpg",
    "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie(
    "Hunger Games",
    "Katniss Everdeen voluntarily takes her younger" +
    " sister's place in the Hunger Games: a televised" +
    " competition in which two teenagers from each of" +
    " the twelve Districts of Panem are chosen at" +
    " random to fight to the death.",
    "https://upload.wikimedia.org/wikipedia/pt/4/42" +
    "/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")

phantom = media.Movie(
    "The Phantom of the Opera",
    "A young soprano becomes the obsession of a disfigured" +
    " musical genius who lives beneath the Paris Opéra" +
    " House. He kidnaps the soprano and forces the owners" +
    " of the play to keep her as the lead role of the play.",
    "https://upload.wikimedia.org/wikipedia/pt/6/65/" +
    "O_Fantasma_da_Opera_poster.jpg",
    "https://www.youtube.com/watch?v=N91AL8sAh9o")

silence = media.Movie(
    "A Quiet Place",
    "In a post-apocalyptic world, a family is forced to" +
    " live in silence while hiding from monsters with" +
    " ultra-sensitive hearing.",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/" +
    "A_Quiet_Place_film_poster.png",
    "https://www.youtube.com/watch?v=WR7cc5t7tv8")

avengers = media.Movie(
    "Avengers: Infinity War",
    "The Avengers and their allies must be willing to" +
    " sacrifice all in an attempt to defeat the powerful" +
    " Thanos before his blitz of devastation and ruin" +
    " puts an end to the universe.",
    "https://upload.wikimedia.org/wikipedia/pt/thumb/9/" +
    "90/Avengers_Infinity_War.jpg/250px-" +
    "Avengers_Infinity_War.jpg",
    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

star_wars = media.Movie(
    "Star Wars",
    "Luke Skywalker joins forces with a Jedi Knight," +
    " a cocky pilot, a Wookiee and two droids to save" +
    " the galaxy from the Empire's world-destroying" +
    " battle station, while also attempting to rescue" +
    " Princess Leia from the evil Darth Vader.",
    "https://upload.wikimedia.org/wikipedia/pt/thumb/" +
    "f/f6/P%C3%B4ster_Star_Wars.jpg/250px-P%C3%B4ster_" +
    "Star_Wars.jpg",
    "https://www.youtube.com/watch?v=XHk5kCIiGoM")

# Storing the Movie objects in the list movies
movies = [les_miserables, avatar, toy_story, moulin_rouge, school_of_rock,
          star_wars, phantom, ratatouille, midnight_in_paris, hunger_games,
          silence, avengers]

# Open the website in the user's browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)
