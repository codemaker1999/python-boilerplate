MAXLINES = 200
def log(msg):
  'write events to file'
  # decide whether to trim log
  with open('_log.txt','r') as f:
    lines = f.readlines()
    if len(lines) > MAXLINES:
      TRIM = True
    else:
      TRIM = False
  # trim
  if TRIM:
    with open('_log.txt','w') as f:
      lines = lines[-MAXLINES:]
      for line in lines:
        f.write( line )
  # write message
  with open('_log.txt','a') as f:
    f.write(msg + '\n')
