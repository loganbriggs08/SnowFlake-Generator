from snowflake import Snowflake

Snowflake_Client: object = Snowflake(node_id=1, worker_id=1)
print(Snowflake_Client.generate())