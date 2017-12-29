from textwrap import dedent
from sys import exit
from random import randint, shuffle

gather = ['line']
dog_ending = 0

class Room (object):
    def __init__ (self, name, description):
        self.name = name
        self.description = description




class Busted (Room):

    busted_lines = [
        "If I could stop being so henpecked, I wouldn't lose my identity.",
        "This year we will probably decorate the Christmas tree with my balls.",
        "I wanted to be stong and independent but my wife told me otherwise.",
        "My wife doesn't really need a kid, she's got me.",
        "If I could ever get on TV, I'd advertise estrogene."
        ]
    busted_text = dedent("""
        That was enough to attract my wife's attention. She appeared a moment later
        and the rest of the weekend I spent in the cellar repairing the frigging boiler.
        """)

    def win (self):
        win_text = dedent("""
            Everything seems to be quiet and I ignite my car. Archibald looks fed and happy,
            he jumps onto the front seat and I follow him. Well, it seems for the next two days
            I'm gonna have a vacation from my usual miserable self and won't have to get back
            to this wretched life of mine. Something to look forward to!

            Yiha!
            """)
        return win_text

    def dog_ending (self):
        return the_garden.dog

    def finita (self):
        return (self.busted_lines[randint(0, len(self.busted_lines) - 1)])

#    def loved (self):
#        print ("Here's when I thought that I had married this woman for some reason.")
#        print ("Fine. To hell with this fishing. I'll stay in today.")
#        print ("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")



class Cellar (Room):

    lines_var = 0

    fall = dedent("""
    As this heavy rack fell down on me and probably broke both of my legs,
    there is something that falls from the top shelf and hits me on the head.
    Before the world around me fades to black, I see this 'something':
    it's my rod!
    """)

    taken = [
        'Ok, this is gone.',
        'Taken.',
        'Gone.',
        'Yep.',
        'Taken care of.'
        ]

    empty = []

    gather = []

    line_lines = [
        "Where the heck is my fishing line?",
        "Sheesh, I can't remember.",
        "Oh, for the lover of... Where's my line?",
        "Damn, where is this frigging line?"
        ]

    fishing_stuff = ['line', 'rod', 'hooks']
    go_toolbox = ['toolbox', 'hooks']
    go_shelves = ['shelf', 'shelves', 'rod']
    wrong_choice_list = ['Attention!', 'Toolbox or shelves?', 'What do I do now?', 'Where is my fishing stuff?']
    toolboxlist = ['hammer', 'ductape', 'wrench', 'screwdriver', 'paintbrush', 'saw']


    def wrong_choice_func(self):
        return (self.wrong_choice_list[randint(0, len(self.wrong_choice_list)-1)])

    def wrong_line_func(self):
        return (self.line_lines[randint(0, len(self.line_lines)-1)])

    def look_around(self, words):
        look_around_func_list = ['look', 'around']
        trfal = []
        word = words.split()
        for i in word:
            if i in look_around_func_list:
                trfal.append(i)

        if trfal != []:
            return "I look around trying to find something that will help me reach the top shelf. Oh! A ladder!"

    def climb_shelves(self):
        climb_end = dedent("""
        I try climbing up the shelving unit and quite predictably, I topple it over,
        oh me, fat sorry fuck. """)
        return climb_end + self.fall

    def ladder (self):
        ladder_end = dedent("""
        I try and drag the ladder closer to the shelves. I realize it is a bad idea
        only after this rotten pile o'garbage breaks under me and I fall. """)
        return  ladder_end + self.fall

    def crates(self):
        return dedent("""
        I try piling up crates to reach up to the upper shelf. And though such act makes me think
        of myself as an evolutionary dead end, I safely manage to build a small tower and see what's
        there on the top shelf.
        Aha! My fishing rod!
        """)
        #self.gather.append('rod')
        #self.shelves_2look()

    def open_toolbox(self):
        toolbox_sentence = 'I open the toolbox and I see a ' + (', a '.join(self.toolboxlist[:-1]) + ' and a ' + self.toolboxlist[-1] + '.')
        return toolbox_sentence

    def toolbox_func (self, comm):

        while self.toolboxlist != self.empty:
            split_take = comm.split()
            filtered = []
            empty = []
            for j in split_take:
                if j in self.toolboxlist:
                    filtered.append(j)

            for i in filtered:
                self.toolboxlist.remove(i)

                if len(self.toolboxlist) > 1:
                    return (dedent(
                    self.taken[randint(0, len(self.taken)-1)] + ' What\'s next: a ' + ', a '.join(self.toolboxlist[:-1]) + ' and a ' + self.toolboxlist[-1] + '.'
                    ))
                elif len(self.toolboxlist) == 1:
                    if filtered == []:
                        return "Nah, get your act together. Only " + self.toolboxlist[0] + " left."
                    return (dedent("Hm. Only " + self.toolboxlist[0] + " left."))

            if filtered == []:
                    return ('Nah, get your act together. What\'s next: a ' + ', a '.join(self.toolboxlist[:-1]) + ' and a ' + self.toolboxlist[-1] + '.')

        return ('Aha! Just as I thought! A tiny bag of hooks underneath all this useless garbage.')



