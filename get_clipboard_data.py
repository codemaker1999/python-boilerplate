import ctypes
ocb = ctypes.windll.user32.OpenClipboard
gcd = ctypes.windll.user32.GetClipboardData
ccb = ctypes.windll.user32.CloseClipboard
def Get( ):
  ocb(None) # Open Clip, Default task
  pcontents = gcd(1) # 1 means CF_TEXT
  data = ctypes.c_char_p(pcontents).value
  ccb()
  return data
