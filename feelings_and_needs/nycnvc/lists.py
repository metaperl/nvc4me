from loguru import logger

feelings = dict()
positive_feelings = list()
negative_feelings = list()

positive_feelings.append("""affectionate
compassionate
fond
loving
openhearted
tender
warm""".split())

positive_feelings.append("""engaged
absorbed
curious
engrossed
enchanted
enthralled
entranced
fascinated
interested
intrigued
involved
open
spellbound
stimulated""".split())

positive_feelings.append("""excited
amazed
ardent
aroused 
dazzled
energetic
enlivened
enthusiastic
exuberant
invigorated
lively
passionate
surprised
vibrant""".split())

positive_feelings.append("""exhilirated
enthralled
radiant
electrified
euphoric
overjoyed
thrilled""".split())

positive_feelings.append("""grateful
appreciative
moved
thankful
touched""".split())

positive_feelings.append("""happy
amused
blissful
cheerful
delighted
ecstatic
elated
giddy
glad
jolly
joyful
jubilant
merry
overjoyed
pleased
rapturous
tickled""".split())

positive_feelings.append("""hopeful
confident
expectant
jazzed
lighthearted
sanguine
up
upbeat""".split())

positive_feelings.append("""inspired
amazed
eager
enthused
motivated
moved
psyched
stimulated
stirred
wonder""".split())

positive_feelings.append("""peaceful
calm
comfortable
centered
content
equanimity
fulfilled
mellow
open
quiet
relaxed
relieved
satisfied
serene
tranquil""".split())

positive_feelings.append("""refreshed
recharged
rejuvenated
renewed
rested
restored
revived""".split())

negative_feelings.append("""anger
aggravated
angry
animosity
annoyed
contempt
disgruntled
enraged
exasperated
furious 
hate 
hostile
incensed
irate
irritated
irked
livid
miffed
nettled
outraged
peeved
resentful""".split())

negative_feelings.append("""aversion
abhorrence
appalled
bothered displeased
disgust
dislike 
enmity
horrified
loathing
repulsion
revulsion""".split())

negative_feelings.append("""confusion
ambivalent
baffled bewildered
conflicted
dazed
discombobulated
disoriented
mixed
mystified
perplexed puzzled
torn""".split())

negative_feelings.append("""disconnection
apathetic
bored
closed
detached
distant
indifferent
listless
numb
withdrawn""".split())

negative_feelings.append("""disquiet
agitated
alarmed
concerned
distraught 
disconcerted
dismayed
disturbed
frustrated
perturbed
rattled
restless
shocked
startled
surprised
troubled
turbulent
turmoil
uncomfortable
uneasy
unnerved
unsettled
upset""".split())

negative_feelings.append("""embarrassment
ashamed
chagrined
discomfited
flustered
mortified
self-conscious""".split())

negative_feelings.append("""fatigue
beat
burnt out
depleted
exhausted
listless
pooped
sleepy
tired
weary
wiped out
 worn out""".split())

negative_feelings.append("""fear
afraid
anxious
apprehensive
dread
fearful
foreboding
frightened
guarded
insecure
leery
mistrustful
panicked
petrified
scared
shaky
terrified
trepidation
wary
worried""".split())

negative_feelings.append("""pain
aching
agony
anguished
devastated
grief
heartbroken
hungry
hurting
lonely
miserable
regretful
remorseful""".split())

negative_feelings.append("""sadness
depressed
dejected
despairing 
despondent
disappointed
discouraged
disheartened
forlorn
gloomy
heavy hearted
hopeless
melancholy
miserable
unhappy
wistful""".split())

negative_feelings.append("""tension
anxious
closed
distressed
edgy
fidgety
frazzled
frustrated 
jittery
nervous
overwhelmed
restless
stressed out""".split())

negative_feelings.append("""yearning
longing
nostalgic
pining""".split())

feelings['positive'] = positive_feelings
feelings['negative'] = negative_feelings

logger.info(str(feelings))
