'''
Reportlab Template for platypus and canvas direct drawing simultaneously
'''
from reportlab.platypus import BaseDocTemplate, Frame, FrameBreak, \
     PageTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch,mm
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class Doc:
  
  def __init__(self,pdf_fp):
    # set up reportlab
    self.c = canvas.Canvas(pdf_fp,pagesize=letter)
    self.styles = getSampleStyleSheet()
    self.pstyle = self.styles['Normal']
    self.pstyle.alignment=1
    # begin
    self.createDoc()
    
  def nextPage(self):
    'add page number and change page'
    # page number
    page_num = self.c.getPageNumber()
    text = "Page #%s" % page_num
    self.c.setFont('Helvetica',11)
    self.c.drawCentredString(letter[0]/2.0, 20*mm, text)
    # draw line
    self.c.setStrokeColor(colors.black)
    self.c.line(inch,25*mm,letter[0]-inch,25*mm)
    # yield page
    self.c.showPage()
    
  def createDoc(self):
    'add document elements'
    self.addTitlePage()
    # Examples:
    #   Playtpus stuff
    p = Paragraph('document body',self.pstyle)
    p.wrapOn(self.c, letter[0]/2. , 4*inch)# you MUST call wrap before draw!!!
    p.drawOn(self.c, letter[0]/4. , letter[1]-4*inch)
    #   Canvas stuff
    im_w,im_h = 600,425
    w,h  =  im_w/4.0, im_h/4.0
    #self.c.drawImage('image.png', letter[0]/2.0 - w/2.0, 8.5*inch, width=w, height=h)
    # create and save
    self.nextPage()
    self.save()

  def addTitlePage(self):
    'add title page elements'
    # some text
    p = Paragraph('This is the title page',self.pstyle)
    p.wrapOn(self.c, letter[0]/2. , 4*inch)# you MUST call wrap before draw!!!
    p.drawOn(self.c, letter[0]/4. , letter[1]-4*inch)
    # start drawing on next page
    self.nextPage()
    
  def save(self):
    'save canvas object to file'
    self.c.save()

if __name__ == '__main__':
  pdf = Doc('sample.pdf')