class Kitchen (Room):


    choice_kitchen = ['look', 'around', 'yes', 'food', 'look around']
    neg_choice_kitchen = ['no', '']

    last_minute = dedent("""
    Last minute, I think about Archibald, my dog. This old idiot lives in the
    garden and he won't be able to stay silent when he sees me and definitely
    he won't let me go away without having to alert the whole neighborhood.

    So, I need something to seal his mouth with.

    I open the fridge and find some jerky beef. That should do.
    """)

    leave_kitchen = dedent("""
    Anyway, time I was on my way. There is a choice, however.
    I can try sneaking through the living room downstairs or try
    my luck in the bedroom upstairs.
    """)



class Living_Room (Room):
    criminals = [
    "Zach", "Edgar", "Colin", "Gorden", "Milo", "Matthew",
    "Marcus", "Nathan", "Noel", "Patrick", "Hugh"
    ]

    yeses = ['ok', 'Ok', 'OK', 'yes', 'yeah', 'yea', 'sure']
    noes = ['no', 'nope', 'nada', 'never', 'not']

    irritation = [
        "'Will you help me, yes or no?'",
        "'Dad, dammit!'",
        "'Come on!'",
        "'Like, really'?",
        "'Are you for frigging real?'",
        "'Do you WANT me to call mum?'"
        ]
    shuffle(criminals)

    man1 = criminals[0]
    man2 = criminals[1]
    man3 = criminals[2]
    man4 = criminals[3]
    man5 = criminals[4]
    killer = man3
    victim = man2

    def daughter_irritation(self):
        return (self.irritation[randint(0, len(self.irritation) - 1)])

    def puzzle_text(self):
        return dedent("""
        'Okay, then.
        There's a group of five men. One of them has killed another.
        Here's what we know.'""")

    puzzle_list = dedent(f"""
        {man1} ran the New York marathon yesterday with one of the not guilty.
        {man2} considered himself a farmer before moving to the city.
        {man3} is a computer genius and he is going to assemble a new computer for {man4} next week.
        The killer's leg was amputated a few days ago.
        {man4} met {man5} half a year ago.
        {man5} has not been seen since the murder.
        {man1} used to drink a lot.
        {man4} and {man3} have been assembling their computers together lately.
        The killer is {man5}'s brother, they grew up together in Seattle.
    """)

    def puzzle(self):
        splits = self.puzzle_list.split(".")
        puzzle_result = []
        s = '\n'
        shuffle(splits)
        for i in splits:
            puzzle_result.append(i)                                      # IDEA: wrong return, fix!! did i fix that?
        return puzzle_result

    brat = "'Okay, then. Muuuuum! Dad is going somewhere!'"



