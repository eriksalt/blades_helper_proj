import pytest
import test.mock_data_gateway
from blades_helper.mission_generator import _get_next_mission_type, _can_use_mission_type, _generate_base_missions, generate_missions
from blades_helper.mission_generator_constants import MissionGeneratorConstants as con

def setup_single_simple_mission(mock, mission_type, note):
    mock.mission_counts.append((1, note))
    mock.mission_types.append(mission_type)

def check_array(source, target):
    assert len(source) == len(target)
    for source_item, target_item in zip(source, target):
        assert source_item==target_item

def check_note_len(mission, notes_len):
    assert len(mission.notes) == notes_len

def check_for_note(mission, note_to_find):
    for note in mission.notes:
        if note_to_find in note:
            return
    assert False

def test_simple_assault_mission():
    mock = test.mock_data_gateway.MockDataGateway()
    rewards = [(4, con.MORALE)]
    penalties = [(1, con.PRESSURE), (1,con.TIME)]
    target = con.PEOPLE
    target_type = con.ASSAULT_TARGET_IS_CHALLENGE
    setup_single_simple_mission(mock, con.ASSAULT, con.NOTHING)
    mock.assault_targets.append(target)
    mock.assault_rewards.append(rewards)
    mock.assault_penalties.append(penalties)
    mock.assault_target_types.append(target_type)
    missions = generate_missions(con.SUPPLY, con.SUPPLY, con.UNDEAD, None, None, con.HOLY, [con.RECON, con.SUPPLY, con.ASSAULT, con.RELIGIOUS], False, mock)
    assert len(missions)==1
    mission = missions[0]
    assert len(mission.rewards)==1
    assert mission.target == target
    check_array(mission.rewards, rewards)
    check_array(mission.penalties, penalties)
    check_for_note(mission, con.ASSAULT_TARGET_IS_CHALLENGE)

def test_simple_recon_mission():
    mock = test.mock_data_gateway.MockDataGateway()
    rewards = [(2, con.INTEL)],[(2, con.INTEL)]
    penalties = [(1, con.DEATHS)]
    target = con.EXFILTRATION
    target_type = con.RECON_TARGET_IS_OBSERVE
    setup_single_simple_mission(mock, con.RECON, con.NOTHING)
    mock.recon_targets.append(target)
    mock.recon_rewards.append(rewards)
    mock.recon_penalties.append(penalties)
    mock.recon_target_types.append(target_type)
    missions = generate_missions(con.SUPPLY, con.SUPPLY, con.UNDEAD, con.INFLITRATION, None, con.HOLY, [con.RECON, con.SUPPLY, con.ASSAULT, con.RELIGIOUS], False, mock)
    assert len(missions)==1
    mission = missions[0]
    assert mission.target == target
    check_array(mission.rewards, rewards)
    check_array(mission.penalties, penalties)
    check_for_note(mission, con.RECON_TARGET_IS_OBSERVE)    

def test_simple_religious_mission():
    mock = test.mock_data_gateway.MockDataGateway()
    rewards = [(-1, con.TIME), (2, con.XP)]
    penalties = [(1,con.PRESSURE)]
    target = con.CLEANSING
    target_type = con.CLEANSING
    setup_single_simple_mission(mock, con.RELIGIOUS, con.NOTHING)
    mock.religious_targets.append(target)
    mock.religious_rewards.append(rewards)
    mock.religious_penalties.append(penalties)
    mock.religious_cultures.append(con.RELIGIOUS_TARGET_OLD_EMPIRE)
    missions = generate_missions(con.SUPPLY, con.SUPPLY, con.UNDEAD, con.INFLITRATION, con.UNEARTH, con.HOLY, [con.RECON, con.SUPPLY, con.ASSAULT, con.RELIGIOUS], False, mock)
    assert len(missions)==1
    mission = missions[0]
    assert mission.target == target
    check_array(mission.rewards, rewards)
    check_array(mission.penalties, penalties)
    check_for_note(mission, con.RELIGIOUS_TARGET_OLD_EMPIRE)  

