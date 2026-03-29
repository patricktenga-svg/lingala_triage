"""
lingala_stopwords.py
====================
A curated stopword list for Lingala (ln) NLP tasks.

There is no official Lingala stopword list in NLTK, spaCy, or any major NLP
library. This list was compiled from:
  - Lingala grammar references (Swarthmore LING073, FSI Basic Course)
  - "Loba Lingala" guide (Yocum, 2014)
  - Wikipedia Lingala grammar article
  - Linguistic analysis of the medical triage corpus used in this project

Organized by grammatical category so you can customize for your task.
For example, in medical NLP you may want to KEEP negation words like "te"
(not/no) since they change clinical meaning drastically.

Author: Generated for Lingala Medical Triage NLP project
"""

# ──────────────────────────────────────────────────────────────────────────────
# 1. SUBJECT PRONOUNS
# These are verbal prefixes that double as standalone pronouns.
# ──────────────────────────────────────────────────────────────────────────────
SUBJECT_PRONOUNS = {
    "na",    # I / me (1sg)
    "o",     # you (2sg)
    "a",     # he / she / it (3sg animate)
    "to",    # we (1pl)
    "bo",    # you (2pl)
    "ba",    # they (3pl animate)
    "e",     # it (3sg inanimate)
    "i",     # they (3pl inanimate)
}

# ──────────────────────────────────────────────────────────────────────────────
# 2. PERSONAL / POSSESSIVE PRONOUNS
# ──────────────────────────────────────────────────────────────────────────────
PERSONAL_PRONOUNS = {
    "ngai",   # I / me / my (emphatic 1sg)
    "nga",   # I / me / my (emphatic 1sg)
    "yo",     # you / your (emphatic 2sg)
    "ye",     # him / her / his / her (emphatic 3sg)
    "biso",   # us / our (1pl)
    "bino",   # you / your (2pl)
    "bango",  # them / their (3pl)
}

# ──────────────────────────────────────────────────────────────────────────────
# 3. DEMONSTRATIVE PRONOUNS
# ──────────────────────────────────────────────────────────────────────────────
DEMONSTRATIVES = {
    "oyo",    # this / these (proximal)
    "wana",   # that / those (distal)
    "kuna",   # that over there (remote)
    "awa",    # here
    "kuna",   # there
    "wapi",   # where (interrogative/relative)
}

# ──────────────────────────────────────────────────────────────────────────────
# 4. CORE PREPOSITIONS & PARTICLES
# na and ya are by far the most frequent words in Lingala text.
# ──────────────────────────────────────────────────────────────────────────────
PREPOSITIONS_PARTICLES = {
    "na",     # with / at / in / to / and (multi-purpose preposition)
    "ya",     # of / from / belonging to (genitive/connective particle)
    "pe",     # also / too / and
    "mpe",    # and / also / as well
    "to",     # or (conjunction)
    "po",     # for / because (colloquial)
    "pona",   # for / in order to
    "kati",   # in / inside / among
    "wuti",   # from / coming from
    "uta",    # from / since
    "tii",    # until / up to
    "ata",    # even / even if
    "lelo",   # today (frequently functions as temporal filler)
}