class Bedroom (Room):

    opts = dedent("""
        !   shout at her<br>
        _   keep silence<br>
        *   cuss<br>
        ?   ask a question<br>
        y   beg her<br>
        x   confess<br>
        ♥   love her<br>
        """)
    opts_dict = {
        "!": "shout at her",
        "_": "keep silence",
        "*": "cuss",
        "?": "ask a question",
        "y": "beg her",
        "x": "confess",
        "♥": "love her",
    }


    opts1 = "What now?  ! _ * ? y x ♥"


    wifes_questions = [
        "'How are you feeling'?",
        "'How is the repair going?'",
        "'Watcha doin\' up \'ere?'",
        "'How long is it gonna take?'",
        "'Are you OK?'",
        "'Aren\'t you tired yet?'",
        "'How\'s my mum there downstairs?'"
        ]

    questions = [
        "'Why do you ask?'",
        "'Do you even trust me?'",
        "'Weren\'t we in this together?'",
        "'Weren\'t you going to help me?'",
        "'You know I\'ve been in that cellar for a long time, don\'t you?'",
        "'Anyway, how are things up here?'",
        "'How you seen our dog today?'",
        ]

    questions_reactions = [
        "'Will you please just start answering my questions?'",
        "'Oh, this evasive manner of yours!'",
        "'Are you even listening to me?'",
        "'Are you for real?'",
        "'Any chance you\'ll start talking like a sane person?'",
        "'Enough with the questions!'",
        "'Are you mentally intact?'"
        ]

    yelling = [
        "'Oh, for the love of... will you stop nagging me, woman? What have I ever done to you?'",
        "'Sweet mary, Mother of... Stop riding my back, I\'m not your horse!'",
        "'Gracious goodness, woman, get your act together! You don\'t own me!'"
        ]

    yelling_reactions = [
        """'Oh you did NOT just say that!' She storms across the room and slaps me in the face.
        It takes her good three minutes to calm down afterwards.""",
        """'You better watch your mouth, because it\'s running!'
        She throws a pillow at me, then grabs a vase and smashes it against the floor.""",
        """'Oh boy, you say this to me after all these years together?'
        She opens a drawer, grabs a pair of tailoring scissors and rips the blanket open."""
        ]

    silence = [
        "Ok, I'm not answering anything.",
        "Let all the guerillas in the world be proud of me.",
        "Not a word.",
        "I can only win this fight, if I don't say anything.",
        "Swallowed my tongue.",
        "Damn, silence is not that easy.",
        "It's like being tortured in CIA catacombs.",
        "I've lived with her for ages, I can stand her stare."
        ]

    silence_reactions = [
        "'Strong, silent type, huh? Well-well.'",
        "'Bitten off your tongue?'",
        "'You there?'",
        "'Are you deaf, mute or both?'",
        "'Listen, you just frighten me sometimes.'",
        "'You know I\'m talking to you, right?'",
        "'Well, that\'s awkward.'",
        "'I\'m not always sure you can speak human.'"
        ]

    cussing = [
        "'Bloody hell, whatever have I done to deserve you of all people!'",
        "'Frigging fuck, woman, why is it always like this with you?'"
        ]

    cussing_reactions = [
        """'Sweet Mother of language, how dare you kiss me with that mouth?',
        she closes her ears with her palms and shivers.""",
        """'Oh me, stupid cow, my mum warned me about you, and she was right!',
        she sobs and bursts into tears."""
        ]

    begging = [
        "'Honey, honestly, I'm so tired with that goddamn boiler, I need a break. Besides, the Simpsons are on!'",
        "'Sweety, the weekend is long, I'll finish it later. Do we have any beer left?'",
        "'Sweetheart, do you remember how I took us to the Chinitooga lake? How about we do this again?'",
        "'My love, how about we watch the Notebook today? Order some pizza?'"
        ]

    begging_reactions = [
        "'Oh no, don't go all sugary on me, this will not work again! No sweets until after it's done!'",
        "'That's a really, REALLY nice try, but no, be a man.'",
        "'Nah-nah, I've known you long enough not to succumb to it. Away with it!'",
        "'Just nope.'"
        ]

    confessing = [
        "'To be honest with you, love, I' don't wanna do this boiler at all. I'd go fishing instead.'",
        "'There's one thing I have to confess. I don't wanna do the boiler, love."
        ]

    confessing_reactions = [
        "'Oh god, I knew you never loved me!'",
        "'How about no?'"
        ]

    love = [
        "'Have I told you that I love you?'",
        "'Hey, I love you.'",
        "'I love you.'"
        ]

    love_reactions = [
        "She blushes.",
        "She does not expect that.",
        "She's suprised."
        ]

    inputs = {
        '!': yelling,
        '*': cussing,
        '_': silence,
        '?': questions,
        'y': begging,
        'x': confessing,
        '♥': love
        }

    reactions = {
        '!': yelling_reactions,
        '*': cussing_reactions,
        '_': silence_reactions,
        '?': questions_reactions,
        'y': begging_reactions,
        'x': confessing_reactions,
        '♥': love_reactions,
    }

    counts = {
        '!': 3,
        '*': 4,
        '_': 1,
        '?': 0,
        'y': 2,
        'x': 9,
        '♥': 1
    }
    emptied = []

    count = 0
    love_count = 0
    conversation = []

    def wifes_questions_func (self):
        her_question = self.wifes_questions.pop(randint(0, len(self.wifes_questions) - 1))
        self.conversation.append(her_question)
        return her_question

    def enter (self, answer):
        bedroom_win = dedent("""
        Surprising as it is, she suddenly gets tired of me and storms out of the room.
        I am free! Phew, who coulda thought!
        Next step - the hall.
        """)

        while self.count <= 7:

            if self.questions == []:
                return bedroom_win

            elif self.love_count == 3:
                return "L'amore! Busted!"
            elif answer in self.inputs.keys():

                lis = self.inputs.get(answer)
                sil = self.reactions.get(answer)
                n = self.counts.get(answer)
                if answer == '♥':
                    self.love_count += n
                else:
                    self.count += n
                self.conversation.append(lis.pop(randint(0, len(lis) - 1)))
                self.conversation.append(sil.pop(randint(0, len(sil) - 1)))
                return self.conversation
            else:
                return "think!"
        else:
            return [
            "That obviously was enough for her.",
            "The next two hours I spent being yelled at."
            ]