def test_simple_supply_mission():
    mock = test.mock_data_gateway.MockDataGateway()
    rewards = [(1, con.ASSET), (1, con.SUPPLY)]
    penalties = [(-1, con.MORALE), (-1, con.SUPPLY)]
    target = con.SCROUNGE_OR_TRADE
    setup_single_simple_mission(mock, con.SUPPLY, con.NOTHING)
    mock.supply_targets.append(target)
    mock.supply_rewards.append(rewards)
    mock.supply_penalties.append(penalties)
    missions = generate_missions(con.SUPPLY, con.SUPPLY, con.UNDEAD, con.INFLITRATION, con.UNEARTH, con.HOLY, [con.RECON, con.SUPPLY, con.ASSAULT, con.RELIGIOUS], False, mock)
    assert len(missions)==1
    mission = missions[0]
    assert mission.target == target
    check_array(mission.rewards, rewards)
    check_array(mission.penalties, penalties)

def test_pick_one_plus_danger_for_recon():
    mock = test.mock_data_gateway.MockDataGateway()
    rewards = [(2, con.INTEL)]
    penalties = [(1, con.DEATHS)]
    target = con.PICK_ONE_PLUS_DANGER
    target_type = con.RECON_TARGET_IS_CONSULT
    setup_single_simple_mission(mock, con.RECON, con.NOTHING)
    mock.recon_targets.append(target)
    mock.recon_rewards.append(rewards)
    mock.recon_penalties.append(penalties)
    mock.recon_target_types.append(target_type)
    missions = generate_missions(con.SUPPLY, con.SUPPLY, con.UNDEAD, con.INFLITRATION, None, con.HOLY, [con.RECON, con.SUPPLY, con.ASSAULT, con.RELIGIOUS], False, mock)
    assert len(missions)==1
    mission = missions[0]
    assert mission.target == con.INFLITRATION
    check_array(mission.rewards, rewards)
    check_array(mission.penalties, penalties)
    check_for_note(mission, con.RECON_TARGET_IS_CONSULT)   
    check_for_note(mission, con.HAS_DANGER_NOTE)

def test_pick_one_plus_favor_for_religious():
    mock = test.mock_data_gateway.MockDataGateway()
    rewards = [(-1, con.TIME), (2, con.XP)]
    penalties = [(1,con.PRESSURE)]
    target = con.PICK_ONE_WITH_FAVOR
    target_type = con.CLEANSING
    setup_single_simple_mission(mock, con.RELIGIOUS, con.NOTHING)
    mock.religious_targets.append(target)
    mock.religious_rewards.append(rewards)
    mock.religious_penalties.append(penalties)
    mock.religious_cultures.append(con.RELIGIOUS_TARGET_ALDERMARK)
    missions = generate_missions(con.SUPPLY, con.SUPPLY, con.UNDEAD, con.INFLITRATION, con.UNEARTH, con.HOLY, [con.RECON, con.SUPPLY, con.ASSAULT, con.RELIGIOUS], False, mock)
    assert len(missions)==1
    mission = missions[0]
    assert mission.target == con.UNEARTH
    check_array(mission.rewards, rewards)
    check_array(mission.penalties, penalties)
    check_for_note(mission, con.HOLY)  
    check_for_note(mission, 'Mission has favor of type')  
    check_for_note(mission, con.RELIGIOUS_TARGET_ALDERMARK)  
    
def test_printing():
    mock = test.mock_data_gateway.MockDataGateway()
    rewards = [(2, con.INTEL),(2, con.INTEL)]
    penalties = [(1, con.DEATHS)]
    target = con.PICK_ONE_PLUS_DANGER
    target_type = con.RECON_TARGET_IS_CONSULT
    setup_single_simple_mission(mock, con.RECON, con.NOTHING)
    mock.recon_targets.append(target)
    mock.recon_rewards.append(rewards)
    mock.recon_penalties.append(penalties)
    mock.recon_target_types.append(target_type)
    missions = generate_missions(con.SUPPLY, con.SUPPLY, con.UNDEAD, con.INFLITRATION, None, con.HOLY, [con.RECON, con.SUPPLY, con.ASSAULT, con.RELIGIOUS], False, mock)
    print(missions[0])