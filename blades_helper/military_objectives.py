class MilitaryObjectiveConstants:
    MO_BLOCK = 'MO_BLOCK'
    MO_BREACH = 'MO_BREACH'
    MO_BYPASS = 'MO_BYPASS'
    MO_CLEAR = 'MO_CLEAR'
    MO_CONTAIN = 'MO_CONTAIN'
    MO_CONTROL = 'MO_CONTROL'
    MO_COUNTERRECON = 'MO_COUNTERRECON'
    MO_DEFEAT = 'MO_DEFEAT'
    MO_DESTROY = 'MO_DESTROY'
    MO_DISENGAGE = 'MO_DISENGAGE'
    MO_DISRUPT = 'MO_DISRUPT'
    MO_FIXLOCATION = 'MO_FIXLOCATION'
    MO_CAPTURE = 'MO_CAPTURE'
    MO_SECURE = 'MO_SECURE'
    MO_SEIZE = 'MO_SEIZE'
    MO_SURPRESS = 'MO_SURPRESS'
    MO_RECON = 'MO_RECON'
    MO_CONVINCE = 'MO_CONVINCE'
    

    MILITARY_OBJECTIVES = { 
        'MO_BLOCK': {'key': 'MO_BLOCK', 'description': 'Prevent the enemy from accessing an area or advancing along a specific route.', 'example': 'Gandalf on the bridge. Letting an ally escape. delaying an enemy until a trap is set. Keeping enemy out during a ritual.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '0', 'is_religious': '0'},
        'MO_BREACH': {'key': 'MO_BREACH', 'description': 'Break through the enemy line to create a passage to a specific point on the battlemap.', 'example': "Keep the route of an ally's escape open. Punch a whole in a line to let an ally into an area behind enemy lines", 'is_assault': '1', 'is_recon': '0', 'is_supply': '0', 'is_religious': '1'},
        'MO_BYPASS': {'key': 'MO_BYPASS', 'description': 'Move across the battlemap to a specific point on the battlemap without detection.', 'example': 'Place listening device in a location without raising the alarm.  Assassination. Kidnapping. Put the guards at a location out of commission without raising the alarm so more troops can get through. Get in and plant false info.', 'is_assault': '0', 'is_recon': '1', 'is_supply': '0', 'is_religious': '0'},
        'MO_CLEAR': {'key': 'MO_CLEAR', 'description': 'Eliminate all the enemy in a specific area, such as a room in a dungeon.', 'example': 'Remove bandits from a town. Remove monsters from a field. Clean up fleeing troops. Remove troops laying an ambush.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '0', 'is_religious': '1'},
        'MO_CONTAIN': {'key': 'MO_CONTAIN', 'description': 'Surround or otherwise trap the bad guys and prevent their escape.', 'example': "Keep enemy in a location until a bomb goes off or the siege weapons fire.  Keep a Lieutennant locked in a building until the Chosen gets there.  Keep some elites in a building so that can't kill innocents until the cavalry comes.", 'is_assault': '1', 'is_recon': '0', 'is_supply': '0', 'is_religious': '0'},
        'MO_CONTROL': {'key': 'MO_CONTROL', 'description': 'Keep the enemy off of specific squares of the battlemap to prevent their use.', 'example': 'Guard a teleportation circle until allies get through. Keep enemies from Siege engines until the barage is over. Keep baddies from a temple until ritual cleaning is complete. Hold off baddies while the goods are loaded.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '1', 'is_religious': '1'},
        'MO_COUNTERRECON': {'key': 'MO_COUNTERRECON', 'description': 'Idenify or elminate observers.', 'example': 'Legion suspects a spy is watching the army- find them and eliminate.   Identify Hexed in a village terrorizing the locals. Refugees taken in by Legion have some Hexed that are divulging plans - eliminate them. Convince the enemy that you are a large force at a location by making an attack.', 'is_assault': '1', 'is_recon': '1', 'is_supply': '0', 'is_religious': '0'},
        'MO_DEFEAT': {'key': 'MO_DEFEAT', 'description': 'Achieve a total victory but killing the enemy is not required.', 'example': 'Mop up stragglers.  A unit is left unprotected- eliminate or get them to surrender.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '0', 'is_religious': '0'},
        'MO_DESTROY': {'key': 'MO_DESTROY', 'description': 'Kill or permanently eliminate enemy.', 'example': 'A Lietennant is left in the lurch - kill them.   You found the infamous that killed your commander-go get revenge.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '0', 'is_religious': '1'},
        'MO_DISENGAGE': {'key': 'MO_DISENGAGE', 'description': 'Reach a specific area, away from the enemy that will allow them to escape with no chance of immediately successful pursuit.', 'example': 'You failed original engagement roll and encontered a huge force - get away. An ally is surrounded- you need to free them and then disengage.', 'is_assault': '1', 'is_recon': '1', 'is_supply': '1', 'is_religious': '0'},
        'MO_DISRUPT': {'key': 'MO_DISRUPT', 'description': 'Break apart the enemy or lock down a specific foe.', 'example': 'Wild animals are being controlled by an infamous- eliminate the leader to stop the attacks. Siege weapons are raining hell- disrupt them! Snipers are on a ridge- move them our of position so legion can pass.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '0', 'is_religious': '1'},
        'MO_FIXLOCATION': {'key': 'MO_FIXLOCATION', 'description': 'Find and surround or otherwise trap the bad guys in a specific area for a specific duration.', 'example': 'Find the infamous and keep their location locked so chosen can get their and eliminate.   An armored caravan is bringing supplies through.   Fix the location and call in a strike of the siege enginer.', 'is_assault': '0', 'is_recon': '1', 'is_supply': '0', 'is_religious': '1'},
        'MO_CAPTURE': {'key': 'MO_CAPTURE', 'description': 'Acquire a target object or creature.', 'example': 'Capture a Broken. Retrieve a relic.', 'is_assault': '0', 'is_recon': '0', 'is_supply': '1', 'is_religious': '1'},
        'MO_SECURE': {'key': 'MO_SECURE', 'description': 'Protect a person, a place, or an object from being damaged or destroyed by the enemy.', 'example': 'Caravan guard.  Bodyguard.  An ally has fallen and the unit must go protect them until reinforcements arrive.  Get an ally across the bridge.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '1', 'is_religious': '1'},
        'MO_SEIZE': {'key': 'MO_SEIZE', 'description': 'Move together to a specific location on the battlemap, remove all enemy from that area and stay in that area without losing it to the enemy.', 'example': 'Retake the temple.  Go get the caravan and hold it until help arrives.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '1', 'is_religious': '1'},
        'MO_SURPRESS': {'key': 'MO_SURPRESS', 'description': 'Keep the enemy locked in combat for a period.', 'example': 'Attack the front gate for x rounds until an ally goes in the back.   Surpess enemy while Chosen attacks a broken.', 'is_assault': '1', 'is_recon': '0', 'is_supply': '0', 'is_religious': '0'},
        'MO_RECON': {'key': 'MO_RECON', 'description': 'Observe an object or area.', 'example': 'Find out what is written in the temple. Scout enemy troop size. Find a route through the desert.', 'is_assault': '0', 'is_recon': '1', 'is_supply': '1', 'is_religious': '1'},
        'MO_CONVINCE': {'key': 'MO_CONVINCE', 'description': 'Convince a group to go along with a plan', 'example': 'Convince the locals to give you the relic. Get bandits to stop attacking trade routes. Get the soldier to give you data.', 'is_assault': '0', 'is_recon': '1', 'is_supply': '1', 'is_religious': '1'},
    }