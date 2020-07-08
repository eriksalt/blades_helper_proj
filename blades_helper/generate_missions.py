from blades_helper.mission_generator_constants import MissionGeneratorConstants as con
from blades_helper.mission import Mission
from blades_helper.mission_generator import generate_missions

#Add key enemies to this list and the tool will generate missions for each one
key_enemies = {'Blighter', 'Breaker'}
available_enemy_missions = [con.ASSAULT, con.RECON, con.SUPPLY, con.RELIGIOUS]

commanders_focus= con.ASSAULT
gm_mission_type=con.SUPPLY
gm_assault_target=con.POWERFUL_UNDEAD
gm_recon_target = con.EXFILTRATION
gm_religious_target=con.UNEARTH
chosens_favor=con.MERCY
available_mission_types=[con.ASSAULT, con.RECON, con.SUPPLY, con.RELIGIOUS]
special_mission_acquired_by_spymaster=False
trap_laid_by_spymaster=False
mission_augmented_by_spymaster=False

