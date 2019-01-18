#Chronos, 2019. Fuck SJWs, niggers and jannies.
#TODO: make everything fancier, continually refresh already-made posts and add in info about the thread (ex: current number of posts and images)
import asyncio
import moesearch
import discord

token = 'Your bot token goes here, https://discordapp.com/developers/applications/'
robotThreads = []

guildName = 'Your discord server name goes here'
channelName = 'Your dedicated robot porn channel name goes here'

client = discord.Client()

async def backgroundRefresh(): 
        await client.wait_until_ready()
        print("[LOG] Refreshing thread array")
        while 1 == 1:
                for x in range(0,24):
                        if 'https://desuarchive.org/aco/thread/'+moesearch.search(archiver_url="https://desuarchive.org",board="aco",text="http://clang.booru.org/",subject="Robot Thread")[x].thread_num in robotThreads:
                                pass
                        else: 
                                robotThreads.insert(0, moesearch.search(archiver_url="https://desuarchive.org",board="aco",text="http://clang.booru.org/",subject="Robot Thread")[x].thread_num)
                print("[LOG] Thread array refreshed.")
                await asyncio.sleep(1800)

async def threadPosting():
        await client.wait_until_ready()
        channel = discord.utils.get(client.get_all_channels(), guild__name=guildName, name=channelName)
        while 1 == 1: 
                channelhistory = await channel.history().flatten()
                messagehistory = []
                for n in range(len(channelhistory)):
                        messagehistory.append(channelhistory[n].content)
                for x in range(len(robotThreads)):
                        if any(robotThreads[x] in s for s in messagehistory):
                                pass
                        else:
                                print("[LOG] Posting new thread, "+robotThreads[x])
                                fuckbed = discord.Embed(title = moesearch.thread("https://desuarchive.org",'aco',robotThreads[x]).op.title_processed)
                                fuckbed.set_image(url = moesearch.thread("https://desuarchive.org",'aco',robotThreads[x]).op.media.media_link)
                                await channel.send('https://desuarchive.org/aco/thread/'+robotThreads[x], embed=fuckbed)
                                await asyncio.sleep(5)
                await asyncio.sleep(1801)




@client.event
async def on_ready():
        await client.change_presence(activity=discord.Game("with humans"))
        print('Logged in as '+str(client.user.name)+'\n'+str(client.user.id))
        print('------')
        

client.loop.create_task(backgroundRefresh())
client.loop.create_task(threadPosting())
client.run(token)
