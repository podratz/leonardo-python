import math

def make_geometric_sequence(common_ratio: int | float):
    def geometric_sequence(n: int = 1, scale_factor: int | float = 1):
        return scale_factor * (common_ratio ** n)
    return geometric_sequence

golden_ratio = (1 + math.sqrt(5)) / 2
golden_sequence = make_geometric_sequence(golden_ratio)

silver_ratio = (2 + math.sqrt(8)) / 2
silver_sequence = make_geometric_sequence(silver_ratio)

bronce_ratio = (3 + math.sqrt(13)) / 2
bronce_sequence = make_geometric_sequence(bronce_ratio)
