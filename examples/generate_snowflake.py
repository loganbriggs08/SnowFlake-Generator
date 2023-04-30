from snowflake import Snowflake

Snowflake_Client: object = Snowflake(node_id=1, worker_id=1)
Random_Snowflake: int = Snowflake_Client.generate()

print(Random_Snowflake)
