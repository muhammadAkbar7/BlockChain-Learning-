import hashlib


class SeaBlock:

    def __init__(self, previous_hash, transactions): # constructor defined as (previous hash, transactions list)
        self.previous_hash = previous_hash
        self.transactions = transactions

        self.block_data = "-".join(transactions) + "-" + previous_hash  # string concatenation
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() # when we encode the hash, we want to turn it into readable string; therefore hexdigest

t1 = "Mo sends 1 SB to Jordan"
t2 = "Bob sends 1 SB to Bill"
t3 = "Joe sends 1 SB to Matt"


initial_block = SeaBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = SeaBlock(initial_block.block_hash, [t3])

print(second_block.block_data)
print(second_block.block_hash)




