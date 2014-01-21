import ctypes

#Get required functions, strcpy..
strcpy = ctypes.cdll.msvcrt.strcpy
ocb = ctypes.windll.user32.OpenClipboard    #Basic Clipboard functions
ecb = ctypes.windll.user32.EmptyClipboard
gcd = ctypes.windll.user32.GetClipboardData
scd = ctypes.windll.user32.SetClipboardData
ccb = ctypes.windll.user32.CloseClipboard
ga = ctypes.windll.kernel32.GlobalAlloc    # Global Memory allocation
gl = ctypes.windll.kernel32.GlobalLock     # Global Memory Locking
gul = ctypes.windll.kernel32.GlobalUnlock
GMEM_DDESHARE = 0x2000 

def Get( ):
  # Open clipboard, default task
  ocb(None)
  pcontents = gcd(1) # 1 means CF_TEXT.. too lazy to get the token thingy ... 
  data = ctypes.c_char_p(pcontents).value
  #gul(pcontents)
  ccb()
  return data

def Paste( data ):
  # Open clipboard, default task
  ocb(None)
  # Empty
  ecb()
  # Allocate memory for data
  hCd = ga( GMEM_DDESHARE, len( bytes(data,"ascii") )+1 )
  # Aquire Lock
  pchData = gl(hCd)
  strcpy(ctypes.c_char_p(pchData),bytes(data,"ascii"))
  # Release Lock
  gul(hCd)
  # Set data
  scd(1,hCd)
  # Close
  ccb()
