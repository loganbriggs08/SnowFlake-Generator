from snowflake import Snowflake

Snowflake_Client: object = Snowflake(node_id=1, worker_id=1)
Random_Snowflake: int = Snowflake_Client.generate()

print(Random_Snowflake)

# print(Snowflake_Client.fetch_random_number(Random_Snowflake))
# print(Snowflake_Client.fetch_worker_id(Random_Snowflake))
# print(Snowflake_Client.fetch_node_id(Random_Snowflake))