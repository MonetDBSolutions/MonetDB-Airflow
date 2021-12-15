from airflow.models.baseoperator import BaseOperator

from typing import Dict, Iterable, List, Mapping, Optional, Union

from monetdb_plugin.hooks.monetdb_hook import MonetDBHook


class MonetDBOperator(BaseOperator):
    def __init__(
        self,
        *,
        sql: Union[str, List[str]],
        monetdb_conn_id: str = 'monetdb_default',
        parameters: Optional[Union[Mapping, Iterable]] = None,
        autocommit: bool = False,
        database: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.monetdb_conn_id = monetdb_conn_id
        self.sql = sql
        self.autocommit = autocommit
        self.parameters = parameters
        self.database = database

    def execute(self, context):
        self.hook = MonetDBHook(monetdb_conn_id=self.monetdb_conn_id, schema=self.database)
        self.log.info(f"executing {self.sql}")
        self.hook.run(sql=self.sql)