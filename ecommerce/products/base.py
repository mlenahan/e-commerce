from django.db import models


class Rarity:
    COMMON = 'common'
    UNCOMMON = 'uncommon'
    RARE = 'rare'
    ULTRA_RARE = 'ultra rare'
    AMAZING_RARE = 'amazing rare'
    SECRET_RARE = 'secret rare'

class Languages:
    ENGLISH = 'English'
    JAPANESE = 'Japanese'
    FRENCH = 'French'
    SPANISH = 'Spanish'
    GERMAN = 'German'
    CHINESE ='Chinese'
    KOREAN = 'Korean'

class Condition:
    SEALED_PRODUCT = 'sealed product'
    PACK_FRESH = 'pack fresh'
    LIGHT_PLAY = 'light play'
    MODERATE_PLAY = 'moderate play'
    HEAVY_PLAY = 'heavy play'
    DAMAGED = 'damaged'

class ProductType:
    BOOSTER_BOX = 'booster box'
    ELITE_TRAINER_BOX_PLUS = 'elite trainer box plus'
    ELITE_TRAINER_BOX = 'elite trainer box'
    PREMIUM_COLLECTION_BOX 'premium collection box'
    POKEMON_THEMED_BOX = 'pokemon themed box'
    PIN_BOX = 'pin box'
    THEME_DECK = 'theme deck'
    BUILD_AND_BATTLE_DECK = 'build and battle deck'
    PREMIUM_BLISTER = 'premium blister'
    THREE_PACK_BLISTER = 'three pack blister'
    SINGLE_PACK_BLISTER = 'single pack blister'
    BOOSTER_PACK = 'booster pack'
    SINGLE_CARD = 'single card'


