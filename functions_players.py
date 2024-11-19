# This code is licensed under the MIT License.
# See the LICENSE file in the root of this repository for details.

def players(heights):
    # Definition of the height ranges by position
    positions = {
        "C":  (208, 230),  # Center         (Pívot)
        "PF": (203, 210),  # Power Forward  (Ala-Pívot)
        "SF": (195, 205),  # Small Forward  (Alero)
        "SG": (193, 198),  # Shooting Guard (Escolta)
        "PG": (180, 193),  # Point Guard    (Base)
    }
    
    # We define the counters for each position
    position_counts = {"PG": 0, "SG": 0, "SF": 0, "PF": 0, "C": 0}
    
    # We review each height and assign it to the appropriate range
    for height in heights:
        for pos, (low, high) in positions.items():
            if low <= height <= high:
                if position_counts[pos] < height:
                    position_counts[pos] = height
    return position_counts
