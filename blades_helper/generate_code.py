from csv import DictReader, reader as csvreader
import jinja2
from io import StringIO

data = {}

with open('blades_helper\military_objectives.csv', 'rt') as input_file:
    reader = DictReader(input_file)
    for row in reader:
        data[row['key']]=row

templateLoader = jinja2.FileSystemLoader(searchpath="./blades_helper/templates")
templateEnv = jinja2.Environment(loader=templateLoader)
MILITARY_OBJECTIVES_TEMPLATE = 'military_objectives.j2'
template = templateEnv.get_template(MILITARY_OBJECTIVES_TEMPLATE)
outputText = template.render(objectives=data, variable_name='military_objectives', keys=data.keys()) 

output_file = StringIO()
output_file.write(r'class MissionGeneratorConstants:')
output_file.write('\r\n')
output_file.write(outputText+'\r\n')

SIMPLE_CONSTANTS_TEMPLATE = 'simple_mission_gen_constants.j2'
gen_template = templateEnv.get_template(SIMPLE_CONSTANTS_TEMPLATE)

with open('blades_helper\simple__mission_gen_constants.csv', 'rt') as input_file:
    reader = DictReader(input_file)
    for vals in reader:        
        output_file.write(gen_template.render(vals))
        output_file.write('\r')

OLD_CONSTANT_ARRAYS_TEMPLATE = 'old_mission__gen_arrays.j2'
gen_template = templateEnv.get_template(OLD_CONSTANT_ARRAYS_TEMPLATE)

with open('blades_helper\old_mission__gen_arrays.csv') as input_file:
    reader = csvreader(input_file, delimiter='\t')
    for row in reader:
        if len(row)>0:
            var_name=row[0]
            var_values = row[1:]
            out = gen_template.render(var_name=var_name, var_values=var_values)
            output_file.write(out)
            output_file.write('\r')

output_file.write(r"    mission_first_names = ['Swift', 'Unceasing', 'Vengeful', 'Lone', 'Cold', 'Hot', 'Purple', 'Brutal', 'Flying', 'Driving', 'Blind', 'Demon', 'Enduring', 'Defiant', 'Lost', 'Dying', 'Falling', 'Soaring', 'Twisted', 'Glass', 'Bleeding', 'Broken', 'Silent', 'Red', 'Black', 'Dark', 'Fallen', 'Patient', 'Burning', 'Final', 'Lazy', 'Morbid', 'Crimson', 'Cursed', 'Frozen', 'Bloody', 'Banished', 'First', 'Severed', 'Empty', 'Spectral', 'Sacred', 'Stone', 'Shattered', 'Hidden', 'Rotting', 'Devils', 'Forgotten', 'Blinding', 'Fading', 'Crystal', 'Secret', 'Cryptic', 'Smoking', 'Heaving', 'Steaming', 'Righteous', 'Purple', 'Amber', 'Wailing', 'Cosmic', 'Foolish', 'Brooding', 'Failing', 'Gasping', 'Starving', 'Sinking', 'Holy', 'Unholy', 'Potent', 'Haunting', 'Pungent', 'Golden', 'Iron', 'Shackled', 'Laughing', 'Damned', 'Poisoned', 'Half-eaten', 'Summoned', 'Gilded', 'Manic', 'Precious', 'Outer', 'Little', 'Choking', 'Half-dead', 'Steely', 'Massive', 'Dismal', 'Rebel', 'Dread', 'Sleeping', 'Magic', 'Dripping', 'Faceless', 'Shambling', 'Furious', 'Dead Mans', 'Perilous', 'Heavy', 'Ancient', 'Jagged', 'Northern', 'Earthly', 'Hellish', 'Hellborn', 'Blessed', 'Buried', 'Senseless', 'Blood-Soaked', 'Sweaty', 'Drunken', 'Azure', 'Amber', 'Broken', 'Chosen', 'Crimson', 'Diamond', 'Emerald', 'Flying', 'Grasping', 'Screaming', 'Shattered', 'Western', 'Desert', 'Forthright', 'Scarlet']"+'\r')
output_file.write(r"    mission_second_names = ['Engine', 'Chant', 'Heart', 'Justice', 'Law', 'Thunder', 'Moon', 'Heat', 'Fear', 'Star', 'Apollo', 'Prophet', 'Hero', 'Hydra', 'Serpent', 'Crown', 'Thorn', 'Empire', 'Summer', 'Druid', 'God', 'Savior', 'Stallion', 'Hawk', 'Vengeance', 'Calm', 'Knife', 'Sword', 'Dream', 'Sleep', 'Stroke', 'Flame', 'Spark', 'Fist', 'Dirge', 'Grave', 'Shroud', 'Breath', 'Smoke', 'Giant', 'Whisper', 'Night', 'Throne', 'Pipe', 'Blade', 'Daze', 'Pyre', 'Tears', 'Mother', 'Crone', 'King', 'Father', 'Priest', 'Dawn', 'Hammer', 'Shield', 'Hymn', 'Vanguard', 'Sentinel', 'Stranger', 'Bell', 'Mist', 'Fog', 'Jester', 'Scepter', 'Ring', 'Skull', 'Paramour', 'Palace', 'Mountain', 'Rain', 'Gaze', 'Future', 'Gift', 'Grin', 'Omen', 'Tome', 'Wail', 'Shriek', 'Glove', 'Gears', 'Slumber', 'Beast', 'Wolf', 'Widow', 'Witch', 'Prince', 'Skies', 'Dance', 'Spear', 'Key', 'Fog', 'Feast', 'Cry', 'Claw', 'Peak', 'Valley', 'Shadow', 'Rhyme', 'Moan', 'Wheel', 'Doom', 'Mask', 'Rose', 'Gods', 'Whale', 'Saga', 'Sky', 'Chalice', 'Agony', 'Misery', 'Tears', 'Rage', 'Anger', 'Laughter', 'Terror', 'Gasp', 'Tongue', 'Cobra', 'Snake', 'Cavern', 'Corpse', 'Prophecy', 'Vagabond', 'Altar', 'Death', 'Reckoning', 'Arrow', 'Citadel', 'Fire', 'Hawk', 'Light', 'Mountain', 'Peak', 'Storm', 'Thorn', 'Tiger', 'Wing', 'Wolf', 'Elephant', 'Feather', 'Guardian', 'Tower', 'Fist']"+'\r')
    

with open(r'blades_helper\mission_generator_constants.py', 'wt') as generated_file:
    generated_file.write(output_file.getvalue())

output_file.close()