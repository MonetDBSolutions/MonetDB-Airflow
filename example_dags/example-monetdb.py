from datetime import datetime

from airflow import DAG

from monetdb_plugin import MonetDBOperator

dag = DAG(
    'examples',
    default_args={'retries': 1},
    tags=['example'],
    start_date=datetime(2021, 1, 1),
    catchup=False,
)

# [START howto_operator_monetdb]

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

# [END howto_operator_monetdb]


# [START howto_operator_monetdb]

t2 = MonetDBOperator(
    task_id="insert-into-table-task",
    sql="""
    INSERT INTO foo VALUES(1,2)
    """,
    dag = dag
)

# [END howto_operator_monetdb]

t1 >> t2