# See what words are common between Emerson and Shakespeare.

emerson = '''One man's justice is another's injustice; one man's beauty another's
ugliness; one man's wisdom another's folly; as one beholds the same
objects from a higher point of view. One man thinks justice consists
in paying debts, and has no measure in his abhorrence of another who
is very remiss in this duty and makes the creditor wait tediously. But
that second man has his own way of looking at things; asks himself
which debt must I pay first, the debt to the rich, or the debt to the
poor? the debt of money, or the debt of thought to mankind, of genius
to nature? For you, O broker, there is no other principle but
arithmetic. For me, commerce is of trivial import; love, faith, truth
of character, the aspiration of man, these are sacred; nor can I
detach one duty, like you, from all other duties, and concentrate my
forces mechanically on the payment of moneys. Let me live onward; you
shall find that, though slower, the progress of my character will
liquidate all these debts without injustice to higher claims. If a
man should dedicate himself to the payment of notes, would not this be
injustice? Owes he no debt but money? And are all claims on him to be
postponed to a landlord's or a banker's?'''

shakespeare = '''Ham. I will tell you why; so shall my anticipation
preuent your discouery of your secricie to the King and
Queene: moult no feather, I haue of late, but wherefore
I know not, lost all my mirth, forgone all custome of exercise;
and indeed, it goes so heauenly with my disposition;
that this goodly frame the Earth, seemes to me a sterrill
Promontory; this most excellent Canopy the Ayre,
look you, this braue ore-hanging, this Maiesticall Roofe,
fretted with golden fire: why, it appeares no other thing
to mee, then a foule and pestilent congregation of vapours.
What a piece of worke is a man! how Noble in
Reason? how infinite in faculty? in forme and mouing
how expresse and admirable? in Action, how like an Angel?
in apprehension, how like a God? the beauty of the
world, the Parragon of Animals; and yet to me, what is
this Quintessence of Dust? Man delights not me; no,
nor Woman neither; though by your smiling you seeme
to say so'''

print('-' * 100)

set_emerson = set(emerson)
set_shakespeare = set(shakespeare)
print(set_emerson)
print(set_shakespeare)
print(type(set_emerson))
print(type(set_shakespeare))

print('-' * 100)

split_emerson = emerson.split()
split_shakespeare = shakespeare.split()
print(split_emerson)
print(split_shakespeare)
print(type(split_emerson))
print(type(split_shakespeare))

print('-' * 100)

set_split_emerson = set(split_emerson)
set_split_shakespeare = set(split_shakespeare)
print(set_split_emerson)
print(set_split_shakespeare)
print(type(set_split_emerson))
print(type(set_split_shakespeare))

print('-' * 100)

print('These words appear in both Emerson and Shakespeare:', set_split_emerson & set_split_shakespeare)
print('These words are unique to each author:', set_split_emerson ^ set_split_shakespeare)

print('-' * 100)
