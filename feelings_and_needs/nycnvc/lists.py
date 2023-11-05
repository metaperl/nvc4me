from loguru import logger

feelings = dict()  # https://www.nycnvc.org/feelings
positive_feelings = list()
negative_feelings = list()
needs = list()  # https://www.nycnvc.org/needs

positive_feelings.append(sorted("""affectionate
compassionate
fond
loving
openhearted
tender
warm""".splitlines()))

positive_feelings.append(sorted("""engaged
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
stimulated""".splitlines()))

positive_feelings.append(sorted("""excited
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
vibrant""".splitlines()))

positive_feelings.append(sorted("""exhilarated
enthralled
radiant
electrified
euphoric
overjoyed
thrilled""".splitlines()))

positive_feelings.append(sorted("""grateful
appreciative
moved
thankful
touched""".splitlines()))

positive_feelings.append(sorted("""happy
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
tickled""".splitlines()))

positive_feelings.append(sorted("""hopeful
confident
expectant
jazzed
lighthearted
sanguine
up
upbeat""".splitlines()))

positive_feelings.append(sorted("""inspired
amazed
eager
enthused
motivated
moved
psyched
stimulated
stirred
wonder""".splitlines()))

positive_feelings.append(sorted("""peaceful
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
tranquil""".splitlines()))

positive_feelings.append(sorted("""refreshed
recharged
rejuvenated
renewed
rested
restored
revived""".splitlines()))

negative_feelings.append(sorted("""anger
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
resentful""".splitlines()))

negative_feelings.append(sorted("""aversion
abhorrence
appalled
bothered 
displeased
disgust
dislike 
enmity
horrified
loathing
repulsion
revulsion""".splitlines()))

negative_feelings.append(sorted("""confusion
ambivalent
baffled 
bewildered
conflicted
dazed
discombobulated
disoriented
mixed
mystified
perplexed puzzled
torn""".splitlines()))

negative_feelings.append(sorted("""disconnection
apathetic
bored
closed
detached
distant
indifferent
listless
numb
withdrawn""".splitlines()))

negative_feelings.append(sorted("""disquiet
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
upset""".splitlines()))

negative_feelings.append(sorted("""embarrassment
ashamed
chagrined
discomfited
flustered
mortified
self-conscious""".splitlines()))

negative_feelings.append(sorted("""fatigue
beat
burnt-out
depleted
exhausted
listless
pooped
sleepy
tired
weary
wiped-out
 worn-out""".splitlines()))

negative_feelings.append(sorted("""fear
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
worried""".splitlines()))

negative_feelings.append(sorted("""pain
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
remorseful""".splitlines()))

negative_feelings.append(sorted("""sadness
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
wistful""".splitlines()))

negative_feelings.append(sorted("""tension
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
stressed-out""".splitlines()))

negative_feelings.append(sorted("""yearning
longing
nostalgic
pining""".splitlines()))

feelings['positive'] = positive_feelings
feelings['negative'] = negative_feelings

needs.append(sorted("""AUTONOMY
choice
dignity
freedom
independence
self-expression
space
spontaneity""".splitlines()))

needs.append(sorted("""CONNECTION
acceptance
affection
appreciation
authenticity
belonging
care
closeness
communication
communion
community
companionship
compassion
consideration
empathy
friendship
inclusion
inspiration
integrity
intimacy
love
mutuality
nurturing
partnership
presence
respect/self-respect
security
self-acceptance
self-care
self-connection
self-expression
shared-reality
stability
support
to know and be known
to see and be seen
trust
understanding
warmth""".splitlines()))

needs.append(sorted("""MEANING
awareness
celebration
challenge
clarity
competence
consciousness
contribution
creativity
discovery
efficiency
effectiveness
growth
integration
integrity
learning
mourning
movement
participation
perspective
presence
progress
purpose
self-expression
stimulation
understanding""".splitlines()))

needs.append(sorted("""PEACE
acceptance
balance
beauty
communion
ease
equanimity
faith
harmony
hope
order
peace-of-mind
space""".splitlines()))

needs.append(sorted("""PHYSICAL 
WELL-BEING
air
care
comfort
food
movement/exercise
rest/sleep
safety (physical)
self-care
sexual expression
shelter
touch
water""".splitlines()))

needs.append(sorted("""PLAY
adventure
excitement
fun
humor
joy
relaxation
stimulation""".splitlines()))

logger.info(str(feelings))
