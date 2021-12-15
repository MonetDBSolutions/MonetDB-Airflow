# MonetDB plugin for Apache Airflow

Operators and hooks for connecting Airflow to MonetDB.

## Installation
Clone this repo inside your `$(AIRFLOW_HOME)/plugins/monetdb_plugin` folder.
Then in your dags it can be used:

```python
from monetdb_plugin import MonetDBOperator

t1 = MonetDBOperator(
    task_id="example-task",
    dag = dag
)
```

