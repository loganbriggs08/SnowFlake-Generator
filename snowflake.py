from helpers.time import Time
from helpers.check import Check
from helpers.random import Random

class Snowflake:
    def __init__(self, node_id: int, worker_id):
        self.node_id: int = node_id
        self.worker_id: int = worker_id
        
    @staticmethod
    def fetch_random_number(snowflake_binary: int) -> int:
        return int(snowflake_binary[52:], 2)
    
    @staticmethod
    def fetch_worker_id(snowflake_binary: int) -> int:
        return int(snowflake_binary[47:52], 2)
    
    @staticmethod
    def fetch_node_id(snowflake_binary: int) -> int:
        return int(snowflake_binary[42:47], 2)
    
    @staticmethod
    def fetch_time_since_epoch(snowflake_binary: int) -> int:
        return int(snowflake_binary[1:42], 2)
      
    def check_node_and_worker(self) -> int:
        try:
            if Check.check5Bit(self.node_id) == False or Check.check5Bit(self.worker_id) == False:
                return 0
            else:
                return 1
        except:
            return 0
        
    def generate(self) -> int:
        """Generate a random snowflake.

        Returns:
            int: Our snowflake that has been generated.
        """
        
        snowflake_binary: str = self._generate_snowflake()
        
        return snowflake_binary
    
    def _generate_snowflake(self) -> str:
        """Generate a random snowflake.

        Returns:
            str: Binary representation of the snowflake.
        """
        time_since_epoch: int = Time.time_since_epoch()
        node_id: int = self.node_id
        worker_id: int = self.worker_id
        random_12_bit_number: int = Random.random_12_bit_number()

        time_since_epoch_binary: str = bin(time_since_epoch)[2:].zfill(41)
        node_id_binary: str = bin(node_id)[2:].zfill(5)
        worker_id_binary: str = bin(worker_id)[2:].zfill(5)
        random_12_bit_number_binary: str = bin(random_12_bit_number)[2:].zfill(12)
        
        print(random_12_bit_number)
        
        snowflake_binary: str = f"0{time_since_epoch_binary}{node_id_binary}{worker_id_binary}{random_12_bit_number_binary}"
        
        return snowflake_binary
    
        