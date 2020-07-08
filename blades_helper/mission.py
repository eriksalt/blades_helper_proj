from .mission_generator_constants import MissionGeneratorConstants as con

class Mission:
    def __init__(self):
        self_mission_type=con.NOTHING
        self.target=con.NOTHING
        self.title=con.NOTHING
        self.rewards=[]
        self.penalties=[]
        self.notes=[]
        self.requirements=[]

    def set_mission_type(self, mission_type):
        self.mission_type=mission_type

    def get_mission_type(self):
        return self.mission_type

    def set_mission_title(self, title):
        self.title=title

    def set_favor_type(self, favor_type):
        the_note = con.FAVOR_NOTE.format(favor_type)
        self.add_note(the_note)
    
    def set_danger(self):
        self.add_note(con.HAS_DANGER_NOTE)
    
    def set_additional_specialist(self, specialist):
        self.add_note(con.ADDITIONAL_SPECIALIST_NOTE)
        self.add_requirement(specialist)

    def add_requirement(self, specialist):
        self.requirements.append(specialist)
    
    def set_target(self, target):
        self.target=target

    def set_rewards(self, rewards):
        self.rewards=rewards
    
    def set_penalties(self, penalties):
        self.penalties=penalties

    def add_objective(self, objective):
        self.notes.append(f'Military Objective: {objective["key"]}. {objective["description"]} Examples: {objective["example"]}')

    def add_note(self, note):
        self.notes.append(note)
    
    def __repr__(self):
        strings= []
        strings.append(f'Mission: {self.title}.')
        strings.append(f'\tType:{self.mission_type}.')
        strings.append(f'\tTarget: {self.target}.')
        strings.append('\tRewards:')
        for reward_count, reward_type in self.rewards:
            strings.append(f'\t\t Type: {reward_type}. Count: {reward_count}.')
        strings.append('\tPenalties:')
        for penalty_count, penalty_type in self.penalties:
            strings.append(f'\t\t Type: {penalty_type}. Count: {penalty_count}.')
        strings.append('\tRequirements:')
        for requirement in self.requirements:
            strings.append(f'\t\t {requirement}.')  
        if len(self.notes) > 0:
            strings.append('\tNotes:')
            for note in self.notes:
                strings.append(f'\t\t{note}.') 
        return '\r'.join(strings)