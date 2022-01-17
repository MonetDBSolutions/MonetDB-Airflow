# MonetDB plugin for Apache Airflow

Operators and hooks for connecting Airflow to MonetDB.

## Installation
Clone this repo inside your `$(AIRFLOW_HOME)/plugins/monetdb_plugin` folder.
Then in your dags it can be used:

```python
from monetdb_plugin import MonetDBOperator

t1 = MonetDBOperator(
    task_id="create-table-task",
    sql="""
    CREATE TABLE IF NOT EXISTS foo(
        bar INT,
        baz INT
    );
    """,
    dag = dag
)
```

This requires [pymonetdb](https://pypi.org/project/pymonetdb/) to be installed


## Backend
MonetDB can also be used as a backend for Airflow. 

However, you do need to define a seperate schema for Airflow.
This is because Airflow tries to create a table called 'users', which already exists in the default 'sys' table in MonetDB.

```sql
CREATE SCHEMA airflow;

ALTER USER <your_user> SET SCHEMA airflow;
```

