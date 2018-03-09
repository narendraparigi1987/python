def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics(f):
    f()
    f()

repeat_lyrics(print_lyrics)