class The_Hall (Room):

    yeses = ['ok', 'Ok', 'OK', 'yes', 'yeah', 'yea', 'sure']
    noes = ['no', 'nope', 'nada', 'never', 'not']

    cat_refuse = dedent("""
    The bastard didn't lie.
    He meowed so loudly as if his ancient namesake had stepped on his tail.
    """)

    cat_win = dedent("The Sphynx smiles and lets me through.")
    cat_lose = dedent("""
    The bastard didn't like that.
    He meowed so loudly as if his ancient namesake had stepped on his tail.
    """)
    def hall_puzzle_func(self):
        return (dedent("""
            A boy and a girl are talking.
            "I am a boy" - said the child with black hair.
            "I am a girl" - said the child with white hair.
            At least one of them lied. Which one?
            """))



class The_Garden (Room):

    colors = {
        'cyan': {'blue', 'green'},
        'magenta': {'blue', 'red'},
        'yellow': {'red', 'green'},
        'white1':{'cyan','red'},
        'white2':{'blue', 'yellow'},
        'white3':{'magenta', 'green'},
        'orange': {'yellow', 'red'},
        'pink': {'white', 'magenta'}


    }

    black = dedent("""
    Whoopsie. This black is blacker than the blackest black times infinity.
    I hardly can change THIS color to anything.
    """)

    success = [
        "Aha",
        "Okey-doke",
        "Yups",
        "Super-dupes",
        "Ooo-lala",
        "Well-well"
    ]
    passed_garden = 0
    buckets = ['blue', 'green', 'black', 'red']
    needed = []
    bucket_empty = []

    dawg = "Only did I think that I was done, something had to ruin my day."
    dog = dedent("""
        Here's when Archibald The Dawg enters the game. The old fucker runs directly at me
        barking as if it's the end of times.

        I totally forgot to feed him.
        """)

    def misunderstood(self):
        misunderstood_list = [
        "Huh?", "What's that?", "Let's see - what do I have here?",
        "Time to cause some damage, bitch!", "What do I do?", "Okay, let's focus."
        ]
        return (misunderstood_list[randint(0, len(misunderstood_list) - 1)])

    def taking_colors(self, color):
        if color == 'black':
            color_black_exit = f"{self.black}"
            dog_ending = 1
            return color_black_exit + self.dog

        elif color in self.buckets and color != 'black':
            self.bucket_empty.append(color)
            return f"Ok, here goes {color}."

        else:
            return "Sheesh!"

    def empty_baskets(self):
        del self.bucket_empty[:]

    def check_buckets (self, buckets):
        if 'white' in buckets and 'orange' in buckets:
            self.passed_garden = 1

    def mixing_colors (self):

        got_this  = "Darn, I've already got this."
        start_anew = dedent("""
        Well, I'm gonna put this aside for now and start mixing anew.
        What color shall come next?
        """)

        for key in self.colors:
            if set(self.bucket_empty) == self.colors[key]:
                if key in self.buckets:
                    #empty1 = list(set(self.bucket_empty))
                    del self.bucket_empty[:]
                    return f"{got_this} I've got " + ", ".join(self.buckets[:len(self.buckets) - 1]) + " and " + self.buckets[-1] + f". \n{start_anew}"
                else:
                    if key in ['white1', 'white2', 'white3']:
                        self.buckets.append('white')
                        self.needed.append('white')
                        del self.bucket_empty[:]
                        return (self.success[randint(0, len(self.success) - 1)] + f", the paint in my bucket is now white. \n{start_anew}")
                    else:
                        self.buckets.append(key)
                        if key == 'orange':
                            self.needed.append('orange')
                        del self.bucket_empty[:]
                        return (self.success[randint(0, len(self.success) - 1)] + f", the paint in my bucket is now {key}. \n{start_anew}")
            elif len(set(self.bucket_empty)) == 1:
                del self.bucket_empty[:]
                return "Well, I didn't mix much, did I? Let's try again."
        else:
            shit1, shit2 = self.bucket_empty[0], self.bucket_empty[1]
            del self.bucket_empty[:]
            return f"{shit1.capitalize()} and {shit2}? What in fuck's grace is this color? Lemme try again."

    def insuccessful (self, f):
        if f == None:
            shit1, shit2 = self.bucket_empty[0], self.bucket_empty[1]
            del self.bucket_empty[:]
            return f"{shit1.capitalize()} and {shit2}? What in fuck's grace is this color? Lemme try again."
        else:
            return f



