
def compute_cost_efficiency(can_height, can_radius, can_cost):
    volume = compute_volume(can_height, can_radius)
    cost_efficiency = volume/ can_cost
    return cost_efficiency


def main():




best_storage_effecieny = 0
for can in can_list:
    can_elements = can.split(",")
    can_name = can_elements[0]
    can_height = float(can_elements[1])
    can_radius = float(can_elements[2])
    can_cost = float(can_elements[3])
    storage_efficiency = (can_height, can_radius)
    compute_cost_efficiency = compute_cost_efficiency(can_height, can_radius)
    best_storage_effecieny = compute_storage_efficiency(can_height, can_radius)
    compute_cost_efficiency = compute_cost_efficiency(can_height, can_radius, can_cost)