# ──────────────────────────────────────────────────────────────────────────────
# 5. COPULA & AUXILIARY VERBS (conjugated forms of kozala = to be/have)
# ──────────────────────────────────────────────────────────────────────────────
COPULA_AUXILIARY = {
    "nazali",  # I am / I have (1sg present)
    "ozali",   # you are / you have (2sg present)
    "azali",   # he/she is / has (3sg present)
    "tozali",  # we are / we have (1pl present)
    "bozali",  # you are / you have (2pl present)
    "bazali",  # they are / they have (3pl present)
    "ezali",   # it is / it has (inanimate present)
    # Equator region spoken Lingala
    "nadjali",  # I am / I have (1sg present)
    "odjali",   # you are / you have (2sg present)
    "adjali",   # he/she is / has (3sg present)
    "todjali",  # we are / we have (1pl present)
    "bodjali",  # you are / you have (2pl present)
    "badjali",  # they are / they have (3pl present)
    "edjali",   # it is / it has (inanimate present)
    "bidjali",   # it is / it has (inanimate present)
    # Other region spoken Lingala
    "nayali",  # I am / I have (1sg present)
    "oyali",   # you are / you have (2sg present)
    "ayali",   # he/she is / has (3sg present)
    "toyali",  # we are / we have (1pl present)
    "boyali",  # you are / you have (2pl present)
    "bayali",  # they are / they have (3pl present)
    "eyali",   # it is / it has (inanimate present)
    "biyali",   # it is / it has (inanimate present)
    # Other region spoken Lingala
    "naali",  # I am / I have (1sg present)
    "oali",   # you are / you have (2sg present)
    "aali",   # he/she is / has (3sg present)
    "toali",  # we are / we have (1pl present)
    "boali",  # you are / you have (2pl present)
    "baali",  # they are / they have (3pl present)
    "eali",   # it is / it has (inanimate present)
    "biali",   # it is / it has (inanimate present)
    # Contracted / colloquial forms (Kinshasa spoken Lingala)
    "naza",    # contracted: nazali
    "oza",     # contracted: ozali
    "aza",     # contracted: azali
    "toza",    # contracted: tozali
    "boza",    # contracted: bozali
    "baza",    # contracted: bazali
    # Contracted / colloquial forms (Kinshasa spoken Lingala)
    "nazo",    # contracted: nazali+ko
    "ozo",     # contracted: nazali+ko
    "azo",     # contracted: nazali+ko
    "tozo",    # contracted: nazali+ko
    "bozo",    # contracted: nazali+ko
    "bazo",    # contracted: nazali+ko
    # Contracted / colloquial forms (Kinshasa spoken Lingala)
    "nao",    # contracted: nazali+ko
    "oo",     # contracted: nazali+ko
    "ao",     # contracted: nazali+ko
    "too",    # contracted: nazali+ko
    "boo",    # contracted: nazali+ko
    "bao",    # contracted: nazali+ko
    # Past forms
    "nazalaki",
    "ozalaki",
    "azalaki",
    "tozalaki",
    "bozalaki",
    "bazalaki",
    "ezalaki",
}

# ──────────────────────────────────────────────────────────────────────────────
# 6. NEGATION
# ⚠️  WARNING: In medical / clinical NLP, negation words change meaning
# entirely (e.g., "nazali kokosola te" = "I am NOT coughing").
# Consider KEEPING these depending on your task.
# ──────────────────────────────────────────────────────────────────────────────
NEGATION = {
    "te",     # not / no (primary negation particle, always final)
    "ata te", # not at all / absolutely not
    "ata",    # even (used in negative constructions)
}

# ──────────────────────────────────────────────────────────────────────────────
# 7. QUESTION WORDS
# ──────────────────────────────────────────────────────────────────────────────
QUESTION_WORDS = {
    "nini",    # what
    "nani",    # who
    "wapi",    # where
    "ndenge",  # how
    "mpo",     # why (short form)
    "mpona",   # why / for what reason
    "ntango",  # when / time (can also be content word in medical context)
    "boni",    # how many / how
    "etuka",   # which (inanimate)
    "moto",    # which person / who (can be content word = "person/head")
}

# ──────────────────────────────────────────────────────────────────────────────
# 8. CONJUNCTIONS
# ──────────────────────────────────────────────────────────────────────────────
CONJUNCTIONS = {
    "mpe",     # and / also
    "kasi",    # but / however
    "soki",    # if / when (conditional)
    "tango",   # when / as (temporal)
    "ntango",  # when / at the time
    "ndenge",  # as / how / like
    "po",      # because (colloquial)
    "pamba",   # because / in vain (context-dependent)
    "kutu",    # moreover / even more so
    "lisusu",  # again / also / moreover
    "boye",    # so / thus / like that
    "yango",   # that / therefore / so (demonstrative/connective)
    "bongo",   # so / therefore (discourse connector)
    "kombo",   # namely / which is called
}

# ──────────────────────────────────────────────────────────────────────────────
# 9. ADVERBS OF DEGREE / FREQUENCY / TIME (high frequency, low content)
# ──────────────────────────────────────────────────────────────────────────────
ADVERBS = {
    "mingi",    # much / many / very / a lot
    "moke",     # little / few / slightly
    "makasi",   # strongly / hard / severely (⚠️ can be clinically relevant)
    "malamu",   # well / good / fine
    "mabe",     # badly / poorly
    "noki",     # quickly / soon
    "lɛlɔ",     # today
    "lobi",     # tomorrow / yesterday (context-dependent)
    "kala",     # long ago / for a long time
    "sik'oyo",  # now / at the moment
    "sikoyo",   # now (variant)
    "nanu",     # not yet / still
    "likoló",   # above / up / more
    "nse",      # below / down
    "mbala",    # time(s) / once (as in "mbala moko" = once)
    "moko",     # one / alone / same (also a numeral)
    "mibale",   # two
    "misato",   # three
    "mpenza",   # really / truly / very much
    "solo",     # really / truly (from French "seul"?)
    "awa",      # here
    "kuna",     # there
    "fulu",     # suddenly / at once
}

