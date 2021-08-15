import csv

#let’s create a new file merge_csv.py and in this, let’s make the imports, read our original
#movies.csv and separate out the headers and the data.

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
    
#Explanation of above code - Here, we are importing the csv library.
#We are then opening our movies.csv and reading the data out of it. We are
#storing all our movie’s data in all_movies and we are storing the
#headers in headers

headers.append("poster_link")

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    
#Explanation of code - Here, we are appending the variable poster_link in our headers. We are
#then creating a new file final.csv and we are appending the headers into it.

#note- The “a+” attribute means that we want to append in the file. This means
#that the old data would not be deleted but the new data will be added. “w”
#on the other hand removes all the data from the file and then adds new data


#read the contents of the movie’s poster links and store it in a variable.

with open("movie_links.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]

###Problem###
#Now, if we observe closely, the original data that we have contains 4,807 rows while the movie’s poster
#link contains 4,748 rows. This means that we do not have poster links for a few movies.

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)
                        
##Explanation of above code ###
#Here, we are first iterating over all the movie data that we have.
#We are then checking if there is any row in the movie’s poster link data
#that contains the name of the movie with the any() function. This will
#simply return True or False.If we found a poster, we are iterating
#over all the movies in the movie’s poster links data and comparing the
#names. If we find the corresponding poster of a movie, we are appending
#this link into our original movie’s data and then writing this entire movie’s
#data in the final.csv.


##Note- 
#we are also checking if the total length is 28 or not. Ideally,we should have 28 columns. 
# If the number of columns is not 28, we are not adding the movie’s data. This will
#remove inconsistency from our data.