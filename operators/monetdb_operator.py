from airflow.models.baseoperator import BaseOperator

class MonetDBOperator(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, context):
        self.hook = MonetDBHook
        pass