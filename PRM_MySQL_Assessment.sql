mysql> SHOW databases;
+--------------------+
| Database           |
+--------------------+
| edyoda             |
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| punnadb            |
| sys                |
| tharun_db          |
+--------------------+
8 rows in set (0.00 sec)

mysql> USE edyoda;
Database changed
mysql> SHOW tables;
+------------------+
| Tables_in_edyoda |
+------------------+
| customers        |
| orders           |
| salespeople      |
+------------------+
3 rows in set (0.00 sec)

mysql> CREATE table countries(
    -> Country_ID int,
    -> Country_Name varchar(48),
    -> Region_ID int,
    -> CHECK(Country_Name IN('italy','india','china'))
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> SHOW tables;
+------------------+
| Tables_in_edyoda |
+------------------+
| countries        |
| customers        |
| orders           |
| salespeople      |
+------------------+
4 rows in set (0.00 sec)
