from airflow.plugins_manager import AirflowPlugin

from monetdb_plugin.operators.monetdb_operator import MonetDBOperator

class MonetDBPlugin(AirflowPlugin):
    name = "monetdb_plugin"
    operators = [MonetDBOperator]
    sensors = []
    hooks = []
    executors = []
    admin_views = []
    flask_blueprints = []
    menu_links = []