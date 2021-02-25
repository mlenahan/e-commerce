from django.db import models


class Rarity:
    COMMON = 'Common'
    UNCOMMON = 'Uncommon'
    RARE = 'Rare'
    ULTRA_RARE = 'Ultra Rare'
    AMAZING_RARE = 'Amazing Rare'
    SECRET_RARE = 'Secret Rare'
    CHOICES = [
        (COMMON, 'Common'),
        (UNCOMMON, 'Uncommon'),
        (RARE, 'Rare'),
        (ULTRA_RARE, 'Ultra Rare'),
        (AMAZING_RARE, 'Amazing Rare'),
        (SECRET_RARE, 'Secret Rare')
    ]

class Languages:
    ENGLISH = 'English'
    JAPANESE = 'Japanese'
    FRENCH = 'French'
    SPANISH = 'Spanish'
    GERMAN = 'German'
    CHINESE ='Chinese'
    KOREAN = 'Korean'
    CHOICES = [
        (ENGLISH, 'English'),
        (JAPANESE, 'Japanese'),
        (FRENCH, 'French'),
        (SPANISH, 'Spanish'),
        (GERMAN, 'German'),
        (CHINESE, 'Chinese'),
        (KOREAN, 'Korean')
    ]

class Condition:
    SEALED_PRODUCT = 'Sealed Product'
    PACK_FRESH = 'Pack Fresh'
    LIGHT_PLAY = 'Light Play'
    MODERATE_PLAY = 'Moderate Play'
    HEAVY_PLAY = 'Heavy Play'
    DAMAGED = 'Damaged'
    CHOICES = [
        (SEALED_PRODUCT, 'Sealed Product'),
        (PACK_FRESH, 'Pack Fresh'),
        (LIGHT_PLAY, 'Light Play'),
        (MODERATE_PLAY, 'Moderate Play'),
        (HEAVY_PLAY, 'Heavy Play'),
        (DAMAGED, 'Damaged')
    ]

class ProductType:
    BOOSTER_BOX = 'Booster Box'
    ELITE_TRAINER_BOX_PLUS = 'Elite Trainer Box Plus'
    ELITE_TRAINER_BOX = 'Elite Trainer Box'
    PREMIUM_COLLECTION_BOX = 'Premium Collection Box'
    POKEMON_THEMED_BOX = 'Pokemon Themed Box'
    PIN_BOX = 'Pin Box'
    THEME_DECK = 'Theme Deck'
    BUILD_AND_BATTLE_DECK = 'Build and Battle Deck'
    PREMIUM_BLISTER = 'Premium Blister'
    THREE_PACK_BLISTER = 'Three Pack Blister'
    SINGLE_PACK_BLISTER = 'Single Pack Blister'
    BOOSTER_PACK = 'Booster Pack'
    SINGLE_CARD = 'Single Card'
    CHOICES = [
        (BOOSTER_BOX, 'Booster Box'),
        (ELITE_TRAINER_BOX_PLUS, 'Elite Trainer Box Plus'),
        (ELITE_TRAINER_BOX, 'Elite Trainer Box'),
        (PREMIUM_COLLECTION_BOX, 'Premium Collection Box'),
        (POKEMON_THEMED_BOX, 'Pokemon Themed Box'),
        (PIN_BOX, 'Pin Box'),
        (THEME_DECK, 'Theme Deck'),
        (BUILD_AND_BATTLE_DECK, 'Build and Battle Deck'),
        (PREMIUM_BLISTER, 'Premium Blister'),
        (THREE_PACK_BLISTER, 'Three Pack Blister'),
        (SINGLE_PACK_BLISTER, 'Single Pack Blister'),
        (BOOSTER_PACK, 'Booster Pack'),
        (SINGLE_CARD, 'Single Card')
    ]

