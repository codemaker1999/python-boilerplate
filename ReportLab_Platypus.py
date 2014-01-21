from reportlab.platypus import BaseDocTemplate, Frame, FrameBreak, \
     PageTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# init
elements=[]
styles = getSampleStyleSheet()
doc = BaseDocTemplate('file.pdf',pagesize=letter,showBoundary=0,)
# define Frames
# constructor args:
#     Frame( x,y,wid,hgt,id='foo',leftPadding=0,bottomPadding=0,
#            rightPadding=0, topPadding=0)
# EX: two columns
wid = (letter[0]-2*inch)/2.
hgt = letter[1]-2*inch
frame1 = Frame( inch, inch, wid, hgt, id='col1', leftPadding=0,
                bottomPadding=0, rightPadding=0, topPadding=0)
frame2 = Frame( inch + wid, inch, wid, hgt, id='col2', leftPadding=0,
                bottomPadding=0, rightPadding=0, topPadding=0)
frames = [frame1, frame2]

# Make page templates
pt1 = PageTemplate(id='TwoCol',frames=frames)
pts = [pt1, ]

# Add page templates to doc
doc.addPageTemplates( pts )

# add things to 'elements'
p1 = Paragraph('foo',styles['Normal'])
elements.append( p1 )

# Build PDF
doc.build(elements)
