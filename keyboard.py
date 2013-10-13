# keyboard.py  11/10/2013 (c) 2013 @whaleygeek
#
# Usage:
#   import keyboard
#   key = keyboard.get()

def getLinux():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch

def getWin():
  ch = msvcrt.getch()
  b = ord(ch)
  if (b == 3): # CTRL-C
    raise KeyboardInterrupt
  return ch
  
try:
  import msvcrt
  get = getWin
except ImportError:
  try:
    import sys, tty, termios
    get = getLinux
  except ImportError:
    raise "No OS keyboard handler found"  

if __name__ == "__main__":
  while True:
    print get()
    
    
    
    
    


  
  