import random 

class Random:
    def random_12_bit_number() -> int:
        random_number: int = random.randint(1, 4095)
        
        if random_number == 0 or random_number > 4095:
            return 0
        else:
            return random_number
            