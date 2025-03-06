import os
import asyncio
import discord
from colorama import init, Fore, Style
import time
from datetime import datetime
import pytz  # For handling time zones
import random  # For random message selection

init(autoreset=True)

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
black = Fore.LIGHTBLACK_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL
magenta = Fore.LIGHTMAGENTA_EX

def get_timestamp():
    # Menggunakan zona waktu Asia/Jakarta (WIB)
    wib = pytz.timezone('Asia/Jakarta')
    now = datetime.now(wib)
    return f"{blue}[{now.strftime('%H:%M:%S')}]{reset}"


def log_info(message):
    print(f"{get_timestamp()} {white}INFO{reset}    | {message}")

def log_success(message):
    print(f"{get_timestamp()} {green}SUCCESS{reset} | {message}")

def log_warning(message):
    print(f"{get_timestamp()} {yellow}WARNING{reset} | {message}")

def log_error(message):
    print(f"{get_timestamp()} {red}ERROR{reset}   | {message}")

# Banner
def print_banner():
    print(f"\n{blue}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰{reset}")
    print(f"{white}      Auto Chat Discord      {reset}")
    print(f"{yellow}         by: Synthinks          {reset}")
    print(f"{blue}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰{reset}\n")

print_banner()

def load_tokens():
    tokens = []
    try:
        with open('token.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    tokens.append(line.strip())
            if tokens:
                log_success(f"Successfully loaded {len(tokens)} tokens from token.txt")
            return tokens
    except FileNotFoundError:
        log_error("File token.txt not found!")
        log_info("Create a token.txt file with the format:")
        print(f"{yellow}TOKEN1{reset}")
        print(f"{yellow}TOKEN2{reset}")
        print(f"{yellow}TOKEN3{reset}")
        exit(1)

class AccountConfig:
    def __init__(self, token, channel_id, message_count, message_delay, delete_mode=True):
        self.token = token
        self.channel_id = channel_id
        self.message_count = message_count
        self.message_delay = message_delay
        self.delete_mode = delete_mode

mainMessages = [
	'Just checking in!',
    'Did anyone see the latest episode?',
    'What everyone up to today?',
    'Cant believe its already this late!',
    'Just finished my tasks, finally!',
    'This weather is something else...',
    'Anyone working on something interesting?',
    'Good morning, everyone!',
    'Time for a quick break, anyone else?',
    'Back to the grind.',
    'Anyone have any tips for leveling up faster?',
    'Just got back, what did I miss?',
    'Feeling motivated today!',
    'Lol, thats hilarious!',
    'Totally agree with you.',
    'Thinking about getting some coffee, brb.',
    'Anyone here into coding?',
    'Oh wow, didnt expect that!',
    'Taking things one step at a time.',
    'Almost there!',
    'Lets keep pushing forward!',
    'Just chilling here for a bit.',
    'Anyone have any weekend plans?',
    'Anyone tried that new game yet?',
    'Haha, I know right?',
    'Feels like time is flying by.',
    'Well, thats a surprise!',
    'Just here to chat and relax.',
    'Anyone else feeling productive today?',
    'Im here to keep you all company!',
    'Hope everyones doing well!',
    'Taking a quick break, needed it.',
    'Lets keep this chat alive!',
    'Anyone else here love a good challenge?',
    'Feels good to be part of this community.',
    'Enjoying the vibe here!',
    'Thinking of learning something new.',
    'Random question: Cats or dogs?',
    'Its always nice to chat with you all.',
    'That sounds awesome!',
    'Haha, love the energy here!',
    'Alright, time to focus!',
    'Whats everyone watching these days?',
    'Just a casual hello!',
    'Oops, wrong chat haha.',
    'Wondering if anyone has advice on leveling?',
    'Anyone working late tonight?',
    'Hey, Im back!',
    'Hope I didnt miss too much.',
    'Alright, lets do this!',
    'Trying to stay motivated!',
    'Hows everyone feeling today?',
    'Good vibes only!',
    'Just saw something really cool!',
    'Hey everyone, how`s it going?',
    'Just checking in!',
    'Did anyone see the latest episode?',
    'What`s everyone up to today?',
    'Can`t believe it`s already this late!',
    'Just finished my tasks, finally!',
    'This weather is something else...',
    'Anyone working on something interesting?',
    'Good morning, everyone!',
    'Time for a quick break, anyone else?',
    'Back to the grind.',
    'Anyone have any tips for leveling up faster?',
    'Just got back, what did I miss?',
    'Feeling motivated today!',
    'Lol, that`s hilarious!',
    'Totally agree with you.',
    'Thinking about getting some coffee, brb.',
    'Anyone here into coding?',
    'Oh wow, didn`t expect that!',
    'Taking things one step at a time.',
    'Almost there!',
    'Let`s keep pushing forward!',
    'Just chilling here for a bit.',
    'Anyone have any weekend plans?',
    'Anyone tried that new game yet?',
    'Need some music recommendations!',
    'What’s a good movie to watch tonight?',
    'Feeling kinda hungry, what should I eat?',
    'Any book lovers here?',
    'Can’t wait for the weekend!',
    'Hope everyone is having a great day!',
    'Game night, anyone?',
    'Anyone else feeling sleepy?',
    'Trying to stay productive!',
    'Just vibing right now.',
    'Music makes everything better!',
    'I need some new anime recommendations.',
    'What’s a fun hobby to start?',
    'Anyone playing something interesting?',
    'How’s your day going?',
    'Just taking a break.',
    'What’s the best snack while gaming?',
    'Feeling nostalgic today.',
    'Anyone into photography?',
    'Trying to learn something new.',
    'Motivation level: 100%',
    'Finally done with work, time to relax!',
    'Any good memes today?',
    'Who else loves late-night chats?',
    'I could use a nap right now.',
    'What`s a good show to binge?',
    'Thinking about starting a new project.',
    'Anyone need help with anything?',
    'Let’s share some fun facts!',
    'Anyone here into crypto?',
    'Just got a new keyboard, love it!',
    'Feeling lucky today!',
    'Who else loves a good mystery?',
    'Just testing something real quick.',
    'Let`s make today productive!',
    'Anyone into fitness?',
    'Time flies so fast!',
    'Trying to stay focused, but it`s hard!',
    'What`s the best way to stay motivated?',
    'Feeling a bit lazy today.',
    'What’s everyone listening to?',
    'Late-night coding session, anyone?',
    'Dreaming about a vacation right now.',
    'Just got some new gear!',
    'What’s your go-to comfort food?',
    'Chilling with some good music.',
    'The weekend can`t come soon enough!',
    'Who else loves a good challenge?',
    'Let’s do something fun!',
    'Thinking about getting a pet.',
    'Anyone tried cooking something new?',
    'What’s a skill you want to learn?',
    'Just trying to relax for a bit.',
    'What’s your dream job?',
    'Who else is excited for the holidays?',
    'Any good podcast recommendations?',
    'Feeling like today is a good day!',
    'Anyone up for a quick game?',
    'Who else loves coffee?',
    'Midnight snacks are the best!',
    'What’s your favorite kind of dessert?',
    'I need some motivation!',
    'Hyped for the next update!',
    'Anyone else obsessed with tech?',
    'Just finished a great book!',
    'What’s a weird fun fact you know?',
    'Anyone else loves a good thriller?',
    'Taking a deep breath and relaxing.',
    'What’s the best way to unwind?',
    'Can`t decide what to do next.',
    'Feeling creative today!',
    'Anyone up for a challenge?',
    'Who else loves learning new things?',
    'Trying out a new routine.',
    'Just checking in, hope you`re all good!',
    'What`s your favorite season?',
    'Nothing beats a good conversation!',
    'Looking forward to the weekend fun!',
        'Grinding XP, who’s with me?',
    'Need just a bit more XP to level up!',
    'Almost there, next level coming soon!',
    'Daily check-in for that sweet XP!',
    'Who else is farming XP right now?',
    'Time to drop some messages and level up!',
    'Crypto chat and XP grind, best combo!',
    'What’s the fastest way to gain XP here?',
    'Leveling up feels so satisfying!',
    'Let’s keep the chat active and earn XP!',
    'Daily quest: chat more, earn more XP!',
    'Anyone else tracking their level progress?',
    'Rank up grind never stops!',
    'More messages, more levels!',
    'Chat more, earn more, simple as that!',
    'Consistency is key to leveling up!',
    'Next rank is calling, let’s go!',
    'Who’s the highest level here?',
    'Fastest way to rank up? Keep chatting!',
    'Crypto discussions = free XP!',
    'Active members always stay on top!',
    'Leaderboard goals, let’s get it!',
    'Dropping by for that daily XP boost!',
    'Who’s aiming for top 10 in the server?',
    'Gotta stay active to stay relevant!',
    'Nothing beats a good chat and XP grind!',
    'Engage, interact, and rank up!',
    'Who just ranked up? Congrats!',
    'Another message, another step closer!',
    'Crypto alpha + XP gains = perfect combo!',
    'Grind now, flex later!',
    'Every message counts toward the next rank!',
    'Stay engaged and watch your level rise!',
    'Active users get the best rewards!',
    'Who else is farming engagement?',
    'Daily XP goal: achieved!',
    'Leaderboard warriors, where you at?',
    'Rank climbing never gets old!',
    'Every chat brings me closer to my goal!',
    'Crypto talk + Discord grind = win-win!',
    'XP farmers unite!',
    'Let’s keep this server alive and thriving!',
    'Who’s the next one to hit a milestone?',
    'Active chats keep the community strong!',
    'Crypto and Discord leveling, best grind ever!',
    'Server ranks = digital street cred!',
    'Dropping alpha and stacking XP!',
    'Next milestone coming up soon!',
    'Climbing ranks one message at a time!',
    'Stay consistent, stay engaged, stay leveling!',
    'Never underestimate the power of engagement!',
    'One step closer to leaderboard domination!',
    'Crypto knowledge + XP grinding = unstoppable!',
    'Chasing XP like I chase gains!',
    'Who else is farming reactions for XP?',
    'Another message, another point!',
    'Community building = XP stacking!',
    'XP doesn’t sleep, so neither do I!',
    'Almost hitting my next rank, let’s go!',
    'Daily grind for XP never stops!',
    'Crypto insights and leveling up, perfect mix!',
    'Active users always win!',
    'Who’s dropping the best alpha today?',
    'One more level and I’m flexing my new rank!',
    'Stacking XP like I stack my bags!',
    'Hard work in chat pays off!',
    'XP farm is real today!',
    'Crypto degens and XP grinders, rise up!',
    'Grinding levels like it’s a bull run!',
    'Which rank are you aiming for?',
    'Rank 10 or bust!',
    'Let’s hit that next milestone together!',
    'Chat farming is the way!',
    'Every message matters for XP gains!',
    'Dropping alpha and collecting XP!',
    'Leveling up is a marathon, not a sprint!',
    'Who just hit the top 5?',
    'Time to overtake someone on the leaderboard!',
    'Crypto alpha + chat XP = big wins!',
    'XP hunting mode activated!',
    'Who’s aiming for that legendary rank?',
    'Every reply is a step closer to the top!',
    'Crypto talk + active chat = max rewards!',
    'One message closer to the goal!',
    'Server engagement is the name of the game!',
    'Daily streak for XP is going strong!',
    'Grind now, rank up later!',
    'Engagement is the key to community success!',
    'Leaderboard warriors, let’s rise!',
    'Who’s the next to flex a new rank?',
    'Crypto chats keep the server alive!',
    'Time to push for that next rank!',
    'Let’s see who’s the most active today!',
    'The more you chat, the faster you rank up!',
    'Crypto grinding and leveling, let’s go!',
    'Who else is keeping their streak alive?',
    'Top 10 leaderboard spot, here I come!',
    'Keep the grind going, rewards will come!',
        'Back to the grind, need that XP!',
    'Who’s the top grinder here?',
    'Crypto talks + leveling up = best combo!',
    'Dropping knowledge and stacking XP!',
    'Time to climb that leaderboard!',
    'XP grind never stops!',
    'Who else is chasing the next rank?',
    'Every message brings me closer to my goal!',
    'Level up game strong!',
    'Crypto chat is the best way to farm XP!',
    'Grind now, flex later!',
    'Who’s ranking up today?',
    'Daily XP mission activated!',
    'Next milestone coming up!',
    'Never stop chatting, never stop leveling!',
    'Who’s leading the XP race?',
    'The grind for top 10 is real!',
    'XP farming while talking crypto, perfect match!',
    'Another step closer to the top!',
    'Leaderboard goal: top 5!',
    'Crypto alpha + active chat = max rewards!',
    'XP is just free if you keep engaging!',
    'Gotta stay active to stay relevant!',
    'Who else is stacking levels today?',
    'Engagement = XP = rewards!',
    'Consistency is the key to leveling up!',
    'Who’s pushing for the next rank?',
    'Crypto degen and XP grinder in action!',
    'Server engagement pays off!',
    'No breaks, only ranks!',
    'XP gains don’t stop!',
    'Time to earn some free XP!',
    'Who else is climbing the leaderboard?',
    'The more you chat, the higher you rank!',
    'Crypto fam, let’s grind this XP!',
    'Almost hitting my next level!',
    'Chatting is the best way to farm XP!',
    'XP stacking mode activated!',
    'Pushing for that next milestone!',
    'Crypto convos = endless XP!',
    'Keep talking, keep ranking up!',
    'Top grinders, where you at?',
    'Daily XP farming session!',
    'Another day, another level up!',
    'How many levels did you gain today?',
    'Crypto talks keeping this chat alive!',
    'Engage, interact, and earn rewards!',
    'Grinding levels like it’s a bull market!',
    'Every message matters!',
    'Who’s flexing their new rank today?',
    'Top 10 or nothing!',
    'Chat XP is the easiest grind!',
    'Crypto chats + XP stacking = perfect day!',
    'This chat is the best place to farm XP!',
    'Anyone else farming levels right now?',
    'Leaderboard chase is on!',
    'More engagement = more XP!',
    'Gotta secure my top spot!',
    'Crypto fam, let’s keep this chat alive!',
    'Next rank coming soon!',
    'I see you all grinding, respect!',
    'Almost hit my next milestone!',
    'Who’s leading the XP charge?',
    'Leveling up faster than BTC pumps!',
    'Daily check-in for the XP boost!',
    'Anyone got XP farming tips?',
    'Crypto + Discord = infinite XP!',
    'Staying consistent with the grind!',
    'Crypto discussions keeping the XP flowing!',
    'Need just a few more messages!',
    'Every chat takes me one step closer!',
    'Server OGs always stay on top!',
    'Crypto education + XP gains, let’s go!',
    'Grinding XP like I grind charts!',
    'Crypto insights and leveling up together!',
    'Server engagement is the key!',
    'Who’s gonna hit the next rank first?',
    'Who else is keeping the chat alive?',
    'Active members always rank higher!',
    'Crypto degen talk = free XP!',
    'Chatting and leveling up, the best routine!',
    'Pushing for that leaderboard flex!',
    'Every reply = free XP!',
    'Crypto leveling strategy: stay active!',
    'Can’t stop, won’t stop leveling!',
    'Daily XP target: almost reached!',
    'Chat XP grind > any other grind!',
    'More messages, more XP!',
    'XP farming on autopilot!',
    'Crypto and Discord leveling, best grind ever!',
    'Server engagement warriors, where you at?',
    'XP stacking, one message at a time!',
    'Crypto market updates + XP gains!',
    'Another message closer to top rank!',
    'Nothing beats an active community!',
    'Daily XP streak still alive!',
    'Anyone else grinding for XP today?',
    'Crypto discussions keep the levels coming!',
    'Leaderboard competition is heating up!',
    'Crypto + community = unstoppable XP!',
    'Next level loading…',
    'Chat and chill while stacking XP!',
    'Who else loves ranking up?',
    'One message away from the next milestone!',
    'Crypto fam, let’s keep this energy going!',
        'When in doubt, zoom out!',
    'Buy the dip or cry later!',
    'Crypto is easy, they said...',
    'Anyone else checking charts every 5 minutes?',
    'Crypto is just legalized gambling, change my mind!',
    'I don’t have diamond hands, I have titanium hands!',
    'One day we make it, right?',
    'Bitcoin fixes this!',
    'Waiting for the bull run like…',
    'When Lambo? When Moon?',
    'Hold on, let me check my portfolio... never mind.',
    'Crypto traders don’t sleep, we just refresh charts!',
    'If you love crypto, you must love volatility!',
    'That moment when you buy the top and sell the bottom.',
    'Crypto makes millionaires… and then takes it back!',
    'How to make $1M in crypto? Start with $10M!',
    'I trust my ledger more than my best friend!',
    'Gas fees are just a donation to the blockchain gods!',
    'Degen life chose me, I didn’t choose it!',
    '99% down is just a dip, right?',
    'Remember, not your keys, not your coins!',
    'Crypto traders have two emotions: euphoria and depression!',
    'Why work 9-5 when I can lose money 24/7?',
    'WAGMI… hopefully.',
    'Bear market? More like build market!',
    'Stablecoins are my only stable relationship!',
    'Crypto is the only place where 10% gains feel slow!',
    'Trust the process, not the price!',
    '“This time it’s different” - said every bag holder!',
    'Binance or bankruptcy?',
    'What’s the next 100x gem?',
    'DYOR or RIP!',
    'Crypto is like a rollercoaster, but with no seatbelt!',
    'Sending crypto to the wrong address is the modern heartbreak!',
    'My portfolio is more volatile than my mood!',
    'The market always finds new ways to surprise us!',
    'Crypto taxes? Never heard of them!',
    'Who else feels bullish today?',
    'Bear market = discount season!',
    'Crypto moves fast, blink and you miss it!',
    'Haters will say crypto is a scam!',
    'Did you buy the dip or is the dip buying you?',
    'GM to everyone except paper hands!',
    'Crypto is the only market where -50% is “normal”!',
    'Waking up to red charts is the worst feeling!',
    'If trading was easy, everyone would be rich!',
    'Crypto and coffee, the perfect morning routine!',
    'Satoshi is watching us!',
    'Elon tweets, market reacts!',
    'No risk, no reward!',
    'Crypto = patience + diamond hands!',
    'One transaction and my gas fees are gone!',
    'I trade, therefore I exist!',
    'Crypto trading is my cardio!',
    'Memecoins are the true test of patience!',
    'Bull market makes everyone a genius!',
    'Crypto, the only place where “soon” means never!',
    'Crypto winter = opportunity!',
    'Airdrop season is the best season!',
    'Waiting for my airdrop like a paycheck!',
    'Altcoins are just Bitcoin’s side characters!',
    'If crypto was easy, everyone would be rich!',
    'Never invest more than you can afford to cry about!',
    'Crypto traders don’t take weekends off!',
    'Diamond hands or ramen hands?',
    'Why hold fiat when you can hold crypto?',
    'Bitcoin is the king, but altcoins are the fun ones!',
    'NFTs are just digital Pokémon cards!',
    'Crypto Twitter is wild, I love it!',
    'Crypto is not a scam, you just bought the top!',
    'Bears say “I told you so” at every dip!',
    'Crypto gives me more anxiety than horror movies!',
    'One tweet can change everything!',
    'Crypto conferences are just parties with charts!',
    'If you never got rugged, are you even in crypto?',
    'Rug pull survivors deserve a medal!',
    'Airdrops = free money from the sky!',
    'Sometimes I wonder if my wallet is empty or just slow!',
    'Holding through the bear market is the real test!',
    'Blockchains never sleep, neither do traders!',
    'Crypto people don’t have weekends, just new candles!',
    'Why take profit when you can hold forever? 😂',
    'If I had a dollar for every “crypto is dead” headline!',
    'A bear market is just a long loading screen!',
    'Bull runs are fun until you realize you sold too early!',
    'Crypto: where one second can change everything!',
    'Bitcoin to $1M? Maybe, maybe not!',
    'Crypto memes are the real utility!',
    'I trust my cold wallet more than my bank!',
    'Who needs banks when you have DeFi?',
    'FOMO is the most expensive mistake!',
    'Is this a correction or just the start of something worse? 😂',
    'Crypto is chaos, and I love it!',
    'One day, we’ll all be legends!',
    'Crypto ain’t for the weak!',
    'Remember, it’s only a loss if you sell!'
]

class Main(discord.Client):
    def __init__(self, config):
        super().__init__()
        self.config = config
        
    async def on_ready(self):
        log_success(f"Logged in as {self.user}")
        log_info(f"Attempting to open channel...")
        
        channel = self.get_channel(self.config.channel_id)
        
        if not channel:
            log_error(f"Channel not found!")
            await self.close()
            return
            
        log_success(f"Successfully connected to channel #{channel.name}")
        sent_count = 0

        while sent_count < self.config.message_count:
            # Select a random message
            msg = random.choice(mainMessages)
            try:
                sent_message = await channel.send(msg)
                log_success(f"[{self.user}] Message {sent_count+1}/{self.config.message_count} sent")
                
                if self.config.delete_mode:
                    try:
                        await sent_message.delete()
                        log_info(f"[{self.user}] Message {sent_count+1} deleted")
                    except discord.errors.Forbidden:
                        log_warning(f"[{self.user}] Cannot delete message (no permission)")
                    except discord.errors.NotFound:
                        log_warning(f"[{self.user}] Message already deleted")
                
                sent_count += 1
                
            except discord.errors.Forbidden as e:
                if "Cannot send messages in a voice channel" in str(e):
                    log_error(f"[{self.user}] Cannot send messages in a voice channel!")
                    await self.close()
                    return
                elif "slowmode" in str(e).lower():
                    log_warning(f"[{self.user}] Channel is in slowmode. Waiting...")
                    await asyncio.sleep(10)
                    continue
                elif "timeout" in str(e).lower():
                    log_error(f"[{self.user}] Account is in timeout!")
                    await self.close()
                    return
                else:
                    log_error(f"[{self.user}] Cannot send message! ({str(e)})")
                    await self.close()
                    return
                    
            except discord.errors.HTTPException as e:
                if e.code == 429:  # Rate limit
                    retry_after = e.retry_after
                    log_warning(f"[{self.user}] Rate limit detected. Waiting {retry_after} seconds...")
                    await asyncio.sleep(retry_after)
                    continue
                else:
                    log_error(f"[{self.user}] HTTP Error: {str(e)}")
                    continue
                    
            except Exception as e:
                log_error(f"[{self.user}] Unknown error: {str(e)}")
                continue
                
            await asyncio.sleep(self.config.message_delay)

        log_success(f"[{self.user}] Successfully sent {self.config.message_count} messages")
        await self.close()

def main():
    log_info("Loading tokens from token.txt...")
    tokens = load_tokens()
    
    if not tokens:
        log_error("No tokens successfully loaded!")
        return

    print(f"\n{white}Select Leveling Mode:{reset}")
    print(f"{blue}1. {white}Leveling with Delete Message enabled{reset}")
    print(f"{blue}2. {white}Leveling without Delete Message{reset}")
    
    while True:
        try:
            mode = int(input(f"\n{magenta}Select mode [1/2]: {reset}"))
            if mode in [1, 2]:
                break
            print(f"{red}Invalid choice! Select 1 or 2.{reset}")
        except ValueError:
            print(f"{red}Invalid input! Enter number 1 or 2.{reset}")
    
    delete_mode = mode == 1
    
    channel_id = int(input(f"{magenta}Enter Channel ID: {reset}"))
    message_count = int(input(f"{magenta}Number of messages to send: {reset}"))
    message_delay = int(input(f"{magenta}Delay between messages (in seconds): {reset}"))
    
    accounts = [AccountConfig(token, channel_id, message_count, message_delay, delete_mode) for token in tokens]
    
    for i, config in enumerate(accounts, 1):
        log_info(f"Running account {i} of {len(accounts)}...")
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            client = Main(config)
            client.run(config.token, bot=False)
        except Exception as e:
            log_error(f"Error: {str(e)}")
        finally:
            loop.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log_warning("Program stopped by user")

    except Exception as e:
        log_error(f"Error: {e}")
