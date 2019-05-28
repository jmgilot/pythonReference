#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import sys
import sqlite3

try:
  conn = sqlite3.connect('movie.db')
except Error as e:
  print(e)

#movieList = ['tt8075192','tt7282468','tt2802850','tt5843850','tt6217608','tt7401588','tt6820256','tt8003558','tt3127022','tt6961808','tt5688932','tt8172466']
f = open("movieList.md", "w", encoding='utf-8')
f.write("# HD Movies"+'\n')

def my_function(movieId, filepath):
  params = (
    ('i', movieId),
    ('apikey', 'bd84094a'),
  )
  response = requests.get('http://www.omdbapi.com/', params=params)
  data = response.json()
  #print (data)
  #print(data["Title"])
  f.write("# "+data["Title"]+" - "+data["Year"]+'\n')
  f.write("![]("+data["Poster"]+')\n\n')
  #f.write("**IMDB ID:** "+data["imdbID"]+'\n\n')
  f.write("**With:** ")
  f.write(data["Actors"]+'\n\n')
  f.write("**Summary:** ")
  f.write(data["Plot"]+'\n\n')
  f.write("```"+'\n')
  f.write(filepath+'\n')
  f.write("```"+'\n')


for row in conn.execute('SELECT imdb, filepath FROM movie WHERE imdb is not null and moviename is null order by insertdate desc'):
  my_function(row[0], row[1])
  #print (row[0])
 
f.close()


#{'Title': 'Serpico', 'Year': '1973', 'Rated': 'R', 'Released': '26 Feb 1974', 'Runtime': '130 min', 'Genre': 'Biography, Crime, Drama, Thriller', 'Director': 'Sidney Lumet', 'Writer': 'Peter Maas (book), Waldo Salt (screenplay), Norman Wexler (screenplay)', 'Actors': 'Al Pacino, John Randolph, Jack Kehoe, Biff McGuire', 'Plot': 'An honest New York cop named Frank Serpico blows the whistle on rampant corruption in the force only to have his comrades turn against him.', 'Language': 'English, Italian, Spanish', 'Country': 'USA, Italy', 'Awards': 'Nominated for 2 Oscars. Another 5 wins & 9 nominations.', 'Poster': 'https://m.media-amazon.com/images/M/MV5BYTU4ZTI0NzAtYzMwNi00YmMxLThmZWItNTY5NzgyMDAwYWVhXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.8/10'}, {'Source': 'Rotten Tomatoes', 'Value': '90%'}, {'Source': 'Metacritic', 'Value': '87/100'}], 'Metascore': '87', 'imdbRating': '7.8', 'imdbVotes': '96,617', 'imdbID': 'tt0070666', 'Type': 'movie', 'DVD': '03 Dec 2002', 'BoxOffice': 'N/A', 'Production': 'Paramount Pictures', 'Website': 'N/A', 'Response': 'True'}