start = Room ("So long and thanks for the fish",
"""
I want to escape from my house to go fishing. My wife wants to stop me
and have me repairing the boiler in the cellar. That's where I am now.
It's quiet upstairs, so if there's ever a moment to flee, it's now.
On my way to salvation, I have to pass the kitchen, the living room
(or the bedroom upstairs), the hall and the garden. I have to do this
without raising my wife's alarm or I'll end up in the cellar.
""")

the_cellar = Cellar('The Cellar',
"""
So, ok. Before moving out, I need to get my stuff. First of all,
I need my fishing rod, some line and some hooks. I vaguely remember
seeing hooks in the toolbox and the rod — in the shelves.<br><br>
But where the heck did I leave the line?
""")

the_toolbox = Cellar('The Cellar',
"""
Alrighty then, let's try to find the hooks. Does my memory serve?
""")

the_shelves = Cellar('The Cellar',
"""
Sheesh, I wish I knew for sure where my fishing rod is.
I am looking at the four-level shelving unit. There are buckets and crates
on the lower shelf, some canisters above that, a bunch of bowling pins
(I mean - whaaat?) on the third shelf, and the top one is too high above and
I cannot see it.
""")

lines = Cellar('The Cellar',
"Ha! Just remembered. I left the line in the kitchen.")

