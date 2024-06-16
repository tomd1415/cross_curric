from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

# Content from the OpenAI API
content = """
### Year 7 Cross-Curriculum Links Between Computing and Art

#### Summary
In Year 7, there are multiple opportunities to link the Computing curriculum with the Art curriculum, emphasising the integration of digital media tools to enhance artistic creation and presentation as well as using computational thinking for creative problem-solving. Existing links are most apparent in digital photography, internet research for artistic inspiration, and the creation of digital presentations which can be aligned within the same term to reinforce learning in both subjects.

#### Detailed Links

- **Autumn Term 1: Introduction to Carving and Introduction to Computing**
  - **Computing**:
    - Introduction to sequence and control flow in programming.
    - Basic internet research skills.
  - **Art**:
    - Learning about Inuit soapstone carvings.
    - Research using books, photographs, and the internet to inform their work.
  - **Cross-Curriculum Ideas**:
    - Students can research Inuit carving techniques online and present their findings using digital presentation software.
    - Introduce basic photo editing tools for documenting their carving projects.

- **Autumn Term 2: The Living World and Networks**
  - **Computing**:
    - Introduction to digital networks and how they enable information sharing.
    - Basic skills in utilising digital tools for communication.
  - **Art**:
    - Creating a project title page focusing on composition, lettering styles, and presentation.
    - Experimenting with different mediums and modifying work as it progresses.
  - **Cross-Curriculum Ideas**:
    - Students can use online resources to gather inspiration for their title page and present their project using digital tools.
    - Incorporate software to digitally create and refine their art pieces.

- **Spring Term 1: Digital Photography and Sequencing in Scratch**
  - **Computing**:
    - Introduction to programming with Scratch, including sequences and variables.
  - **Art**:
    - Using digital photography to record and document artistic work.
  - **Cross-Curriculum Ideas**:
    - Combine Scratch programming with digital art by creating animated stories or interactive art pieces where students use their digital photos as assets.

- **Spring Term 2: Rural Landscapes and Data Modelling**
  - **Computing**:
    - Understanding spreadsheets, collecting, and modelling data.
  - **Art**:
    - Studying rural landscapes and experimenting with different media.
  - **Cross-Curriculum Ideas**:
    - Utilize spreadsheets to gather data on landscape types and integrate these findings into their landscape artworks.
    - Create digital compositions or visualisations of rural landscapes based on gathered data.

- **Summer Term 1: Using Media for a Cause and The Wider World**
  - **Computing**:
    - Using media to create content that gains support for a cause, inclusive of copyright and fair use principles.
  - **Art**:
    - Exploring a broader artistic world inspired by various cultural figures and historical contexts.
  - **Cross-Curriculum Ideas**:
    - Students can create digital campaigns advocating for environmental conservation using their art inspired by different cultures.
    - Integrate photography and editing tools to create impactful visual content that aligns with a cause they are passionate about.

#### Further Development of Cross-Curriculum Links
To further strengthen cross-curricular links, more project-based learning opportunities can be introduced where students use digital tools to complement their artistic projects. For example, students might develop digital portfolios that compile their art and document the creative process from inspiration (via internet research) to final product. They could also create digital animations or interactive stories where both their programming and artistic skills are utilised. Encouraging the use of technology in documenting and presenting art projects would also allow students to see the practical applications of their computing skills in enhancing their artistic expression.
"""

# Function to convert the content into a formatted PDF
def create_pdf(content, filename):
    # Create a PDF document
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    # Customize the title style
    title_style = ParagraphStyle(
        name='Title',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12,
        alignment=TA_CENTER
    )

    # Split the content into lines
    lines = content.split('\n')

    # Create a list to hold the PDF elements
    elements = []

    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue

        # Apply different styles based on the content
        if line.startswith('####'):
            line = line.replace('#### ', '')
            elements.append(Paragraph(line, styles['Heading2']))
        elif line.startswith('###'):
            line = line.replace('### ', '')
            elements.append(Paragraph(line, title_style))
        elif line.startswith('- **'):
            line = line.replace('- **', '    ')
            line = line.replace('**', '')
            elements.append(Paragraph(line, styles['Heading3']))
        elif line.startswith('  - **'):
            line = line.replace('  - **', '    ')
            line = line.replace('**:', ':')
            elements.append(Paragraph(line, styles['Heading4']))
        elif line.startswith('    - '):
            line = line.replace('    - ', '')
            elements.append(Paragraph(line, styles['Normal']))
        else:
            elements.append(Paragraph(line, styles['Normal']))

        # Add a small space after each paragraph
        elements.append(Spacer(1, 0.1 * inch))

    # Build the PDF
    doc.build(elements)

# Create the PDF
create_pdf(content, "Curriculum_Report.pdf")

