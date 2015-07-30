import media   # this is the media.py file
import fresh_tomatoes



#media is the file, Movie is the class within that file
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")   

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pcu = media.Movie("PCU",
				  "PCU is a 1994 American comedy film written by Adam Leff and Zak Penn and directed by Hart Bochner about college life at the fictional Port Chester University, and represents 'an exaggerated view of contemporary college life....' The film is based on the experiences of Leff and Penn at Eclectic Society at Wesleyan University in Middletown, Connecticut.",
				  "https://upload.wikimedia.org/wikipedia/en/6/66/PCUposter.jpg",
				  "https://www.youtube.com/watch?v=T2Fp61jJcIs")

cars =media.Movie("Cars",
				  "Lighning McQueen takes a wrong turn and ends up finding happiness",
				  "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
				  "https://www.youtube.com/watch?v=WGByijP0Leo")

dispicable_me_2 = media.Movie("Dispicable Me 2",
							  "Purple Minions!!!!",
							  "https://upload.wikimedia.org/wikipedia/en/2/29/Despicable_Me_2_poster.jpg",
							  "https://www.youtube.com/watch?v=AuzyODgWRp4")

chef = media.Movie("Chef",
				  "Carl gets his chance",
				  "https://upload.wikimedia.org/wikipedia/en/b/b8/Chef_2014.jpg",
				  "https://www.youtube.com/watch?v=mJiN6a7K5fI")
#print(avatar.storyline)
#avatar.show_trailer()








movies = [toy_story, avatar,pcu,cars,dispicable_me_2,chef]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
