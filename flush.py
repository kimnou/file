file=open("flush","a")
file.write("clears internal buffer")
file.flush()
file.write("flushes internal buffer")