# ──────────────────────────────────────────────────────────────────────────────
# 10. COMMON DISCOURSE FILLERS & INTERJECTIONS
# ──────────────────────────────────────────────────────────────────────────────
DISCOURSE_FILLERS = {
    "ee",      # yes
    "iyo",     # yes
    "yango",   # that / it (discourse filler)
    "bongo",   # so / thus / OK
    "ah",      # interjection
    "eh",      # interjection / hesitation
    "hm",      # hesitation
    "yoka",    # listen! / hey!
    "tala",    # look! / see!
    "eee",     # filler / affirmation
    "oo",      # oh! (surprise/understanding)
    "ko",      # infinitive marker (when isolated, not part of a verb)
}

# ──────────────────────────────────────────────────────────────────────────────
# 11. COMMON VERB PREFIXES / INFINITIVE MARKER
# These are not standalone stopwords but useful for morphological stripping.
# ──────────────────────────────────────────────────────────────────────────────
VERB_PREFIXES = [
    "ko",    # infinitive prefix
    "na",    # 1sg conjugation prefix
    "o",     # 2sg conjugation prefix
    "a",     # 3sg conjugation prefix
    "to",    # 1pl conjugation prefix
    "bo",    # 2pl conjugation prefix
    "ba",    # 3pl conjugation prefix
    "e",     # inanimate 3sg prefix
    "bi",     # inanimate 3sg prefix

]

# ──────────────────────────────────────────────────────────────────────────────
# MASTER STOPWORD SET
# Combines all categories. Customize by removing categories you need.
# ──────────────────────────────────────────────────────────────────────────────
STOPWORDS_FULL = (
    SUBJECT_PRONOUNS
    | PERSONAL_PRONOUNS
    | DEMONSTRATIVES
    | PREPOSITIONS_PARTICLES
    | COPULA_AUXILIARY
    | NEGATION          # ⚠️ remove this line for medical NLP!
    | QUESTION_WORDS
    | CONJUNCTIONS
    | ADVERBS
    | DISCOURSE_FILLERS
)

# Safe version for MEDICAL / CLINICAL NLP:
# Keeps negation and severity adverbs which carry clinical meaning.
STOPWORDS_MEDICAL = (
    SUBJECT_PRONOUNS
    | PERSONAL_PRONOUNS
    | DEMONSTRATIVES
    | PREPOSITIONS_PARTICLES
    | COPULA_AUXILIARY
    # NEGATION excluded — "te" changes clinical meaning
    | QUESTION_WORDS
    | CONJUNCTIONS
    | (ADVERBS - {"makasi", "mingi", "moke", "mpenza", "malamu", "mabe"})
    | DISCOURSE_FILLERS
)


# ──────────────────────────────────────────────────────────────────────────────
# USAGE
# ──────────────────────────────────────────────────────────────────────────────
def remove_stopwords(text: str, stopwords: set = STOPWORDS_MEDICAL) -> str:
    """
    Remove stopwords from a Lingala string.
    Lowercases before comparison; preserves original casing in output.
    """
    tokens = text.split()
    return " ".join(t for t in tokens if t.lower() not in stopwords)


def tokenize_and_filter(text: str, stopwords: set = STOPWORDS_MEDICAL) -> list:
    """Returns a list of non-stopword tokens."""
    return [t for t in text.split() if t.lower() not in stopwords]


if __name__ == "__main__":
    print(f"Full stopword list:    {len(STOPWORDS_FULL)} words")
    print(f"Medical stopword list: {len(STOPWORDS_MEDICAL)} words")
    print()

    examples = [
        "Naali na nkanda moke mpe nazali kolɛmba",
        "Nzoto na ngai ezali kobɛta makasi mpe mpɛmɛ ekɔtaka te",
        "Mwana azali na fiɛvɛrɛ ya 41°C mpe azali komilinga",
        "nao yoka mokongo pasi makasi moko",

    ]

    print("── Example: Medical stopword removal ──")
    for ex in examples:
        filtered = remove_stopwords(ex, STOPWORDS_MEDICAL)
        print(f"  Original : {ex}")
        print(f"  Filtered : {filtered}")
        print()
