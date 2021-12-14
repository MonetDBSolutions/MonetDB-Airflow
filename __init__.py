from airflow.plugins_manager import AirflowPlugin

from monetdb_plugin.operators.monetdb_operator import MonetDBOperator
from monetdb_plugin.hooks.monetdb_hook import MonetDBHook

class MonetDBPlugin(AirflowPlugin):
    name = "monetdb_plugin"
    operators = [MonetDBOperator]
    sensors = []
    hooks = [MonetDBHook]
    executors = []
    admin_views = []
    flask_blueprints = []
    menu_links = []