#!/usr/bin/env python3 

from ebaysdk.finding import Connection
import time
import sys
import signal

def signal_handler(signal, frame):
	print("\nA Clean Exit...")
	sys.exit()
signal.signal(signal.SIGINT, signal_handler)

try:
	ItemDesc =  sys.argv[1]
	

	print('#####################################')																	
	print('#                                   #')
	print('#           $$ Jordys $$            #')
	print('#       $$ Pokemon Pricer $$        #')
	print('#             by ryku               #')
	print('#                                   #')
	print('#####################################')
	print('\n')
	print('\n')
	print('Hmmmmm Hungry For Some Candy....')

	animation = "|/-\\"


	for i in range(100):
	    time.sleep(0.1)
	    sys.stdout.write("\r" + 'Searching for the rarest of candies....' + animation[i % len(animation)])
	    sys.stdout.flush()
	    #do something
	try:
	    api = Connection(siteid='EBAY-ENCA')
	    
	    response = api.execute('findCompletedItems', {'keywords': ItemDesc})

	    assert(response.reply.ack == 'Success')
	    assert(type(response.reply.timestamp) == datetime.datetime)
	    assert(type(response.reply.searchResult.item) == list)

	    item = response.reply.searchResult.item[0]
	    assert(type(item.listingInfo.endTime) == datetime.datetime)
	    assert(type(response.dict()) == dict)

	except ConnectionError as e:
	    print(e)
	    print(e.response.dict())
	    print("End!") 

except IndexError:
	print('\n[*] Usage: python3 pokepricer.py <pokemon card> E.g: python3 pokepricer.py Blastoise')
