from helpers.time import Time
from helpers.check import Check
from helpers.random import Random

class Snowflake:
    def __init__(self, node_id: int, worker_id):
        self.node_id: int = node_id
        self.worker_id: int = worker_id
        
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

        time_since_epoch: int = bin(Time.time_since_epoch())[2:].zfill(41)
        node_id: int = bin(self.node_id)[2:].zfill(5)
        worker_id: int = bin(self.worker_id)[2:].zfill(5)
        random_12_bit_number: int = bin(Random.random_12_bit_number())[2:].zfill(12)
        
        return_string: str = f"0{time_since_epoch}{node_id}{worker_id}{random_12_bit_number}"
        return_int: int = int(return_string)
        
        print(f"Binary: {return_int}")
        print(f"Decimal: {int(return_int)}")
        
        