the_kitchen = Kitchen("The Kitchen",
"""
I sneak into the kitchen. Excellent, all quiet, no one around.<br><br>
I open the upper drawer of one of the cupboards and aha! there it is,
my line. I grab it and hurry away.<br><br>

At the door, however, I stop for a moment and think: maybe I need
something else, while I'm in the kitchen?
""")

the_living_room = Living_Room("The Living Room",
"""
I'm in the living room aaaand... I'm busted. My daughter is lying
on the couch and reading a book.<br>
'Hey old man, I need you,' she says, somewhat impatiently.<br>
'Well, I'm not available, am I?'<br>
'Why? Where are you going?'<br>
'That's my business.'<br>
'And mom's, right?'<br><br>

Damn, I'm just not good with kids.<br><br>

'Alrighty then, whatcha need?' Let's get this over with and I'll be on my way.<br>
'I'm reading this book here,' the little brat is waving with the piece of junk
she's holding in her hand, 'And there's a puzzle I can't solve. And I really need
it fooor... my school project. Will you help me?'
""")

the_bedroom = Bedroom("The Bedroom",
"""
I sneak into our bedroom upstairs and... geez, that's a mistake.<br><br>
'Hi honey, what's up?', my wife is changing sheets on our bed
and looks quite peaceful. How do I not ruin that?
""")

the_hall = The_Hall("The Hall",
"""
Surprising as it is, she suddenly gets tired of me and storms out of the room.<br>
I am free! Phew, who coulda thought!<br>
Next step — the hall.<br><br>

Okay, <i>that</i> I did not expect. As I was two steps away from the front door,
I saw our cat, Sphynx, sitting on the cupboard and looking at me.<br><br>

"The hell are you looking at?", I asked.<br>
"A criminal at large", he said.<br><br>

Well, as I said, I did not expect that.<br><br>

"Okay, then, if you riddle me this, I'll let you go, if you fail, I'll scream
so loud, the female human you jointly hold me in captivity with will come down
and bust you during your attempt to escape." The creature licked his fangs and smiled.<br>

"How come you can speak?" I finally regained my ability to do what he seemed
perfectly comfortable doing.<br>
"A feline should have his own ways." Motherbleeper yawned lazily.
""")

the_garden = The_Garden("The Garden",
"""
I'm in the garden. The end is nigh. I am looking around and see a few buckets
of paint in my garage.<br><br>

Damn.<br><br>

I wanted to colour my boat! My last trip, I was fined as my boat was very dark
and shabby and only visible from a very short distance. So, they gave me
instructions on how to paint it.<br><br>

I approach the buckets and see that there are four of them with paint and
several empty ones. For my paint job I need orange and white, and in my garage,
I have red, black, blue and green.<br><br>
Tiddly-doo, what can I do? Mix the colours, perhaps?<br>
What colour should I take first?<br>
""")

busted = Busted("Whoopsie!", Busted.busted_text)

win = Busted("Yaaas!", "Finally!")

love = Busted("O'lala!",
"""Here's when I thought that I had married this woman for some reason.""")

dawgs = Busted('O-oh.', The_Garden.dawg)

wife_busted = Busted('Oh crap.',
"""
Why would possibly think I was stronger than her?<br>
Of course, I couldn't talk my way out of it!<br>
""")
