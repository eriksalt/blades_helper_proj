import pytest
from blades_helper.mission_generator_constants import MissionGeneratorConstants as con

def check_array(items):
    assert len(items) ==6
    for item in items:
        assert isinstance(item, list)

def test_rewards():
    check_array(con.assault_rewards)
    check_array(con.recon_rewards)
    check_array(con.religious_rewards)
    check_array(con.supply_rewards)
    
def test_penalties():
    check_array(con.assault_penalties)
    check_array(con.recon_penalties)
    check_array(con.religious_penalties)
    check_array(con.supply_penalties)