import pytest
import test.mock_data_gateway
from blades_helper.mission_generator import _get_next_mission_type, _can_use_mission_type, _generate_base_missions
from blades_helper.mission_generator_constants import MissionGeneratorConstants as con

def setup_one_mission_base_build(mock, note, type):
    mock.mission_counts.append((1, note))
    mock.mission_types.append(type)

def check_array(source, target):
    assert len(source)==len(target)
    for i in range(len(source)):
        assert source[i]==target[i]

def check_mission_type(mission, mission_type):
    assert mission.mission_type == mission_type

def check_note_len(mission, notes_len):
    assert len(mission.notes) == notes_len

def check_for_note(mission, note_to_find):
    for note in mission.notes:
        if note_to_find in note:
            return
    assert False

def check_requirement(mission, specialist):
    return specialist in mission.requirements

def check_for_note_plus_one_specialist(mission, specialist):
    check_for_note(mission, "Mission can include one additional specialist")
    check_requirement(mission, specialist)

def check_for_note_favor(mission, favor_type):
    check_for_note(mission, con.FAVOR_NOTE[0:-3])
    check_for_note(mission, favor_type)

def check_mission(mission, mission_type, target, rewards, penalties, notes_len, requirement, contained_notes):
    check_mission_type(mission, mission_type)
    assert mission.target == target
    check_array(mission.rewards, rewards)
    check_array(mission.penalties, penalties)
    check_note_len(mission, notes_len)
    if not requirement == con.NOTHING:
        check_requirement(mission, requirement)
    for contained_note in contained_notes:
        check_for_note(mission, contained_note)
 
def test_get_next_mission_type():
    assert _get_next_mission_type(con.ASSAULT) == con.RECON
    assert _get_next_mission_type(con.RECON) == con.RELIGIOUS
    assert _get_next_mission_type(con.RELIGIOUS)==con.SUPPLY
    assert _get_next_mission_type(con.SUPPLY)  == con.COMMANDER_FOCUS
    with pytest.raises(AssertionError):
        _get_next_mission_type(con.COMMANDER_FOCUS)
    with pytest.raises(AssertionError):
        _get_next_mission_type(con.GM_CHOICE)

def test_can_use_mission_type():
    assert not _can_use_mission_type(con.SUPPLY, [con.ASSAULT])
    assert _can_use_mission_type(con.SPECIAL, [con.SPECIAL])
    assert _can_use_mission_type(con.GM_CHOICE, [con.GM_CHOICE])
    assert not _can_use_mission_type(con.SUPPLY, [])
    assert _can_use_mission_type(con.SUPPLY, [con.SUPPLY])
    assert _can_use_mission_type(con.SUPPLY, [con.ASSAULT, con.SUPPLY])
    assert _can_use_mission_type(con.SUPPLY, [con.SUPPLY, con.ASSAULT])



def test_make_one_mission():
    mock = test.mock_data_gateway.MockDataGateway()
    mock.titles.append('bunker hill')
    setup_one_mission_base_build(mock, con.NOTHING, con.RELIGIOUS)
    missions =_generate_base_missions(mock, False, False, False,  con.SUPPLY, con.ASSAULT, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT, con.RECON] )
    assert len(missions)==1
    mission = missions[0]
    check_mission(mission, con.RELIGIOUS, con.NOTHING, [], [], 0, con.required_religious_specialists, [])

def test_one_has_favor():
    mock = test.mock_data_gateway.MockDataGateway()
    mock.favor_types.append(con.THE_WILD)
    setup_one_mission_base_build(mock, con.ONE_HAS_FAVOR, con.SUPPLY)
    missions =_generate_base_missions( mock, False, False, False,  con.ASSAULT, con.ASSAULT, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT, con.RECON] )
    assert len(missions)==1
    mission = missions[0]
    check_mission(mission,con.SUPPLY,con.NOTHING,[],[],1,con.required_supply_specialists,[con.FAVOR_NOTE[0:-3], con.THE_WILD])

def test_one_extra_specialist():
    mock = test.mock_data_gateway.MockDataGateway()
    mock.specialists.append(con.SNIPER)
    setup_one_mission_base_build(mock, con.PLUS_ONE_SPECIALIST, con.SUPPLY)
    missions =_generate_base_missions( mock, False, False, False,  con.ASSAULT, con.ASSAULT, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT, con.RECON] )
    mission = missions[0]
    check_mission(mission, con.SUPPLY, con.NOTHING, [],[], 1, con.required_supply_specialists, ["Mission can include one additional specialist"])
    check_for_note_plus_one_specialist(mission, con.SNIPER)


