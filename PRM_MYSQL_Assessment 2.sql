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
    -> COUNTRY_ID varchar(2),
    -> COUNTRY_NAME varchar(40),
    -> REGION_ID decimal(10,0)
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> CREATE table COUNTRY_NEW as
    -> SELECT * from countries;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SHOW tables;
+------------------+
| Tables_in_edyoda |
+------------------+
| countries        |
| country_new      |
| customers        |
| orders           |
| salespeople      |
+------------------+
5 rows in set (0.00 sec)
