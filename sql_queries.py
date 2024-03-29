# DROP TABLES
# Drop tables if it exists.
# Reference: http://www.postgresqltutorial.com/postgresql-drop-table/
time_table_drop = "DROP TABLE IF EXISTS time"
song_table_drop = "DROP TABLE IF EXISTS songs"
user_table_drop = "DROP TABLE IF EXISTS users"
artist_table_drop = "DROP TABLE IF EXISTS artists"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"


# CREATE TABLES
# Reference for timestamp: https://stackoverflow.com/questions/9826833/create-table-in-postgresql
# Reference for float: Udacity Lesson 2 Demo 3
# Reference for float: https://stackoverflow.com/questions/21565183/create-a-table-of-two-types-in-postgresql
# Reference (CONSTAINTS settings): https://stackoverflow.com/questions/34132814/best-practices-to-prevent-duplicate-data-pandas-postgres
songplay_table_create = '''
                        CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, 
                                                              start_time TIMESTAMP, user_id INT, 
                                                              level VARCHAR, song_id VARCHAR, artist_id VARCHAR,     
                                                              session_id INT, location VARCHAR, user_agent VARCHAR,
                                                              
                                                              CONSTRAINT unique_event UNIQUE (start_time, user_id, song_id));
                        '''


user_table_create = '''
                        CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, first_name VARCHAR, 
                                                          last_name VARCHAR, gender VARCHAR, level VARCHAR);
                    '''


song_table_create = '''
                        CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR PRIMARY KEY, title VARCHAR, 
                                                          artist_id VARCHAR, year INT, duration NUMERIC);
                    '''


artist_table_create = '''
                          CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR PRIMARY KEY, name VARCHAR, 
                                                              location VARCHAR, latitude NUMERIC, longitude NUMERIC);
                      '''


time_table_create = '''
                        CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMP, 
                                                         hour INT, day INT, week INT, 
                                                         month INT, year INT, weekday INT);
                    '''


# INSERT RECORDS
songplay_table_insert = '''
                        INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                        ON CONFLICT ON CONSTRAINT unique_event DO NOTHING;
                        '''


user_table_insert = '''
                    INSERT INTO users (user_id, first_name, last_name, gender, level) 
                                VALUES (%s, %s, %s, %s, %s)
                                ON CONFLICT (user_id) DO NOTHING;
                    '''


song_table_insert = '''
                    INSERT INTO songs (song_id, title, artist_id, year, duration) 
                                VALUES (%s, %s, %s, %s, %s)
                                ON CONFLICT (song_id) DO NOTHING;
                    '''


artist_table_insert = '''
                      INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                                VALUES (%s, %s, %s, %s, %s)
                                ON CONFLICT (artist_id) DO NOTHING;
                      '''


time_table_insert = '''
                    INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s);
                    '''


# FIND SONGS
song_select = '''
                   SELECT song_id, artist_id
                   FROM (SELECT * FROM artists) A INNER JOIN
                        (SELECT * FROM songs) B USING (artist_id)
                   WHERE title = %s AND name = %s AND duration = %s;
              '''


# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]