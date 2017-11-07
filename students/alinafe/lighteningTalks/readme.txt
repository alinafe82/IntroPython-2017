https://docs.python.org/3/library/configparser.html

brew install postgresql@9.6

echo 'export PATH="/usr/local/opt/postgresql@9.6/bin:$PATH"' >> ~/.zshrc

brew services start postgresql@9.6

note: if you cannot login, restart your Mac, the services should restart

$ psql -d postgres
SET
2017-11-03 23:08:14
Null display is "[NULL]".
Line style is unicode.
Pager usage is off.
Output format is wrapped.
Timing is on.
SET
Time: 0.085 ms
SET
Time: 0.068 ms
psql (9.6.5)
Type "help" for help.


\?

\dg[S+]
                                              List of roles
     Role name     │                         Attributes                         │ Member of │ Description 
───────────────────┼────────────────────────────────────────────────────────────┼───────────┼─────────────
 alinafe.matenda   │ Superuser, Create role, Create DB, Replication, Bypass RLS │ {}        │ 
 pg_signal_backend │ Cannot login                                               │ {}        │ 
 postgres          │                                                            │ {}        │ 

alinafe.matenda@[local]:5432/postgres# grant all on database suppliers to postgres;
GRANT
Time: 0.214 ms

alinafe.matenda@[local]:5432/postgres*# commit;
COMMIT

Time: 1.082 ms

1. create database.ini with connection string
2. config() function to read the database.ini and return connection parameters.
3.  print the connection string: python config.py
   a. check the python code style pycodestyle config.py
4. create connect.py
$ python connect.py 
{'host': 'localhost', 'database': 'suppliers', 'user': 'postgres', 'password': 'postgres'}
{'host': 'localhost', 'database': 'suppliers', 'user': 'postgres', 'password': 'postgres'}
Connecting to the PostgreSQL database...
PostgreSQL database version:
('PostgreSQL 9.6.5 on x86_64-apple-darwin16.7.0, compiled by Apple LLVM version 9.0.0 (clang-900.0.37), 64-bit',)
Database connection closed.

postgres@[local]:5432/suppliers> \dt
No relations found.
$ python createTables.py 
postgres@[local]:5432/suppliers> \dt

INSERT INTO public.daughter(
	daughter_id, name)
	VALUES (1, 'daughter1');
INSERT INTO public.daughter(
	daughter_id, name)
	VALUES (2, 'daughter2');

python  writeBlob.py
python readBlob.py

select * from daughter_pics;

