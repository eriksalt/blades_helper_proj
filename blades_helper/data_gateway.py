import random
from blades_helper.mission_generator_constants import MissionGeneratorConstants as con

class DataGateway:
    def __init__(self):
        pass
    def get_random_mission (self, missions):
        return random.choice(missions)

    def get_mission_type(self):
        return random.choice(con.mission_types)

    def get_simple_mission_type(self):
        return random.choice(con.mission_types[0:3])

    def get_mission_count(self):
        return random.choice(con.mission_counts)

    def get_favor_type(self):
        return random.choice(con.favor_types)

    def get_specialist(self):
        return random.choice(con.specialists)

    def get_assault_target(self):
        return random.choice(con.assault_targets)

    def get_simple_assault_target(self):
        return self.get_assault_target()

    def get_simple_recon_target(self):
        return random.choice(con.recon_targets[0:4])

    def get_simple_religious_target(self):
        return random.choice(con.religious_targets[0:3])

    def get_assault_rewards(self):
        return random.choice(con.assault_rewards)

    def get_assault_penalties(self):
        return random.choice(con.assault_penalties)

    def get_assault_target_types(self):
        return random.choice(con.assault_target_types)

    def get_recon_target(self):
        return random.choice(con.recon_targets)

    def get_recon_rewards(self):
        return random.choice(con.recon_rewards)

    def get_recon_penalties(self):
        return random.choice(con.recon_penalties)

    def get_recon_target_types(self):
        return random.choice(con.recon_target_types)

    def get_religious_target(self):
        return random.choice(con.religious_targets)

    def get_religious_rewards(self):
        return random.choice(con.religious_rewards)

    def get_religious_penalties(self):
        return random.choice(con.religious_penalties)

    def get_supply_target(self):
        return random.choice(con.supply_targets)

    def get_supply_rewards(self):
        return random.choice(con.recon_rewards)

    def get_supply_penalties(self):
        return random.choice(con.supply_penalties)
    
    def get_religious_culture(self):
        return random.choice(random.choice(con.religious_cultures))

    def get_title(self):
        return f'{random.choice(con.mission_first_names)} {random.choice(con.mission_second_names)}'
