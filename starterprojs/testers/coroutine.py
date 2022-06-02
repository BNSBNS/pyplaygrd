#  Python3 program for demonstrating
# coroutine execution
 
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)
 
# calling coroutine, nothing will happen
corou = print_name("Dear")
 
# This will start execution of coroutine and
# Prints first line "Searching prefix..."
# and advance execution to the first yield expression
corou.__next__()
 
# sending inputs
corou.send("Atul")
# as long as Dear contain
corou.send("Dearr Atul") 


# Python3 program for demonstrating
# coroutine chaining

def producer(sentence, next_coroutine):
	'''
	Producer which just split strings and
	feed it to pattern_filter coroutine
	'''
	tokens = sentence.split(" ")
	for token in tokens:
		next_coroutine.send(token)
	next_coroutine.close()

def pattern_filter(pattern="ing", next_coroutine=None):
	'''
	Search for pattern in received token
	and if pattern got matched, send it to
	print_token() coroutine for printing
	'''
	print("Searching for {}".format(pattern))
	try:
		while True:
			token = (yield)
			if pattern in token:
				next_coroutine.send(token)
	except GeneratorExit:
		print("Done with filtering!!")

def print_token():
	'''
	Act as a sink, simply print the
	received tokens
	'''
	print("I'm sink, i'll print tokens")
	try:
		while True:
			token = (yield)
			print(token)
	except GeneratorExit:
		print("Done with printing!")

pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine = pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)
