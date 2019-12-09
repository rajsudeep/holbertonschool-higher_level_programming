# SQL - More Queries
### [0. My privileges](./0-privileges.sql)
> Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost)
### [1. Root user](./1-create_user.sql)
> Write a script that creates the MySQL server user user_0d_1
### [2. Read user](./2-create_read_user.sql)
> Write a script that creates the database hbtn_0d_2 and the user user_0d_2
### [3. Always a name](./3-force_name.sql)
> Write a script that creates the table force_name on your MySQL server
> * id INT
> * name VARCHAR(256) can’t be null
### [4. ID can't be null](./4-never_empty.sql)
> Write a script that creates the table id_not_null on your MySQL server
> * id INT with the default value 1
> * name VARCHAR(256)
### [5. Unique ID](./5-unique_id.sql)
> Write a script that creates the table unique_id on your MySQL server
> * id INT with the default value 1 and must be unique
> * name VARCHAR(256)
### [6. States table](./6-states.sql)
> Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
> * id INT unique, auto generated, can’t be null and is a primary key
> * name VARCHAR(256) can’t be null
### [7. Cities table](./7-cities.sql)
> Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
> * id INT unique, auto generated, can’t be null and is a primary key
> * state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
> * name VARCHAR(256) can’t be null
### [8. Cities of California](./8-cities_of_california_subquery.sql)
> Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa
> * The states table contains only one record where name = California (but the id can be different, as per the example)
> * Results must be sorted in ascending order by cities.id
### [9. Cities by States](./9-cities_by_state_join.sql)
> Write a script that lists all cities contained in the database hbtn_0d_usa
> * Each record should display: cities.id - cities.name - states.name
> * Results must be sorted in ascending order by cities.id
> * You can use only one SELECT statement
### [10. Genre ID by show](./10-genre_id_by_show.sql)
> Import the database dump from [hbtn_0d_tvshows](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) to your MySQL server
> Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
> * Each record should display: tv_shows.title - tv_show_genres.genre_id
> * Results must be sorted in ascending order by title and genre_id
### [11. Genre ID for all shows](./11-genre_id_all_shows.sql)
> Write a script that lists all shows contained in the database hbtn_0d_tvshows (use db dump from task 10)
### [12. No genre](./12-no_genre.sql)
> Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked (use db dump from task 10)
### [13. Number of shows by genre](./13-count_shows_by_genre.sql)
> Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each (use db dump from task 10)
### [14. My genres](./14-my_genres.sql)
> Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
### [15. Only Comedy](./15-comedy_only.sql)
> Write a script that lists all Comedy shows in the database hbtn_0d_tvshows
### [16. List shows and genres](./16-shows_by_genre.sql)
> Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
