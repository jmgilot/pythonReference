#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from pathlib import Path

try:
    conn = sqlite3.connect('movie.db')
except Error as e:
    print(e)
 
c = conn.cursor()
#c.execute("DELETE FROM MOVIE")

f = open("list.txt", encoding='utf-8')

for line in f:
    right,one,user,group,filesize,insertdate,ctime,filepath=line.split(' ',7)
    filename = Path(filepath)
    folder = filename.parent
    imdbid = filename.stem.split("--")
    if len(imdbid) == 2:
     imdb = imdbid[1]
     print (filename.stem, imdb)
    else:
     imdb = ''
    val = (imdb,filepath,filesize,filename.name,filename.suffix,insertdate)
    try:
      c.execute("INSERT INTO movie (imdb,filepath, filesize, filename, extension, insertdate) VALUES (?,?,?,?,?,?)", val)
    except sqlite3.IntegrityError as e:
     pass

f.close()

# Save (commit) the changes
conn.commit()
conn.close()