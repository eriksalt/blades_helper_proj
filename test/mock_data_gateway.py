from blades_helper.data_gateway import DataGateway

class MockDataGateway(DataGateway):
    def __init__(self):
        super().__init__()
        #Generral Data Tables
        self.mission_types = []
        self.mission_counts = []
        self.favor_types = []
        self.specialists = []
        #Assault data tables
        self.assault_targets = []
        self.assault_target_types =[]
        #Recon data tables
        self.recon_targets = []
        self.recon_target_types= []
        #Religious data tables
        self.religious_targets = []
        self.religious_cultures = []
        #Supply data tables
        self.supply_targets = []
        self.simple_mission_types=[]
        self.simple_recon_targets=[]
        self.simple_religious_targets=[]
        self.random_missions=[]
        self.titles=[]

        self.religious_reward_max_ids=[]
        self.religious_reward_ids=[]
        self.religious_rewards=[]
        self.religious_penalty_max_ids=[]
        self.religious_penalty_ids=[]
        self.religious_penalties=[]

        self.supply_reward_max_ids=[]
        self.supply_reward_ids=[]
        self.supply_rewards=[]
        self.supply_penalty_max_ids=[]
        self.supply_penalty_ids=[]
        self.supply_penalties=[]

        self.recon_reward_max_ids=[]
        self.recon_reward_ids=[]
        self.recon_rewards=[]
        self.recon_penalty_max_ids=[]
        self.recon_penalty_ids=[]
        self.recon_penalties=[]
        
        self.assault_reward_max_ids=[]
        self.assault_reward_ids=[]
        self.assault_rewards=[]
        self.assault_penalty_max_ids=[]
        self.assault_penalty_ids=[]
        self.assault_penalties=[]

        self.military_ojectives=[]
        self.assault_objectives=[]
        self.assault_objective=[]
        self.recon_objectives=[]
        self.recon_objective=[]
        self.supply_objectives=[]
        self.supply_objective=[]
        self.religious_objectives=[]
        self.religious_objective=[]

        self.old_assault_objective=None
        self.old_recon_objective=None
        self.old_supply_objective=None
        self.old_religious_objective=None


    def get_military_objectives(self):
        if len(self.military_ojectives) >0:
            return self.military_ojectives.pop()
        else:
            return super().get_military_objectives()

    def get_assault_objectives(self):
        if len(self.assault_objectives) >0:
            return self.assault_objectives.pop()
        else:
            return super().get_assault_objectives()        

    def get_recon_objectives(self):
        if len(self.recon_objectives) >0:
            return self.recon_objectives.pop()
        else:
            return super().get_recon_objectives()        

    def get_supply_objectives(self):
        if len(self.supply_objectives) >0:
            return self.supply_objectives.pop()
        else:
            return super().get_supply_objectives()        

    def get_religious_objectives(self):
        if len(self.religious_objectives) >0:
            return self.religious_objectives.pop()
        else:
            return super().get_religious_objectives()        

    def get_assault_objective(self):
        d=''
        if len(self.assault_objective) >0:
            d= self.assault_objective.pop()
        else:
            d= super().get_assault_objective()        
        self.old_assault_objective = d
        return d

    def get_recon_objective(self):
        d=''
        if len(self.recon_objective) >0:
            d= self.recon_objective.pop()
        else:
            d= super().get_recon_objective()        
        self.old_recon_objective = d
        return d

    def get_supply_objective(self):
        d=''
        if len(self.supply_objective) >0:
            d= self.supply_objective.pop()
        else:
            d= super().get_supply_objective()        
        self.old_supply_objective = d
        return d

    def get_religious_objective(self):
        d=''
        if len(self.religious_objective) >0:
            d= self.religious_objective.pop()
        else:
            d= super().get_religious_objective()        
        self.old_religious_objective = d
        return d

    def get_religious_rewards_id(self):
        if len(self.religious_reward_ids)>0:
            return self.religious_reward_ids.pop()
        else:
            return super().get_religious_rewards_id()

    def get_religious_reward(self, id):
        if len(self.religious_rewards)>0:
            return self.religious_rewards.pop()
        else:
            return super().get_religious_reward(id)

    def get_max_religious_rewards_id(self):
        if len(self.religious_reward_max_ids)>0:
            return self.religious_reward_max_ids.pop()
        else:
            return super().get_max_religious_rewards_id()
            
    def get_religious_penalties_id(self):
        if len(self.religious_penalty_ids)>0:
            return self.religious_penalty_ids.pop()
        else:
            return super().get_religious_penalties_id()

    def get_religious_penalty(self, id):
        if len(self.religious_penalties)>0:
            return self.religious_penalties.pop()
        else:
            return super().get_religious_penalty(id)

    def get_max_religious_penalties_id(self):
        if len(self.religious_penalty_max_ids)>0:
            return self.religious_penalty_max_ids.pop()
        else:
            return super().get_max_religious_penalties_id()
            
    def get_supply_rewards_id(self):
        if len(self.supply_reward_ids)>0:
            return self.supply_reward_ids.pop()
        else:
            return super().get_supply_rewards_id()

    def get_supply_reward(self, id):
        if len(self.supply_rewards)>0:
            return self.supply_rewards.pop()
        else:
            return super().get_supply_reward(id)

    def get_max_supply_rewards_id(self):
        if len(self.supply_reward_max_ids)>0:
            return self.supply_reward_max_ids.pop()
        else:
            return super().get_max_supply_rewards_id()
            
    def get_supply_penalties_id(self):
        if len(self.supply_penalty_ids)>0:
            return self.supply_penalty_ids.pop()
        else:
            return super().get_supply_penalties_id()

    def get_supply_penalty(self, id):
        if len(self.supply_penalties)>0:
            return self.supply_penalties.pop()
        else:
            return super().get_supply_penalty(id)

    def get_max_supply_penalties_id(self):
        if len(self.supply_penalty_max_ids)>0:
            return self.supply_penalty_max_ids.pop()
        else:
            return super().get_max_supply_penalties_id()
            
    def get_recon_rewards_id(self):
        if len(self.recon_reward_ids)>0:
            return self.recon_reward_ids.pop()
        else:
            return super().get_recon_rewards_id()

    def get_recon_reward(self, id):
        if len(self.recon_rewards)>0:
            return self.recon_rewards.pop()
        else:
            return super().get_recon_reward(id)

    def get_max_recon_rewards_id(self):
        if len(self.recon_reward_max_ids)>0:
            return self.recon_reward_max_ids.pop()
        else:
            return super().get_max_recon_rewards_id()
            
    def get_recon_penalties_id(self):
        if len(self.recon_penalty_ids)>0:
            return self.recon_penalty_ids.pop()
        else:
            return super().get_recon_penalties_id()

    def get_recon_penalty(self, id):
        if len(self.recon_penalties)>0:
            return self.recon_penalties.pop()
        else:
            return super().get_recon_penalty(id)

    def get_max_recon_penalties_id(self):
        if len(self.recon_penalty_max_ids)>0:
            return self.recon_penalty_max_ids.pop()
        else:
            return super().get_max_recon_penalties_id()
            
    def get_assault_rewards_id(self):
        if len(self.assault_reward_ids)>0:
            return self.assault_reward_ids.pop()
        else:
            return super().get_assault_rewards_id()

    def get_assault_reward(self, id):
        if len(self.assault_rewards)>0:
            return self.assault_rewards.pop()
        else:
            return super().get_assault_reward(id)

    def get_max_assault_rewards_id(self):
        if len(self.assault_reward_max_ids)>0:
            return self.assault_reward_max_ids.pop()
        else:
            return super().get_max_assault_rewards_id()
            
    def get_assault_penalties_id(self):
        if len(self.assault_penalty_ids)>0:
            return self.assault_penalty_ids.pop()
        else:
            return super().get_assault_penalties_id()

    def get_assault_penalty(self, id):
        if len(self.assault_penalties)>0:
            return self.assault_penalties.pop()
        else:
            return super().get_assault_penalty(id)

    def get_max_assault_penalties_id(self):
        if len(self.assault_penalty_max_ids)>0:
            return self.assault_penalty_max_ids.pop()
        else:
            return super().get_max_assault_penalties_id()

    def get_random_mission (self, missions):
        if len(self.random_missions) > 0:
            return missions[self.random_missions.pop(0)]
        else:
            return super().get_random_mission(missions)

    def get_mission_type(self):
        if len(self.mission_types) > 0:
            return self.mission_types.pop(0)
        else:
            return super().get_mission_type()

    def get_simple_mission_type(self):
        if len(self.simple_mission_types) > 0:
            return self.simple_mission_types.pop(0)
        else:
            return super().get_simple_mission_type()

    def get_mission_count(self):
        if len(self.mission_counts) > 0:
            return self.mission_counts.pop(0)
        else:
            return super().get_mission_count()

    def get_favor_type(self):
        if len(self.favor_types) > 0:
            return self.favor_types.pop(0)
        else:
            return super().get_favor_type()

    def get_title(self):
        if len(self.titles)>0:
            return self.titles.pop(0)
        else:
            return super().get_title()

    def get_specialist(self):
        if len(self.specialists) > 0:
            return self.specialists.pop(0)
        else:
            return super().get_specialist()

    def get_assault_target(self):
        if len(self.assault_targets) > 0:
            return self.assault_targets.pop(0)
        else:
            return super().get_assault_target()

    def get_simple_assault_target(self):
        return super().get_simple_assault_target()

    def get_simple_recon_target(self):
        if len(self.simple_recon_targets) > 0:
            return self.simple_recon_targets.pop(0)
        else:
            return super().get_simple_recon_target()

    def get_simple_religious_target(self):
        if len(self.simple_religious_targets) > 0:
            return self.simple_religious_targets.pop(0)
        else:
            return super().get_simple_religious_target() 

    def get_assault_target_types(self):
        if len(self.assault_target_types) > 0:
            return self.assault_target_types.pop(0)
        else:
            return super().get_assault_target_types()

    def get_recon_target(self):
        if len(self.recon_targets) > 0:
            return self.recon_targets.pop(0)
        else:
            return super().get_recon_target()

    def get_recon_target_types(self):
        if len(self.recon_target_types) > 0:
            return self.recon_target_types.pop(0)
        else:
            return super().get_recon_target_types()

    def get_religious_target(self):
        if len(self.religious_targets) > 0:
            return self.religious_targets.pop(0)
        else:
            return super().get_religious_target()

    def get_supply_target(self):
        if len(self.supply_targets) > 0:
            return self.supply_targets.pop(0)
        else:
            return super().get_supply_target()
   
    def get_religious_culture(self):
        if len(self.religious_cultures) > 0:
            return self.religious_cultures.pop(0)
        else:
            return super().get_religious_culture()


