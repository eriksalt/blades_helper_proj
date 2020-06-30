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
        self.assault_rewards = []
        self.assault_penalties = []
        self.assault_target_types =[]
        #Recon data tables
        self.recon_targets = []
        self.recon_rewards = []
        self.recon_penalties = []
        self.recon_target_types= []
        #Religious data tables
        self.religious_targets = []
        self.religious_rewards = []
        self.religious_penalties = []
        self.religious_cultures = []
        #Supply data tables
        self.supply_targets = []
        self.supply_rewards = []
        self.supply_penalties = []
        self.simple_mission_types=[]
        self.simple_recon_targets=[]
        self.simple_religious_targets=[]
        self.random_missions=[]
        self.titles=[]
    
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

    def get_assault_rewards(self, is_augmented):
        if len(self.assault_rewards) > 0:
            return self.assault_rewards.pop(0)
        else:
            return super().get_assault_rewards(is_augmented)


    def get_assault_penalties(self, is_augmented):
        if len(self.assault_penalties) > 0:
            return self.assault_penalties.pop(0)
        else:
            return super().get_assault_penalties(is_augmented)


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


    def get_recon_rewards(self, is_augmented):
        if len(self.recon_rewards) > 0:
            return self.recon_rewards.pop(0)
        else:
            return super().get_recon_rewards(is_augmented)


    def get_recon_penalties(self, is_augmented):
        if len(self.recon_penalties) > 0:
            return self.recon_penalties.pop(0)
        else:
            return super().get_recon_penalties(is_augmented)


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

    def get_religious_rewards(self, is_augmented):
        if len(self.religious_rewards) > 0:
            return self.religious_rewards.pop(0)
        else:
            return super().get_religious_rewards(is_augmented)


    def get_religious_penalties(self, is_augmented):
        if len(self.religious_penalties) > 0:
            return self.religious_penalties.pop(0)
        else:
            return super().get_religious_penalties(is_augmented)


    def get_supply_target(self):
        if len(self.supply_targets) > 0:
            return self.supply_targets.pop(0)
        else:
            return super().get_supply_target()


    def get_supply_rewards(self, is_augmented):
        if len(self.supply_rewards) > 0:
            return self.supply_rewards.pop(0)
        else:
            return super().get_supply_rewards(is_augmented)


    def get_supply_penalties(self, is_augmented):
        if len(self.supply_penalties) > 0:
            return self.supply_penalties.pop(0)
        else:
            return super().get_supply_penalties(is_augmented)

    
    def get_religious_culture(self):
        if len(self.religious_cultures) > 0:
            return self.religious_cultures.pop(0)
        else:
            return super().get_religious_culture()