def test_commanders_focus():
    mock = test.mock_data_gateway.MockDataGateway()    
    setup_one_mission_base_build(mock, con.NOTHING, con.COMMANDER_FOCUS)
    missions =_generate_base_missions( mock, False, False, False,  con.RECON, con.ASSAULT, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT, con.RECON] )
    mission = missions[0]
    check_mission(mission, con.RECON, con.NOTHING, [],[], 0,con.required_recon_specialists,[])
    

def test_gm_choice():
    mock = test.mock_data_gateway.MockDataGateway()    
    setup_one_mission_base_build(mock, con.NOTHING, con.GM_CHOICE)
    missions =_generate_base_missions( mock, False, False, False,  con.ASSAULT, con.RECON, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT, con.RECON] )
    mission = missions[0]
    check_mission(mission, con.RECON, con.NOTHING, [],[], 0,con.required_recon_specialists,[])



def test_unavailable_mission():
    #test simple unavailability
    mock = test.mock_data_gateway.MockDataGateway()    
    setup_one_mission_base_build(mock, con.NOTHING, con.RECON)
    missions =_generate_base_missions( mock, False, False, False,  con.ASSAULT, con.RECON, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT] )
    mission = missions[0]
    check_mission(mission, con.RELIGIOUS, con.NOTHING, [],[], 0,con.required_religious_specialists,[])
    #test when mutiple missions unavailable
    setup_one_mission_base_build(mock, con.NOTHING, con.ASSAULT)
    missions =_generate_base_missions( mock, False, False, False,  con.UNDEFINED, con.ASSAULT, [] )
    mission = missions[0]
    check_mission(mission, con.UNDEFINED, con.NOTHING, [],[], 0,con.NOTHING,[])

def test_special_missions_are_allowed():
    # special
    mock = test.mock_data_gateway.MockDataGateway()    
    setup_one_mission_base_build(mock, con.NOTHING, con.SPECIAL)
    missions =_generate_base_missions( mock, False, False, False, con.ASSAULT, con.ASSAULT, [] )
    mission = missions[0]
    check_mission(mission, con.SPECIAL, con.NOTHING, [],[], 0,con.NOTHING,[])


def create_mission_with_gm_choice_and_note(mock, choice, note, spymaster_buy=False):
    setup_one_mission_base_build(mock, note, con.GM_CHOICE)
    missions =_generate_base_missions( mock, spymaster_buy,  False, False,  con.ASSAULT, choice, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT] )
    assert len(missions) == 1
    return missions[0]

def create_mission_with_commander_focus_and_note(mock, focus,note, spymaster_buy=False):
    setup_one_mission_base_build(mock, note, con.COMMANDER_FOCUS)
    missions =_generate_base_missions( mock, spymaster_buy,  False, False,  focus, con.ASSAULT, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT] )
    assert len(missions) == 1
    return missions[0]

def test_commander_focus_plus_one_specialist():
    mock = test.mock_data_gateway.MockDataGateway()    
    mock.specialists.append(con.HEAVY)
    focus=con.SUPPLY
    note=con.PLUS_ONE_SPECIALIST
    mission=create_mission_with_commander_focus_and_note(mock, focus, note)
    check_mission_type(mission, focus)
    check_note_len(mission, 1)
    check_for_note_plus_one_specialist(mission, con.HEAVY)
    
def test_commander_focus_one_has_favor():
    mock = test.mock_data_gateway.MockDataGateway()    
    mock.favor_types.append(con.HOLY)
    focus=con.SUPPLY
    note=con.ONE_HAS_FAVOR
    mission=create_mission_with_commander_focus_and_note(mock, focus, note)
    check_mission_type(mission, focus)
    check_note_len(mission, 1)
    check_for_note_favor(mission, con.HOLY)

def test_commander_focus_one_is_special():
    mock = test.mock_data_gateway.MockDataGateway()    
    focus=con.SUPPLY
    note=con.ONE_IS_SPECIAL
    mission=create_mission_with_commander_focus_and_note(mock, focus, note)
    check_mission_type(mission, con.SPECIAL)
    check_note_len(mission, 0)

def test_gm_choice_plus_one_specialist():
    mock = test.mock_data_gateway.MockDataGateway()    
    mock.specialists.append(con.HEAVY)
    choice=con.SUPPLY
    note=con.PLUS_ONE_SPECIALIST
    mission=create_mission_with_gm_choice_and_note(mock, choice, note)
    check_mission_type(mission, choice)
    check_note_len(mission, 1)
    check_for_note_plus_one_specialist(mission, con.HEAVY)

def test_gm_choice_one_has_favor():
    mock = test.mock_data_gateway.MockDataGateway()
    mock.favor_types.append(con.HOLY)
    choice=con.SUPPLY
    note=con.ONE_HAS_FAVOR
    mission=create_mission_with_gm_choice_and_note(mock, choice, note)
    check_mission_type(mission, choice)
    check_note_len(mission, 1)
    check_for_note_favor(mission, con.HOLY)
    

