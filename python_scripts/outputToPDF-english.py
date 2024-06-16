from xhtml2pdf import pisa

# Function to convert HTML to PDF
def convert_html_to_pdf(source_html, output_filename):
    # Open output file for writing (binary mode)
    with open(output_filename, "w+b") as output_file:
        # Convert HTML to PDF
        pisa_status = pisa.CreatePDF(source_html, dest=output_file)
    return pisa_status.err

# HTML content with embedded CSS for styling
html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        font-family: Arial, sans-serif;
        font-size: 11px;
        line-height: 1.2;
    }
    h1 {
        text-align: center;
        font-size: 16pt;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    h1#yeargroup {
        font-size: 20pt;
        font-weight: bold;
        margin-top:10px;
        color: darkblue;
        }
    h1#subjects {
        font-size: 20pt;
        font-weight: bold;
        margin-bottom: 10px;
        margin-top: 5px;
        color: darkblue;
        }
    h2 {
        text-align: center;
        font-size: 14pt;
        color: #333;
        margin-top: 30px;
        margin-bottom: 8px;
        border-top: 1px, solid, black;
        padding-top: 10px;
    }
    h3 {
        font-size: 12pt;
        color: #444;
        margin-top: 13px;
        margin-bottom: 6px;
    }
    span.topics {
        font-weight: none;
        font-size: 11pt;
        }
    h4 {
        font-size: 10pt;
        color: #555;
        margin-top: 6px;
        margin-bottom: 3px;
        padding-left: 2em;
    }
    h4.cross {
        font-size: 11pt;
        color: darkblue;
        margin-top: 6px;
        margin-bottom: 3px;
    }
    ul {
        margin-top: 0;
        margin-bottom: 6px;
        padding-left: 3em;
    }
    ul li {
        margin-bottom: 5px;
    }
    p {
        margin-top: 0;
        margin-bottom: 10px;
    }
</style>
</head>
<body>
<h1 id="yeargroup">Year 7</h1>
<h1>Cross-Curriculum Links Between</h1>
<h1 id="subjects">Computing and English</h1>
<h2>Summary</h2>
<p>In Year 7, there are numerous opportunities to link the Computing curriculum with the English curriculum, particularly through the integration of digital literacy, data interpretation, and multimedia content creation. The most prominent cross-curricular opportunities lie in multimedia presentations, analysis of digital texts, and understanding the impact of technology on communication.</p>
<h2>Detailed Links</h2>
<h3>Autumn Term 1: <span class="topics">Introduction to Computing and Fictional Narratives</span></h3>
<h4>Computing:</h4>
<ul>
<li>Introduction to sequence and control flow in programming.</li>
<li>Basic internet research skills.</li>
</ul>
<h4>English:</h4>
<ul>
<li>Introduction to fictional narratives and story elements.</li>
<li>Reading and analysing character and plot development.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Students can create interactive digital stories or animations based on their fictional narratives using programming tools.</li>
<li>Introduce basic elements of digital literacy to research background information for narrative settings and themes.</li>
<li>Utilise programming to build branching narratives, making decisions based on character development.</li>
</ul>
<h3>Autumn Term 2: <span class="topics">Developing Communication Skills and Persuasive Writing</span></h3>
<h4>Computing:</h4>
<ul>
<li>Introduction to digital networks and how they enable information sharing.</li>
<li>Basic skills in utilising digital tools for communication.</li>
</ul>
<h4>English:</h4>
<ul>
<li>Focus on persuasive writing techniques and constructing arguments.</li>
<li>Exploring different forms of communication including speeches and letters.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Students could develop and present digital campaigns or public service announcements, combining their persuasive writing skills with multimedia tools.</li>
<li>Utilise digital presentation software to enhance their argumentative essays and speeches.</li>
<li>Analysis of digital marketing techniques and their persuasive power across various media.</li>
</ul>
<h3>Spring Term 1: <span class="topics">Non-Fiction Texts and Data Modelling</span></h3>
<h4>Computing:</h4>
<ul>
<li>Understanding spreadsheets and collecting and modeling data.</li>
<li>Basic coding and use of logic sequences.</li>
</ul>
<h4>English:</h4>
<ul>
<li>Reading and writing informational/expository texts.</li>
<li>Evaluating evidence and data to support textual analysis.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Students can use spreadsheets to collect and analyse data for informational texts.</li>
<li>Creating digital infographics or data visualisations to complement written reports and presentations.</li>
<li>Develop coding projects that automate the collection and presentation of data about informational topics.</li>
</ul>
<h3>Spring Term 2: <span class="topics">Poetry and Multimedia Projects</span></h3>
<h4>Computing:</h4>
<ul>
<li>Editing and creating multimedia projects such as videos or podcasts.</li>
<li>Understanding the use of sound and visuals in enhancing digital content.</li>
</ul>
<h4>English:</h4>
<ul>
<li>Reading, analysing, and composing various forms of poetry.</li>
<li>Exploring the use of imagery and auditory elements in poems.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Create multimedia projects that combine voice recordings of poetry with digital music and images.</li>
<li>Students can use software to edit and enhance their poetry readings with sound effects and background music.</li>
<li>Develop digital poetry anthologies that employ different multimedia components to enrich the readers’ experience.</li>
</ul>
<h3>Summer Term 1: <span class="topics">Digital Citizenship and Modern Literature</span></h3>
<h4>Computing:</h4>
<ul>
<li>Understanding the implications of digital citizenship and online safety.</li>
<li>Exploring the basics of creating and evaluating content for the web.</li>
</ul>
<h4>English:</h4>
<ul>
<li>Study of modern literature and its themes related to technology and society.</li>
<li>Critical thinking about the impact of digital media on literature and communication.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Evaluate and discuss modern literature that addresses issues of digital citizenship and online behaviour.</li>
<li>Create blog posts or online articles that reflect on the themes discussed in their literature classes.</li>
<li>Students could design web pages or digital portfolios to present their modern literature analyses and reflections.</li>
</ul>
<h3>Summer Term 2: <span class="topics">Interactive Fiction and Creative Writing</span></h3>
<h4>Computing:</h4>
<ul>
<li>Applying knowledge of sequences and data modeling in broader projects such as interactive stories.</li>
<li>Using programming to create interactive narratives and choose-your-own-adventure games.</li>
</ul>
<h4>English:</h4>
<ul>
<li>Focus on creative writing and developing original stories.</li>
<li>Exploring narrative structures and alternative storytelling methods.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Develop interactive fiction projects where students write and code their stories with multiple outcomes.</li>
<li>Leverage digital storytelling tools to enhance creative writing and explore different narrative structures.</li>
<li>Use programming to gamify storytelling, enabling interactive choices within their written narratives.</li>
</ul>
<h2>Further Development of Cross-Curriculum Links</h2>
<p>To enhance cross-curricular links further, project-based learning can be introduced where students integrate computing skills with their English assignments. For instance, they might develop a digital magazine or a blog that showcases their creative writing, incorporating multimedia elements such as podcasts, videos, or interactive graphics. Encouraging students to use digital tools for research, analysis, and presentation of their English literature assignments will not only deepen their understanding but also solidify their digital literacy skills. Collaborative projects that combine coding with storytelling or that employ digital platforms for the publication and critique of work could be particularly engaging and educational.</p>
</body>
</html>
"""

# Convert HTML to PDF
output_filename = "Curriculum_Report_english.pdf"
convert_html_to_pdf(html_content, output_filename)

