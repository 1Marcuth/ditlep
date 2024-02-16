# Ditlep

Well, this package is a Ditlep API wrapper with a data decryption layer.

I then intend to add a translation layer using my other library, [`dragon-city-utils`](https://github.com/1Marcuth/py.dragon-city-utils) to obtain translated data regardless of the language, different from what we see on the Ditlep website, which is only in English, but well, that's for sure. when you feel like using this library again ;)

---

## Using

To use this library is very simple, you just need to create an instance of the Ditlep object and pass some parameters:

```python
from ditlep import Ditlep

ditlep = Ditlep(
    iv = "...",
    password = "...",
    salt = "...",
    dk_len = ...,
    count = ...
)
```

> If you don't know the decryption parameters you can try to contact me so I can give you them

---

Well, now just be happy, this object can get different information from Ditlep, not all of it because I haven't explored all of Ditlep's existing endpoints, especially since they ended up updating their website recently...

Here's an example of how to get data from the Heroic Race:

```python
data = ditlep.get_heroic_races()
```

Running the code, you will have something like this:

```python
{'island': {'dragon_race_id': 3175, 'rewards': None, 'title': 'High Passion  Heroic Race Guide', 'laps': None, 'boards': None, 'id': 0, 'start_ts': 1707390000, 'end_ts': 1708340399, 'isValid': True, 'isUpComing': False, 'timeLeft': 249747, 'pool_points': 0, 'pool_time': 0, 'tid_name': None}, 'dragonRewards': [{'attackSkills': [{'element': 'bt', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 1200, 'time': '24', 'originalName': 'Beauty 1', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 406, 'groupType': None, 'name': 'Beauty 1 - Damage: 1200', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}, {'element': 'f', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 1500, 'time': '1', 'originalName': 'Fire', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 217, 'groupType': None, 'name': 'Fire - Damage: 1500', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}, {'element': 'el', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 1300, 'time': '24', 'originalName': 'Electro Ball', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 408, 'groupType': None, 'name': 'Electro Ball - Damage: 1300', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}, {'element': 'ch', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 1450, 'time': '24', 'originalName': 'Iron Shock', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 486, 'groupType': None, 'name': 'Iron Shock - Damage: 1450', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}], 'hasSKill': False, 'trainableAttackSkills': None, 'attackSkillsRaw': [406, 217, 408, 486], 'trainableAttackSkillsRaw': [397, 372, 525, 538], 'dragonAttribute': ['/Content/Images/DragonType/ic-beauty-flag.png', 
'/Content/Images/DragonType/ic-fire-flag.png', '/Content/Images/DragonType/ic-electric-flag.png', '/Content/Images/DragonType/ic-chaos-flag.png'], 'level': 0, 'isStuck': False, 'isTraining': False, 'isBreeding': False, 'isInTower': False, 'rarity': 'H', 'elements': ['bt', 'f', 'el', 'ch'], 'kill': 0, 'hp': 0, 'damage': 0, 'maxHp': 0, 'maxDamage': 0, 'funModeDragonId': 0, 'amount': 0, 'description': None, 'urlName': 'High-Passion-Dragon', 'priceSell': 0, 'priceGold': 0, 'priceGem': 0, 'hatchingTime': 0, 'breedingTime': 0, 'category': 11, 'inStore': False, 'breedable': False, 'releaseDate': None, 'rank': {'globalRank': 51, 'rarityRank': 18, 'categoryRank': 18, 'speedRank': 1033}, 'originalTypeId': 0, 'maxSpeed': 890, 'baseSpeed': 130, 'weaknessElements': ['mg', 'so'], 'strongElements': ['dr', 'hp', 'i', 'm', 'mg', 'p', 'so', 'w'], 'skills': [], 'skillType': 0, 'familyName': None, 'familyIcon': None, 'habitatId': 0, 'workId': 0, 'xp': None, 'workingSecondsLeft': 0.0, 'grade': 0, 'id': 3175, 'groupType': 'DRAGON', 'name': 'High Passion Dragon', 'type': 3175, 'typeId': 3175, 'image': 'dragons/ui_3175_dragon_highpassion', 'customName': None}, {'attackSkills': [{'element': 'mg', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 1050, 'time': '24', 'originalName': 'Magic Blow', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 71, 'groupType': None, 'name': 'Magic Blow - Damage: 1050', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}, {'element': 'd', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 650, 'time': '12', 'originalName': 'Leech', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 26, 'groupType': None, 'name': 'Leech - Damage: 650', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}, {'element': 'w', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 550, 'time': '12', 'originalName': 'Tsunami', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 16, 'groupType': None, 'name': 'Tsunami - Damage: 550', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}, {'element': 'p', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 650, 'time': '12', 'originalName': 'Poison Ivy', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 11, 'groupType': None, 'name': 'Poison Ivy - Damage: 650', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}], 'hasSKill': False, 'trainableAttackSkills': None, 'attackSkillsRaw': [71, 26, 16, 11], 'trainableAttackSkillsRaw': [261, 164, 44, 39], 'dragonAttribute': ['/Content/Images/DragonType/ic-magic-flag.png', '/Content/Images/DragonType/ic-dark-flag.png', '/Content/Images/DragonType/ic-water-flag.png', '/Content/Images/DragonType/ic-plant-flag.png'], 'level': 0, 'isStuck': False, 'isTraining': False, 'isBreeding': False, 'isInTower': False, 'rarity': 'L', 'elements': ['mg', 'd', 'w', 'p'], 'kill': 0, 'hp': 0, 'damage': 0, 'maxHp': 0, 'maxDamage': 0, 'funModeDragonId': 0, 'amount': 0, 'description': None, 'urlName': 'Magicienne-Dragon', 'priceSell': 0, 'priceGold': 0, 'priceGem': 0, 'hatchingTime': 0, 'breedingTime': 0, 'category': 9, 'inStore': False, 'breedable': False, 'releaseDate': None, 'rank': {'globalRank': 495, 'rarityRank': 417, 'categoryRank': 300, 'speedRank': 727}, 'originalTypeId': 0, 'maxSpeed': 974, 'baseSpeed': 114, 'weaknessElements': ['ch', 'hp'], 'strongElements': ['bt', 'f', 'li', 'li', 'm', 'so', 'w', 'wr'], 'skills': [], 'skillType': 0, 'familyName': None, 'familyIcon': None, 'habitatId': 0, 'workId': 0, 'xp': None, 'workingSecondsLeft': 0.0, 'grade': 0, 
'id': 2658, 'groupType': 'DRAGON', 'name': 'Magicienne Dragon', 'type': 2658, 'typeId': 2658, 'image': 'dragons/ui_2658_dragon_magicienne', 'customName': None}, {'attackSkills': [{'element': 'ph', 'isAdvanceSkill': False, 'skillType': 1, 'damage': 338, 'time': '12', 'originalName': 'Punch', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 1, 'groupType': None, 'name': 'Punch - Damage: 338', 'type': 0, 'typeId': 0, 'image': None, 'customName': None}, {'element': 'm', 'isAdvanceSkill': True, 'skillType': 2, 'damage': 1200, 'time': '24', 'originalName': 'Cannon Balls', 'totalDragons': 0, 'skillEffect': None, 'description': None, 'target': None, 'randomSkills': None, 'skillId': 0, 'specialIcon': 0, 'id': 51, 'groupType': None, 'name': 'Cannon Balls - Damage: 1200', 'type': 0, 'typeId': 0, 'image': None, 'customName': None},
```

## Possible problems

- If you receive the error `ValueError: Data must be padded to 16 byte boundary in CBC mode` it is likely that the data you are looking for is not currently available, an example of this is an event that has already been completed and has been removed from the endpoints.

## How to Contribute

If you want to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a branch for your feature (`git checkout -b feature/MyFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/MyFeature`).
5. Create a new Pull Request.

## Author

Marcuth [@1marcuth](https://github.com/1marcuth)

## License

This project is licensed under the MIT License.