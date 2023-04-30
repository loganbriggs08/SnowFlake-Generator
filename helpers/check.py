variables: dict[str] = {
    "MAX5BITS": 31,
	"MAX12BITS": 4095,
	"MAX41BITS": 2199023255551
}

class Check:
    def fiveBit(number: int) -> bool:
        """Check if a 5 bit number is valid.

        Args:
            node_id (int): The number to check.

        Returns:
            bool: True if the number is valid, False otherwise.
        """
        
        if number > variables["MAX5BITS"] or number == 0:
            return False
        else:
            return True
        
    def twelveBit(number: int) -> bool:
        """Check if a 12 bit number is valid.

        Args:
            worker_id (int): The number to check.

        Returns:
            bool: True if the number is valid, False otherwise.
        """
        
        if number > variables["MAX12BITS"] or number == 0:
            return False
        else:
            return True
        
    def fortyOneBit(number: int) -> bool:
        """Check if a 41 bit number is valid.

        Args:
            number (int): The number to check.

        Returns:
            bool: True if the number is valid, False otherwise.
        """
        
        if number > variables["MAX41BITS"] or number == 0:
            return False 
        else:
            return True