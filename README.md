Project: Data Modeling with Postgres

Context and problem motivation
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

Project Description
In this project, we performed data modeling with Postgres and build an ETL pipeline using Python. Star schema inspired appropriate fact and dimension tables were designed which is populated by the aforestated ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

-- To run the scripts, perform the following steps
1. open terminal
2. in terminal, run: python create_tables.py
    -- Step 1: This will delete/drop the old tables, if there was any.
    -- Step 2: Create table schema appropraite for the project using the sql queries from the script sql_queries.py
3. in terminal, run: python etl.py
    -- ETL pipeline that transfers data from files in two local directories (within data folder) into these tables in Postgres using Python and SQL. The prototying of the ETL was done in the jupyter notebook: etl.ipynb, where as the initial testing was done in the jupyter notebook (test.ipynb)

