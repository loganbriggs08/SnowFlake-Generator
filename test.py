from snowflake import Snowflake

Snowflake_Client: object = Snowflake(node_id=1, worker_id=1)
Random_Snowflake: dict[str] = Snowflake_Client.generate()
Our_Snowflake: int = Random_Snowflake["snowflake"]
Snowflake_Binary: int = Snowflake_Client.snowflake_to_binary(Our_Snowflake)

print(Our_Snowflake)
print(Snowflake_Client.fetch_random_number(Snowflake_Binary))
print(Snowflake_Client.fetch_worker_id(Snowflake_Binary))
print(Snowflake_Client.fetch_node_id(Snowflake_Binary))