def test_gm_choice_one_is_special():
    mock = test.mock_data_gateway.MockDataGateway()
    choice=con.SUPPLY
    note=con.ONE_IS_SPECIAL
    mission=create_mission_with_gm_choice_and_note(mock, choice, note)
    check_mission_type(mission, con.SPECIAL)
    check_note_len(mission, 0)

def test_simple_spymaster_spend():
    mock=test.mock_data_gateway.MockDataGateway()
    setup_one_mission_base_build(mock, con.NOTHING, con.SUPPLY)
    missions =_generate_base_missions( mock, True, False, False,  con.ASSAULT,con.ASSAULT, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT] )
    assert len(missions) == 1
    check_mission_type(missions[0], con.SPECIAL)
    
def test_one_mission_with_spymaster_and_one_is_special():
    mock=test.mock_data_gateway.MockDataGateway()
    setup_one_mission_base_build(mock, con.ONE_IS_SPECIAL, con.SUPPLY)
    missions =_generate_base_missions( mock, True, False, False,  con.ASSAULT,con.ASSAULT, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT] )
    assert len(missions) == 1
    check_mission_type(missions[0], con.SPECIAL)
    check_note_len(missions[0],0)

def test_two_missions_with_spymaster_and_one_is_special():
    mock=test.mock_data_gateway.MockDataGateway()
    mock.mission_counts.append((2, con.ONE_IS_SPECIAL))
    mock.mission_types.append(con.RECON)
    mock.mission_types.append(con.SUPPLY)
    missions =_generate_base_missions( mock, True, False, False,  con.ASSAULT,con.ASSAULT, [con.RELIGIOUS, con.SUPPLY, con.ASSAULT] )
    assert len(missions) == 2
    check_mission_type(missions[0], con.SPECIAL)
    check_note_len(missions[0],0)
    check_mission_type(missions[1], con.SPECIAL)
    check_note_len(missions[1],0)

def setup_three_missions(mock, note, first_type, second_type, third_type, commanders_focus, gms_choice, spymaster_buy=False):
    mock.mission_counts.append((3, note))
    mock.mission_types.append(first_type)
    mock.mission_types.append(second_type)
    mock.mission_types.append(third_type)
    missions = _generate_base_missions(mock, spymaster_buy,  False, False,  commanders_focus, gms_choice, [con.ASSAULT, con.RECON, con.SUPPLY, con.RELIGIOUS])
    assert len(missions)==3
    return missions
    
def test_three_simple_missions():
    mock=test.mock_data_gateway.MockDataGateway()
    note=con.NOTHING
    first_type=con.RELIGIOUS
    second_type=con.SUPPLY
    third_type=con.RECON
    spymaster_buy=False
    commander_focus=con.ASSAULT
    gm_choice=con.ASSAULT
    missions=setup_three_missions(mock, note, first_type, second_type, third_type, commander_focus, gm_choice, spymaster_buy)
    check_mission_type(missions[0], con.RELIGIOUS)
    check_mission_type(missions[1], con.SUPPLY)
    check_mission_type(missions[2], con.RECON)

def test_three_missions_with_one_is_special():
    mock=test.mock_data_gateway.MockDataGateway()
    mock.random_missions.append(1)
    mock.specialists.append(con.HEAVY)
    note=con.PLUS_ONE_SPECIALIST
    first_type=con.RELIGIOUS
    second_type=con.SUPPLY
    third_type=con.RECON
    spymaster_buy=False
    commander_focus=con.ASSAULT
    gm_choice=con.ASSAULT
    missions=setup_three_missions(mock, note, first_type, second_type, third_type, commander_focus, gm_choice, spymaster_buy)
    check_mission_type(missions[0], con.RELIGIOUS)
    check_mission_type(missions[1], con.SUPPLY)
    check_mission_type(missions[2], con.RECON)
    check_for_note_plus_one_specialist(missions[1],con.HEAVY)

def test_three_missions_with_spymaster_buy_and_one_is_special():
    mock=test.mock_data_gateway.MockDataGateway()
    note=con.ONE_IS_SPECIAL
    first_type=con.RELIGIOUS
    second_type=con.SUPPLY
    third_type=con.RECON
    spymaster_buy=True
    commander_focus=con.ASSAULT
    gm_choice=con.ASSAULT
    missions=setup_three_missions(mock, note, first_type, second_type, third_type, commander_focus, gm_choice, spymaster_buy)
    check_mission_type(missions[0], con.SPECIAL)
    check_mission_type(missions[1], con.SPECIAL)
    check_mission_type(missions[2], con.RELIGIOUS)


