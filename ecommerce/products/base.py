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


# TODO singular!
class Languages:
    ENGLISH = 'English'
    JAPANESE = 'Japanese'
    FRENCH = 'French'
    SPANISH = 'Spanish'
    GERMAN = 'German'
    CHINESE = 'Chinese'
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
    BOOSTER_BOX = 'booster-box'
    ELITE_TRAINER_BOX_PLUS = 'elite-trainer-box-plus'
    ELITE_TRAINER_BOX = 'elite-trainer-box'
    PREMIUM_COLLECTION_BOX = 'premium-collection-box'
    POKEMON_THEMED_BOX = 'pokemon-themed-box'
    PIN_BOX = 'pin-box'
    THEME_DECK = 'theme-deck'
    BUILD_AND_BATTLE_DECK = 'build-and-battle-deck'
    PREMIUM_BLISTER = 'premium-blister'
    THREE_PACK_BLISTER = 'three-pack-blister'
    SINGLE_PACK_BLISTER = 'single-pack-blister'
    BOOSTER_PACK = 'booster-pack'
    SINGLE_CARD = 'single-card'
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
