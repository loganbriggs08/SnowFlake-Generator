# SnowFlake Generator
Ever wanted to generate Custom ID's like Discord & Twitter? Well now you can, SnowFlake-Generator allows you to create Custom ID's like you normally would but they contain useful data so it doesn't have to be fetched from the database.

## SnowFlake Structure:
SnowFlakes that are generated contain useful information that you might want to fetch from the database but now won't have to like Creation Date or Node ID, you can easily check when a users account was created. 

![App Screenshot](https://raw.githubusercontent.com/NotKatsu/SnowFlake-Generator/main/assets/snowflake.png)

Unused Bit - Like it suggest its a unused bit, if you want you can fork this repository and make this do something else that might be useful.

Creation Date - This tells you when the SnowFlake was generated the amount of milliseconds since the 6th of january 2023 is checked and added to the snowflake in binary so you can always get the creation date of your SnowFlakes easily.

Node ID: This number tells you which node generated the SnowFlake, you could use upto 31 nodes, these Nodes could generate for different things for example in Discord's case they could have a node for Users and a Node for Guilds.

Worker ID: Workers are supposed to run for Nodes and you can have 31 workers per Node so thats 961 Workers in total.

## Example:
The project is not yet on Pypi to you will have to clone the code from Github to use it in your project however ill put it in Pypi soon so it can be install with PIP.

```python
from snowflake import Snowflake

Snowflake_Client: object = Snowflake(node_id=1, worker_id=1)
Random_Snowflake: dict[str] = Snowflake_Client.generate()

Unique_Snowflake: int = Random_Snowflake["snowflake"]

print(Unique_Snowflake)
```


## Read Me:
The project took massive inspiration from https://github.com/kkrypt0nn/spaceflake and is just a Python version of this so be sure to check that project out to if your looking for a Golang alternitave.