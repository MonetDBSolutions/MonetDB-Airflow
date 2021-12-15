from airflow.models.baseoperator import BaseOperator

from monetdb_plugin.hooks.monetdb_hook import MonetDBHook


class MonetDBOperator(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, context):
        self.hook = MonetDBHook
        pass