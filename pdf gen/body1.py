from fpdf import FPDF

title = 'SAMPLE BUSINESS MEETING MINUTES FOR JONES CONSULTANTS, INC.'

class PDF(FPDF):
    def header(self):
        if self.page_no() == 1 :
            # Arial bold 15
            self.set_font('Arial', 'B', 15)
            # Calculate width of title and position
            w = self.get_string_width(title) + 6
            self.set_x((210 - w) / 2)
            # Colors of frame, background and text
            # self.set_draw_color(0, 80, 180)
            # self.set_fill_color(230, 230, 0)
            self.set_text_color(220, 50, 50)
            # Thickness of frame (1 mm)
            self.set_line_width(1)
            # Title
            
            self.multi_cell(0, 10, title.upper(), 0, 1, 'C')
            # Line break
            self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, '')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', 'B', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, ' %d : %s' % (num, label), 0, 1, 'L')
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        # with open(name, 'rb') as fh:
        #     txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 13)
        # Output justified text
        self.multi_cell(0, 5, '%s ' % (name), 0, 1, 'L')
        # Line break
        self.ln()
        # Mention in italics
        # self.set_font('', 'I')
        # self.cell(0, 5, '(end of excerpt)')
    
    def chapter_subody(self, subname):
        self.set_font('Times', '', 13)
        self.multi_cell(0, 5, '%s' % (subname), 0, 1, 'L')
        # self.set_text_color(220, 0, 0)
        self.ln()
        # Thickness of frame (1 mm)
        # self.set_line_width(1)

    def print_chapter(self, num, title, name, subname):
        self.chapter_title(num, title)
        self.chapter_body(name)
        self.chapter_subody(subname)

pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.rect(5, 5, 200, 287, 'D')
# pdf.set_left_margin(20)
pdf.set_title(title)

# pdf.set_author('Jules Verne')
pdf.print_chapter(1, 'MEETING DETAILS ' ,'    Chairman : \n    Secretary: \n\n    Date: \n    Time: \n\n    Priority: \n    Venue: \n    Agenda: \n', '' )
pdf.print_chapter(2, 'ATTENDEES', '    (name1) \n    (name2) \n    (name3) ', '')
pdf.print_chapter(3, 'CALL TO ORDER' , '    A meeting of (organization) was held at (location) on (date)','' )
pdf.print_chapter(4, 'REPORT FROM', '   (minutes)', '')
pdf.print_chapter(5, 'APPROVAL OF MINUTES', '   A motion to approve the minutes of the previous (date) meeting wase made by (name)  and seconded by (name) ', '')
pdf.print_chapter(6, 'ADJOURNMENT', '   End of Meeting - speaker (name) - (time)', '   Minutes submitted by : (sign) Print name: (name) \n   Approved by: (sign) Print name: (name) ')

pdf.output('tuto2.pdf', 'F')
 