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
<h1 id="yeargroup">Year 7<h1>
<h1>Cross-Curriculum Links Between</h1>
<h1 id="subjects">Computing and History</h1>
<h2>Summary</h2>
<p>In Year 7, there are several opportunities to link the Computing curriculum with the History curriculum, particularly in terms defined by overlapping skills such as the use of technical software, data analysis, and the understanding of how societies and technologies develop over time. The strongest existing links are evident in the study of the Roman Empire and the Saxon, Viking, and Norman periods, where digital timelines and data modeling can enhance historical understanding.</p>
<h2>Detailed Links</h2>
<h3>Autumn Term 1: <span class="topics">What is History and The Romans</span></h3>
<h4>Computing:</h4>
<ul>
<li>Understanding sequence and control flow in programming.</li>
<li>Modeling data and variables.</li>
</ul>
<h4>History:</h4>
<ul>
<li>Introduction to historical timelines and chronology.</li>
<li>Study of the Roman invasion, society, and everyday life.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Create timelines using digital tools to model the sequence of historical events.</li>
<li>Use simple coding to simulate Roman army movements or daily life scenarios.</li>
<li>Analyze historical data sets to understand population distributions in Roman towns.</li>
</ul>
<h3>Autumn Term 2: <span class="topics">Saxons, Vikings, and Normans</span></h3>
<h4>Computing:</h4>
<ul>
<li>Define and modify sequences.</li>
<li>Introduction to the concepts of variables and conditions.</li>
</ul>
<h4>History:</h4>
<ul>
<li>Study of the invasions and changes brought by the Saxons, Vikings, and Normans.</li>
<li>Examination of the 1066 crisis and the Norman conquest.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Use historical data to create digital maps showing the routes taken by the Saxons and Vikings.</li>
<li>Program simple decision trees reflecting historical battle outcomes based on variables (e.g., size of the army, resources).</li>
</ul>
<h3>Spring Term 1: <span class="topics">Medieval Kings</span></h3>
<h4>Computing:</h4>
<ul>
<li>Advanced use of sequences and conditions in programming.</li>
</ul>
<h4>History:</h4>
<ul>
<li>Examination of various medieval monarchs and their contributions.</li>
<li>Understanding the political changes during medieval times.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Create an interactive software project where students can explore decisions made by medieval kings.</li>
<li>Incorporate data analysis of historical documents to identify political trends and changes.</li>
</ul>
<h3>Spring Term 2 and Summer Term 1: <span class="topics">Medieval Life</span></h3>
<h4>Computing:</h4>
<ul>
<li>Exploring more complex sequences and the concept of iteration in programming.</li>
</ul>
<h4>History:</h4>
<ul>
<li>Detailed look into the daily life, law, entertainment, and religion during medieval Europe.</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Develop a simulation game where students code scenarios based on medieval life choices.</li>
<li>Use spreadsheets to analyze statistical data about medieval populations, health, and economy.</li>
</ul>
<h3>Summer Term 2: <span class="topics">The Wider World</span></h3>
<h4>Computing:</h4>
<ul>
<li>Applying knowledge of sequences and data modeling in broader projects.</li>
</ul>
<h4>History:</h4>
<ul>
<li>Study of international historical figures and major global trade routes (e.g., Silk Roads).</li>
</ul>
<h4 class="cross">Cross-Curriculum Ideas:</h4>
<ul>
<li>Create digital models of trade routes and analyze trade data using spreadsheets and mapping software.</li>
<li>Program simulations about cultural exchange and economic impact along the Silk Roads.</li>
</ul>
<h2>Further Development of Cross-Curriculum Links</h2>
<p>To further strengthen cross-curricular links, project-based learning could be encouraged where students undertake comprehensive projects involving both computing and history skills. For example, they might design a historical website or interactive presentation about a particular era studied in history. Encouraging data-driven historical research using digital tools will not only deepen their understanding of historical events but also solidify their computational thinking skills. Additionally, collaborative exercises where students use programming to tell historical narratives or examine "what-if" scenarios can be both engaging and fun.</p>
</body>
</html>
"""

# Convert HTML to PDF
output_filename = "Curriculum_Report_history.pdf"
convert_html_to_pdf(html_content, output_filename)

