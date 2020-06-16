from blades_helper.mission_generator_constants import MissionGeneratorConstants as con
from blades_helper.mission import Mission
from blades_helper.data_gateway import DataGateway
import random

def _can_use_mission_type(mission_type, available_mission_types):
    return mission_type in [con.SPECIAL,con.COMMANDER_FOCUS, con.GM_CHOICE] or mission_type in available_mission_types

def _get_next_mission_type(the_mission_type):
    assert the_mission_type not in [con.COMMANDER_FOCUS, con.GM_CHOICE]
    return con.mission_types[con.mission_types.index(the_mission_type)+1]

def _generate_base_missions(gateway, are_special_mission_acquired_by_spymaster, commanders_focus, gm_mission_type, available_mission_types):
    special_mission_count=0
    if are_special_mission_acquired_by_spymaster:
        special_mission_count = special_mission_count+1
    count, note = gateway.get_mission_count()
    if(note == con.ONE_IS_SPECIAL):
        special_mission_count = special_mission_count + 1
    the_missions=[]
    for i in range(count):
        the_mission = Mission()
        the_mission.set_mission_title(gateway.get_title())
        if special_mission_count > 0:
            the_mission.set_mission_type(con.SPECIAL)
            special_mission_count=special_mission_count-1
        else:
            the_mission_type = gateway.get_mission_type()
            while not _can_use_mission_type(the_mission_type, available_mission_types):
                the_mission_type = _get_next_mission_type(the_mission_type)

            if the_mission_type == con.COMMANDER_FOCUS:
                the_mission.set_mission_type(commanders_focus)
            elif the_mission_type == con.GM_CHOICE:
                the_mission.set_mission_type(gm_mission_type)
            else:
                the_mission.set_mission_type(the_mission_type)
        the_missions.append(the_mission)
    nonspecialist_missions= [mission for mission in the_missions if mission.get_mission_type() != con.SPECIAL].copy()
    if len(nonspecialist_missions)>0:
        if note == con.ONE_HAS_FAVOR:
            gateway.get_random_mission(nonspecialist_missions).set_favor_type(gateway.get_favor_type())
        elif note == con.PLUS_ONE_SPECIALIST:
            gateway.get_random_mission(nonspecialist_missions).set_additional_specialist(gateway.get_specialist())
    return the_missions

def _set_target(mission, selected_target, gm_choice, chosens_favor):
    the_target =selected_target
    if the_target == con.PICK_ONE_PLUS_DANGER:
        the_target= gm_choice
        mission.set_danger()
    if the_target ==con.PICK_ONE_WITH_FAVOR:
        the_target = gm_choice
        mission.set_favor_type(chosens_favor)
    mission.set_target(the_target)
    return

def _setup_assault_mission(the_mission, gateway, chosens_favor, gm_assault_target):
    target=gateway.get_assault_target()
    _set_target(the_mission, target, gm_assault_target, chosens_favor)
    the_mission.set_rewards(gateway.get_assault_rewards())
    the_mission.set_penalties(gateway.get_assault_penalties())
    the_mission.add_note(gateway.get_assault_target_types())

def _setup_recon_mission(the_mission, gateway, chosens_favor, gm_recon_target):
    target = gateway.get_recon_target()
    _set_target(the_mission, target, gm_recon_target, chosens_favor)
    the_mission.set_rewards(gateway.get_recon_rewards())
    the_mission.set_penalties(gateway.get_recon_penalties())
    the_mission.add_note(gateway.get_recon_target_types())

def _setup_religious_mission(the_mission, gateway, chosens_favor, gm_religious_target):
    target = gateway.get_religious_target()
    _set_target(the_mission, target, gm_religious_target, chosens_favor)
    the_mission.set_rewards(gateway.get_religious_rewards())
    the_mission.set_penalties(gateway.get_religious_penalties())
    the_mission.add_note(con.CULTURE_USE_NOTE.format(gateway.get_religious_culture()))

def _setup_supply_mission(the_mission, gateway, chosens_favor):
    target = gateway.get_supply_target()
    _set_target(the_mission, target, con.NOTHING, chosens_favor)
    the_mission.set_rewards(gateway.get_supply_rewards())
    the_mission.set_penalties(gateway.get_supply_penalties())

#def _setup_none_value(input, random_values):
#    if input == None or input == con.NOTHING:
#        return random.choice(random_values)

def generate_missions(commanders_focus, gm_mission_type, gm_assault_target, gm_recon_target, gm_religious_target, chosens_favor, available_mission_types, special_mission_acquired_by_spymaster, gateway=None):
    if gateway == None or gateway == con.NOTHING:
        gateway = DataGateway()
    if gm_mission_type == con.NOTHING or gm_mission_type==None:
        gm_mission_type = gateway.get_simple_mission()
    if gm_assault_target == con.NOTHING or gm_assault_target==None:
        gm_assault_target = gateway.get_simple_assault_target()
    if gm_recon_target == con.NOTHING or gm_recon_target==None:
        gm_recon_target = gateway.get_simple_recon_target()
    if gm_religious_target == con.NOTHING or gm_religious_target==None:
        gm_religious_target = gateway.get_simple_religious_target()
    
    missions = _generate_base_missions(gateway, special_mission_acquired_by_spymaster, commanders_focus, gm_mission_type, available_mission_types)
    for mission in missions:
        if mission.get_mission_type() == con.ASSAULT:
            _setup_assault_mission(mission, gateway, chosens_favor, gm_assault_target)
        elif mission.get_mission_type() == con.RECON:
            _setup_recon_mission(mission, gateway, chosens_favor, gm_recon_target)
        elif mission.get_mission_type() == con.RELIGIOUS:
            _setup_religious_mission(mission, gateway, chosens_favor, gm_religious_target)
        elif mission.get_mission_type() == con.SUPPLY:
            _setup_supply_mission(mission, gateway, chosens_favor)
    return missions 