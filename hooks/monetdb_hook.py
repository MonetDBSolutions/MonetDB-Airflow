from typing import Dict
from airflow.hooks.dbapi import DbApiHook
from airflow.models import Connection

import pymonetdb

class MonetDBHook(DbApiHook):

    conn_name_attr = 'monetdb_conn_id'
    default_conn_name = 'monetdb_default'
    conn_type = 'monetdb'
    hook_name = 'MonetDB'
    supports_autocommit = True

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.schema = kwargs.pop("schema", None)
        self.connection = kwargs.pop("connection", None)

    def get_conn(self) -> pymonetdb.sql.connections.Connection:
        conn = self.connection or self.get_connection(getattr(self, self.conn_name_attr))
        info = self._get_conn_config(conn)
        return pymonetdb.connect(**info)


    def _get_conn_config(self, conn: Connection) -> Dict:
        return {
            'username': conn.login,
            'password': conn.password,
            'hostname': conn.host,
            'database': conn.schema,
        }
