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

    def get_assault_target_types(self):
        return random.choice(con.assault_target_types)

    def get_recon_target(self):
        return random.choice(con.recon_targets)

    def get_recon_target_types(self):
        return random.choice(con.recon_target_types)

    def get_religious_target(self):
        return random.choice(con.religious_targets)

    def get_supply_target(self):
        return random.choice(con.supply_targets)
    
    def get_religious_culture(self):
        return random.choice(random.choice(con.religious_cultures))

    def get_title(self):
        return f'{random.choice(con.mission_first_names)} {random.choice(con.mission_second_names)}'

    def get_supply_rewards(self, is_augmented):
        if is_augmented:
            return self.get_supply_reward( min(self.get_supply_rewards_id()+1, self.get_max_supply_rewards_id())  )
        else:
            return self.get_supply_reward(self.get_supply_rewards_id())

    def get_supply_rewards_id(self):
        return random.randint(0, self.get_max_supply_rewards_id())

    def get_max_supply_rewards_id(self):
        return len(con.supply_rewards)-1
    
    def get_supply_reward(self, id):
        return con.supply_rewards[id]

    def get_supply_penalties(self, is_augmented):
        if is_augmented:
            return self.get_supply_penalty( min(self.get_supply_penalties_id()+1, self.get_max_supply_penalties_id())  )
        else:
            return self.get_supply_penalty(self.get_supply_penalties_id())

    def get_supply_penalties_id(self):
        return random.randint(0, self.get_max_supply_penalties_id())

    def get_max_supply_penalties_id(self):
        return len(con.supply_penalties)-1
    
    def get_supply_penalty(self, id):
        return con.supply_penalties[id]
        
    def get_religious_rewards(self, is_augmented):
        if is_augmented:
            return self.get_religious_reward( min(self.get_religious_rewards_id()+1, self.get_max_religious_rewards_id())  )
        else:
            return self.get_religious_reward(self.get_religious_rewards_id())

    def get_religious_rewards_id(self):
        return random.randint(0, self.get_max_religious_rewards_id())

    def get_max_religious_rewards_id(self):
        return len(con.religious_rewards)-1
    
    def get_religious_reward(self, id):
        return con.religious_rewards[id]

    def get_religious_penalties(self, is_augmented):
        if is_augmented:
            return self.get_religious_penalty( min(self.get_religious_penalties_id()+1, self.get_max_religious_penalties_id())  )
        else:
            return self.get_religious_penalty(self.get_religious_penalties_id())

    def get_religious_penalties_id(self):
        return random.randint(0, self.get_max_religious_penalties_id())

    def get_max_religious_penalties_id(self):
        return len(con.religious_penalties)-1
    
    def get_religious_penalty(self, id):
        return con.religious_penalties[id]
        
    def get_recon_rewards(self, is_augmented):
        if is_augmented:
            return self.get_recon_reward( min(self.get_recon_rewards_id()+1, self.get_max_recon_rewards_id())  )
        else:
            return self.get_recon_reward(self.get_recon_rewards_id())

    def get_recon_rewards_id(self):
        return random.randint(0, self.get_max_recon_rewards_id())

    def get_max_recon_rewards_id(self):
        return len(con.recon_rewards)-1
    
    def get_recon_reward(self, id):
        return con.recon_rewards[id]

    def get_recon_penalties(self, is_augmented):
        if is_augmented:
            return self.get_recon_penalty( min(self.get_recon_penalties_id()+1, self.get_max_recon_penalties_id())  )
        else:
            return self.get_recon_penalty(self.get_recon_penalties_id())

    def get_recon_penalties_id(self):
        return random.randint(0, self.get_max_recon_penalties_id())

    def get_max_recon_penalties_id(self):
        return len(con.recon_penalties)-1
    
    def get_recon_penalty(self, id):
        return con.recon_penalties[id]
        
    def get_assault_rewards(self, is_augmented):
        if is_augmented:
            return self.get_assault_reward( min(self.get_assault_rewards_id()+1, self.get_max_assault_rewards_id())  )
        else:
            return self.get_assault_reward(self.get_assault_rewards_id())

    def get_assault_rewards_id(self):
        return random.randint(0, self.get_max_assault_rewards_id())

    def get_max_assault_rewards_id(self):
        return len(con.assault_rewards)-1
    
    def get_assault_reward(self, id):
        return con.assault_rewards[id]

    def get_assault_penalties(self, is_augmented):
        if is_augmented:
            return self.get_assault_penalty( min(self.get_assault_penalties_id()+1, self.get_max_assault_penalties_id())  )
        else:
            return self.get_assault_penalty(self.get_assault_penalties_id())

    def get_assault_penalties_id(self):
        return random.randint(0, self.get_max_assault_penalties_id())

    def get_max_assault_penalties_id(self):
        return len(con.assault_penalties)-1
    
    def get_assault_penalty(self, id):
        return con.assault_penalties[id]

    def get_military_objectives(self):
        return con.military_objectives

    def get_assault_objectives(self):
        return [v for v in self.get_military_objectives().values() if v['is_assault'] == '1']

    def get_recon_objectives(self):
        return [v for v in self.get_military_objectives().values() if v['is_recon'] == '1']

    def get_supply_objectives(self):
        return [v for v in self.get_military_objectives().values() if v['is_supply'] == '1']

    def get_religious_objectives(self):
        d=[v for v in self.get_military_objectives().values() if v['is_religious'] == '1']
        return d

    def get_assault_objective(self):
        return random.choice(self.get_assault_objectives())

    def get_recon_objective(self):
        return random.choice(self.get_recon_objectives())

    def get_supply_objective(self):
        return random.choice(self.get_supply_objectives())

    def get_religious_objective(self):
        return random.choice(self.get_religious_objectives())

    def get_supply_problem(self):
        return random.choice(con.supply_problems)

    def get_supply_type(self):
        return random.choice(con.supply_types)