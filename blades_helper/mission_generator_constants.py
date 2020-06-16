class MissionGeneratorConstants:
    SPECIAL='Special'
    UNDEFINED='UNDEFINED'
    PRESSURE = 'Pressure'
    MORALE='Morale'
    INTEL = 'Intel'
    TIME = 'Time'
    ASSAULT = 'Assault'
    RECON = 'Recon'
    RELIGIOUS = 'Religious'
    SUPPLY = "Supply"
    ASSET_OR_TROOPS = 'Asset or Troops'
    ASSET = 'Asset'
    COMMANDER_FOCUS = 'Commander Focus'
    GM_CHOICE = 'GMs choice'
    PEOPLE = 'People'
    THE_WILD = 'The Wild'
    UNDEAD = 'Undead'
    POWERFUL_UNDEAD = 'Powerful Undead'
    AREA_RECON = 'Area Recon'
    ROUTE_RECON = 'Route Recon'
    TROOP_RECON = 'Troop Recon'
    INFLITRATION = 'Infiltration'
    EXFILTRATION = 'Exfiltration'
    PICK_ONE_PLUS_DANGER = 'Pick one plus danger'
    NOTHING = ''
    ONE_HAS_FAVOR = 'one has favor'
    PLUS_ONE_SPECIALIST = 'one has +1 specialist'
    ONE_IS_SPECIAL = 'one special mission'
    HOLY='Holy'
    MYSTIC='Mystic'
    GLORY='Glory'
    KNOWLEDGE='Knowledge' 
    MERCY='Mercy'
    WILD='Wild'
    HEAVY='Heavy'
    MEDIC='Medic'
    SCOUT='Scout'
    SNIPER='Sniper'
    OFFICER='Officer'
    ALCHEMIST_OR_MERCY='Alchemist or Mercy'
    DEATHS = 'Death(s)'
    NONE='None'
    ESCORT='Escort'
    CLEANSING='Cleansing'
    DEFENSE='Defense'
    UNEARTH='Unearth'
    PICK_ONE_WITH_FAVOR='Pick one with Favor'
    XP = 'xp'
    SCORE_POINTS='Score points'
    FINE_ASSET='Fine Asset'
    EXCEPTIONAL_ASSET='Exceptional Asset'
    SPECIALIST='Specialist'
    SCROUNGE_OR_TRADE = 'Scrounge or Trade'
    RESCUE_SUPPLIES = 'Rescue Supplies'
    MERCENARY_WORK = 'Mercenary Work'
    ASSET_OR_TROOPS = 'Asset or Troops'

    ASSAULT_TARGET_IS_CHALLENGE='Your target may be a challenge that needs to be overcome'
    ASSAULT_TARGET_IS_OBJECTIVE='Your target may be an objective which you need to engage in conflict to achieve'

    RECON_TARGET_IS_OBSERVE='It may be that your information can be gained by observing something or someone'
    RECON_TARGET_IS_STEAL='It may be that your information can be gained by stealing something or someone'
    RECON_TARGET_IS_CONSULT='It may be that your information can be gained by consulting local sources with vital intelligence'

    RELIGIOUS_TARGET_ALDERMARK='Aldermark'
    RELIGIOUS_TARGET_BARTA='Barta'
    RELIGIOUS_TARGET_OR='Or'
    RELIGIOUS_TARGET_DAR='Dar'
    RELIGIOUS_TARGET_OLD_EMPIRE='the Old Empire'
    RELIGIOUS_TARGET_PANYA='Panya'
    RELIGIOUS_TARGET_ZEMYA='Zemya'
    RELIGIOUS_TARGET_ROYIN='Royin'
    RELIGIOUS_TARGET_BONE_WASTES='the Bone Wastes'
    RELIGIOUS_TARGET_ANDRASTUS='the Principalities of Andrastus'

    #Output text
    FAVOR_NOTE = "Mission has favor of type {}"
    HAS_DANGER_NOTE = "Mission is especially dangerous.  Consider adding a lieutenant or elite"
    ADDITIONAL_SPECIALIST_NOTE = "Mission requires a {} in addition to any other requirements. Mission can include one additional specialist"
    CULTURE_USE_NOTE='Consider setting in the context of {}'

    #Generral Data Tables
    mission_types = [
        ASSAULT, 
        RECON,
        RELIGIOUS,
        SUPPLY,
        COMMANDER_FOCUS,
        GM_CHOICE
        ]

    mission_counts = [
        (3,NOTHING),
        (3,NOTHING), 
        (3,PLUS_ONE_SPECIALIST),
        (2,NOTHING), 
        (3,ONE_HAS_FAVOR), 
        (3, ONE_IS_SPECIAL)
    ]

    favor_types = [
        HOLY,
        MYSTIC, 
        GLORY, 
        KNOWLEDGE, 
        MERCY, 
        WILD
        ]

    specialists = [
        HEAVY, 
        MEDIC, 
        SCOUT, 
        SNIPER, 
        OFFICER, 
        ALCHEMIST_OR_MERCY
        ]

    #Assault data tables
    assault_targets = [
        PEOPLE, 
        THE_WILD, 
        UNDEAD, 
        UNDEAD, 
        POWERFUL_UNDEAD, 
        POWERFUL_UNDEAD
        ]

    assault_rewards = [ 
        [(2,MORALE)], 
        [(3, MORALE)], 
        [(4, MORALE)], 
        [(2, MORALE), (1,SUPPLY)], 
        [(2,MORALE), (1,INTEL)], 
        [(2,MORALE), (-1,TIME)]
        ]

    assault_penalties = [
        [(1, PRESSURE), (1,TIME)], 
        [(1, TIME)], 
        [(-1, SUPPLY)], 
        [(1, PRESSURE)], 
        [(1, PRESSURE)],
        [(1,PRESSURE)]
        ]

    assault_target_types =[
        ASSAULT_TARGET_IS_CHALLENGE, 
        ASSAULT_TARGET_IS_OBJECTIVE
        ]

    #Recon data tables
    recon_targets = [
        AREA_RECON, 
        ROUTE_RECON, 
        TROOP_RECON, 
        INFLITRATION, 
        EXFILTRATION, 
        PICK_ONE_PLUS_DANGER
        ]

    recon_rewards = [
        [(2, INTEL)],
        [(2,INTEL)], 
        [(1,ASSET), (1, INTEL)], 
        [(1, ASSET_OR_TROOPS), (1,INTEL)],
        [(1, INTEL), (-1,TIME)],
        [(3,INTEL)]
        ]

    recon_penalties = [
        [(1, TIME) ], 
        [(2, DEATHS)], 
        [(1, DEATHS)], 
        [(1, PRESSURE)],
        [(1,PRESSURE)], 
        [(0, NONE)]
        ]

    recon_target_types= [
        RECON_TARGET_IS_OBSERVE, 
        RECON_TARGET_IS_STEAL, 
        RECON_TARGET_IS_CONSULT
        ]

    #Religious data tables
    religious_targets = [
        ESCORT, 
        CLEANSING, 
        DEFENSE, 
        UNEARTH, 
        PICK_ONE_WITH_FAVOR, 
        PICK_ONE_WITH_FAVOR
        ]

    religious_rewards = [
        [(-1, TIME), (2, XP)], 
        [(2,MORALE), (10,SCORE_POINTS)], 
        [(1, INTEL), (2, MORALE)], 
        [(1, FINE_ASSET)],
        [(1, EXCEPTIONAL_ASSET)], 
        [(1,SPECIALIST)]
        ]

    religious_penalties = [
        [(-1, MORALE), (1,PRESSURE)],
        [(1,PRESSURE)],
        [(1,PRESSURE)],
        [(-1,MORALE)],
        [(-1, MORALE)],
        [(0,NONE)]
        ]

    religious_cultures_common = [
        RELIGIOUS_TARGET_ALDERMARK, 
        RELIGIOUS_TARGET_OLD_EMPIRE
        ]

    religious_cultures_uncommon = [
        RELIGIOUS_TARGET_BARTA, 
        RELIGIOUS_TARGET_OR, 
        RELIGIOUS_TARGET_PANYA, 
        RELIGIOUS_TARGET_ZEMYA
        ]

    religious_cultures_rare = [
        RELIGIOUS_TARGET_ANDRASTUS, 
        RELIGIOUS_TARGET_BONE_WASTES, 
        RELIGIOUS_TARGET_DAR, 
        RELIGIOUS_TARGET_ROYIN
        ]

    #cultures below are added multiple times in proportion to rarity so random.choice works in a weighted manner
    religious_cultures = [
        religious_cultures_common, 
        religious_cultures_common, 
        religious_cultures_common, 
        religious_cultures_common, 
        religious_cultures_uncommon, 
        religious_cultures_uncommon, 
        religious_cultures_rare
        ]

    #Supply data tables
    supply_targets = [
        SCROUNGE_OR_TRADE, 
        SCROUNGE_OR_TRADE, 
        RESCUE_SUPPLIES, 
        RESCUE_SUPPLIES, 
        MERCENARY_WORK, 
        MERCENARY_WORK
        ]

    supply_rewards = [
        [(1, ASSET), (1, SUPPLY)], 
        [(1, ASSET), (1, SUPPLY)], 
        [(2, SUPPLY)], 
        [(1, ASSET), (2, SUPPLY)], 
        [(3,SUPPLY)], 
        [(3, SUPPLY)]
        ]

    supply_penalties = [
        [(-1, MORALE), (-1, SUPPLY)], 
        [(-1,SUPPLY)],
        [(-1, MORALE)], 
        [(-1, MORALE)],
        [(0,NONE)],
        [(0,NONE)]
        ]

    mission_first_names = ['Swift', 'Unceasing', 'Vengeful', 'Lone', 'Cold', 'Hot', 'Purple', 'Brutal', 'Flying', 'Driving', 'Blind', 'Demon', 'Enduring', 'Defiant', 'Lost', 'Dying', 'Falling', 'Soaring', 'Twisted', 'Glass', 'Bleeding', 'Broken', 'Silent', 'Red', 'Black', 'Dark', 'Fallen', 'Patient', 'Burning', 'Final', 'Lazy', 'Morbid', 'Crimson', 'Cursed', 'Frozen', 'Bloody', 'Banished', 'First', 'Severed', 'Empty', 'Spectral', 'Sacred', 'Stone', 'Shattered', 'Hidden', 'Rotting', 'Devils', 'Forgotten', 'Blinding', 'Fading', 'Crystal', 'Secret', 'Cryptic', 'Smoking', 'Heaving', 'Steaming', 'Righteous', 'Purple', 'Amber', 'Wailing', 'Cosmic', 'Foolish', 'Brooding', 'Failing', 'Gasping', 'Starving', 'Sinking', 'Holy', 'Unholy', 'Potent', 'Haunting', 'Pungent', 'Golden', 'Iron', 'Shackled', 'Laughing', 'Damned', 'Poisoned', 'Half-eaten', 'Summoned', 'Gilded', 'Manic', 'Precious', 'Outer', 'Little', 'Choking', 'Half-dead', 'Steely', 'Massive', 'Dismal', 'Rebel', 'Dread', 'Sleeping', 'Magic', 'Dripping', 'Faceless', 'Shambling', 'Furious', 'Dead Mans', 'Perilous', 'Heavy', 'Ancient', 'Jagged', 'Northern', 'Earthly', 'Hellish', 'Hellborn', 'Blessed', 'Buried', 'Senseless', 'Blood-Soaked', 'Sweaty', 'Drunken', 'Azure', 'Amber', 'Broken', 'Chosen', 'Crimson', 'Diamond', 'Emerald', 'Flying', 'Grasping', 'Screaming', 'Shattered', 'Western', 'Desert', 'Forthright', 'Scarlet']
    mission_second_names = ['Engine', 'Chant', 'Heart', 'Justice', 'Law', 'Thunder', 'Moon', 'Heat', 'Fear', 'Star', 'Apollo', 'Prophet', 'Hero', 'Hydra', 'Serpent', 'Crown', 'Thorn', 'Empire', 'Summer', 'Druid', 'God', 'Savior', 'Stallion', 'Hawk', 'Vengeance', 'Calm', 'Knife', 'Sword', 'Dream', 'Sleep', 'Stroke', 'Flame', 'Spark', 'Fist', 'Dirge', 'Grave', 'Shroud', 'Breath', 'Smoke', 'Giant', 'Whisper', 'Night', 'Throne', 'Pipe', 'Blade', 'Daze', 'Pyre', 'Tears', 'Mother', 'Crone', 'King', 'Father', 'Priest', 'Dawn', 'Hammer', 'Shield', 'Hymn', 'Vanguard', 'Sentinel', 'Stranger', 'Bell', 'Mist', 'Fog', 'Jester', 'Scepter', 'Ring', 'Skull', 'Paramour', 'Palace', 'Mountain', 'Rain', 'Gaze', 'Future', 'Gift', 'Grin', 'Omen', 'Tome', 'Wail', 'Shriek', 'Glove', 'Gears', 'Slumber', 'Beast', 'Wolf', 'Widow', 'Witch', 'Prince', 'Skies', 'Dance', 'Spear', 'Key', 'Fog', 'Feast', 'Cry', 'Claw', 'Peak', 'Valley', 'Shadow', 'Rhyme', 'Moan', 'Wheel', 'Doom', 'Mask', 'Rose', 'Gods', 'Whale', 'Saga', 'Sky', 'Chalice', 'Agony', 'Misery', 'Tears', 'Rage', 'Anger', 'Laughter', 'Terror', 'Gasp', 'Tongue', 'Cobra', 'Snake', 'Cavern', 'Corpse', 'Prophecy', 'Vagabond', 'Altar', 'Death', 'Reckoning', 'Arrow', 'Citadel', 'Fire', 'Hawk', 'Light', 'Mountain', 'Peak', 'Storm', 'Thorn', 'Tiger', 'Wing', 'Wolf', 'Elephant', 'Feather', 'Guardian', 'Tower', 'Fist']