import blades_helper as blades
from blades_helper import MissionGeneratorConstants as con
import random

def generate_broken_mission(title, mission_types, broken_themes, assault_targets, recon_targets, religious_targets, gateway):
    mission = blades.Mission()
    blades._initialize_mission(mission, title, random.choice(mission_types), con.NOTHING, con.NOTHING)
    blades._configure_mission_by_type(mission, random.choice(broken_themes), random.choice(assault_targets), random.choice(recon_targets), random.choice(religious_targets), gateway)
    return mission

gateway=blades.DataGateway()

#Add key enemies to this list and the tool will generate missions for each one
available_enemy_missions = [con.ASSAULT, con.RECON, con.SUPPLY, con.RELIGIOUS]
enemy_assault_targets= ['civilians', 'legion', 'broken']
enemy_recon_targets = [ con.AREA_RECON, con.ROUTE_RECON, con.TROOP_RECON, con.INFLITRATION, con.EXFILTRATION]
enemy_religiious_targets = [con.UNEARTH, 'desecrate']

#this is usually the next advance they are working on, but add other themes if you want
blighter_themes = ['gut sack development']#, 'surgery techniques', 'poison gas']
breaker_themes = ['storm riding - jumping bodies']

blighter_mission = generate_broken_mission('Blighter Mission',available_enemy_missions, blighter_themes, enemy_assault_targets, enemy_recon_targets, enemy_religiious_targets, gateway)
breaker_mission = generate_broken_mission('Breaker Mission', available_enemy_missions, breaker_themes, enemy_assault_targets, enemy_recon_targets, enemy_religiious_targets, gateway)

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

missions = blades.generate_missions(commanders_focus, gm_mission_type, gm_assault_target, gm_recon_target, gm_religious_target, chosens_favor, available_mission_types, special_mission_acquired_by_spymaster, trap_laid_by_spymaster, mission_augmented_by_spymaster, gateway)
indents = ['','\t','\t\t', '\t\t\t', '\t\t\t\t' ]
indent_level=0

print(blighter_mission)
print('')
print(breaker_mission)

for mission in missions:
    print('')
    print(mission)




