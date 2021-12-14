# MonetDB plugin for Apache Airflow

Operators and hooks for connecting Airflow to MonetDB.

## Installation
Clone this repo inside your `$(AIRFLOW_HOME)/plugins` folder.
Then in your dags it can be used:

```python
t1 = MonetDBOperator(
    task_id="example-task",
    dag = dag
)
```

