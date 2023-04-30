from helpers.check import Check

class Snowflake:
    def __init__(self, node_id: int, worker_id):
        self.node_id: int = node_id
        self.worker_id: int = worker_id
        
    def generate(self) -> int:
        try:
            if Check.check5Bit(self.node_id) == False or Check.check5Bit(self.worker_id) == False:
                return 0
            else:
                return 1
        except:
            return 0