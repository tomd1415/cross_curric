import os

class Config:
    SUBJECT1 = "Computing"
    SUBJECT2 = "PSHE"
    YEAR_GROUP = "Year 7"
    API_KEY = os.environ.get("OPENAI_API_KEY")
    ASSISTANT_ID = "asst_YD85E6hMJiuTb3cPkdZEXTor"
    VECTOR_STORE_ID = "vs_dDNSpbfefdYjygAyIt7lgfMO"
    OUTPUT_FILENAME = f"{YEAR_GROUP}_{SUBJECT1}_{SUBJECT2}"
    HTML_FILENAME = OUTPUT_FILENAME + ".html"
    PDF_FILENAME = OUTPUT_FILENAME + ".pdf"
    STYLE = """<!DOCTYPE html>
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
"""
    PROMPT_EXAMPLES = """Example 1 for when Computing and History were looked at the example is between <body> and </body>:
<body>
<h1 id=\"yeargroup\">Year 7</h1>
<h1>Cross-Curriculum Links Between</h1>
<h1 id=\"subjects\">Computing and History</h1>
<h2>Summary</h2>
<p>In Year 7, there are several opportunities to link the Computing curriculum with the History curriculum, particularly in terms defined by overlapping skills such as the use of technical software, data analysis, and the understanding of how societies and technologies develop over time. The strongest existing links are evident in the study of the Roman Empire and the Saxon, Viking, and Norman periods, where digital timelines and data modeling can enhance historical understanding.</p>
<h2>Detailed Links</h2>
<h3>Autumn Term 1: <span class=\"topics\">What is History and The Romans</span></h3>
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
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Create timelines using digital tools to model the sequence of historical events.</li>
<li>Use simple coding to simulate Roman army movements or daily life scenarios.</li>
<li>Analyze historical data sets to understand population distributions in Roman towns.</li>
</ul>
<h3>Autumn Term 2: <span class=\"topics\">Saxons, Vikings, and Normans</span></h3>
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
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Use historical data to create digital maps showing the routes taken by the Saxons and Vikings.</li>
<li>Program simple decision trees reflecting historical battle outcomes based on variables (e.g., size of the army, resources).</li>
</ul>
<h3>Spring Term 1: <span class=\"topics\">Medieval Kings</span></h3>
<h4>Computing:</h4>
<ul>
<li>Advanced use of sequences and conditions in programming.</li>
</ul>
<h4>History:</h4>
<ul>
<li>Examination of various medieval monarchs and their contributions.</li>
<li>Understanding the political changes during medieval times.</li>
</ul>
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Create an interactive software project where students can explore decisions made by medieval kings.</li>
<li>Incorporate data analysis of historical documents to identify political trends and changes.</li>
</ul>
<h3>Spring Term 2 and Summer Term 1: <span class=\"topics\">Medieval Life</span></h3>
<h4>Computing:</h4>
<ul>
<li>Exploring more complex sequences and the concept of iteration in programming.</li>
</ul>
<h4>History:</h4>
<ul>
<li>Detailed look into the daily life, law, entertainment, and religion during medieval Europe.</li>
</ul>
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Develop a simulation game where students code scenarios based on medieval life choices.</li>
<li>Use spreadsheets to analyze statistical data about medieval populations, health, and economy.</li>
</ul>
<h3>Summer Term 2: <span class=\"topics\">The Wider World</span></h3>
<h4>Computing:</h4>
<ul>
<li>Applying knowledge of sequences and data modeling in broader projects.</li>
</ul>
<h4>History:</h4>
<ul>
<li>Study of international historical figures and major global trade routes (e.g., Silk Roads).</li>
</ul>
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Create digital models of trade routes and analyze trade data using spreadsheets and mapping software.</li>
<li>Program simulations about cultural exchange and economic impact along the Silk Roads.</li>
</ul>
<h2>Further Development of Cross-Curriculum Links</h2>
<p>To further strengthen cross-curricular links, project-based learning could be encouraged where students undertake comprehensive projects involving both computing and history skills. For example, they might design a historical website or interactive presentation about a particular era studied in history. Encouraging data-driven historical research using digital tools will not only deepen their understanding of historical events but also solidify their computational thinking skills. Additionally, collaborative exercises where students use programming to tell historical narratives or examine \"what-if\" scenarios can be both engaging and fun.</p>
</body>

Example 2 for when Computing and Art were looked at the example is between <body> and </body>:

<body>
<h1 id=\"yeargroup\">Year 7</h1>
<h1>Cross-Curriculum Links Between</h1>
<h1 id=\"subjects\">Computing and Art</h1>
<h2>Summary</h2>
<p>In Year 7, there are multiple opportunities to link the Computing curriculum with the Art curriculum, emphasising the integration of digital media tools to enhance artistic creation and presentation as well as using computational thinking for creative problem-solving. Existing links are most apparent in digital photography, internet research for artistic inspiration, and the creation of digital presentations which can be aligned within the same term to reinforce learning in both subjects.</p>
<h2>Detailed Links</h2>
<h3>Autumn Term 1: <span class=\"topics\">Introduction to Carving and Introduction to Computing</span></h3>
<h4>Computing:</h4>
<ul>
<li>Introduction to sequence and control flow in programming.</li>
<li>Basic internet research skills.</li>
</ul>
<h4>Art:</h4>
<ul>
<li>Learning about Inuit soapstone carvings.</li>
<li>Research using books, photographs, and the internet to inform their work.</li>
</ul>
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Students can research Inuit carving techniques online and present their findings using digital presentation software.</li>
<li>Introduce basic photo editing tools for documenting their carving projects.</li>
</ul>
<h3>Autumn Term 2:<span class=\"topics\"> The Living World and Networks</span></h3>
<h4>Computing:</h4>
<ul>
<li>Introduction to digital networks and how they enable information sharing.</li>
<li>Basic skills in utilising digital tools for communication.</li>
</ul>
<h4>Art:</h4>
<ul>
<li>Creating a project title page focusing on composition, lettering styles, and presentation.</li>
<li>Experimenting with different mediums and modifying work as it progresses.</li>
</ul>
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Students can use online resources to gather inspiration for their title page and present their project using digital tools.</li>
<li>Incorporate software to digitally create and refine their art pieces.</li>
</ul>
<h3>Spring Term 1:<span class=\"topics\">Digital Photography and Sequencing in Scratch</span></h3>
<h4>Computing:</h4>
<ul>
<li>Introduction to programming with Scratch, including sequences and variables.</li>
</ul>
<h4>Art:</h4>
<ul>
<li>Using digital photography to record and document artistic work.</li>
</ul>
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Combine Scratch programming with digital art by creating animated stories or interactive art pieces where students use their digital photos as assets.</li>
</ul>
<h3>Spring Term 2: <span class=\"topics\">Rural Landscapes and Data Modelling</span></h3>
<h4>Computing:</h4>
<ul>
<li>Understanding spreadsheets, collecting, and modelling data.</li>
</ul>
<h4>Art:</h4>
<ul>
<li>Studying rural landscapes and experimenting with different media.</li>
</ul>
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Utilize spreadsheets to gather data on landscape types and integrate these findings into their landscape artworks.</li>
<li>Create digital compositions or visualisations of rural landscapes based on gathered data.</li>
</ul>
<h3>Summer Term 1: <span class=\"topics\">Using Media for a Cause and The Wider World</span></h3>
<h4>Computing:</h4>
<ul>
<li>Using media to create content that gains support for a cause, inclusive of copyright and fair use principles.</li>
</ul>
<h4>Art:</h4>
<ul>
<li>Exploring a broader artistic world inspired by various cultural figures and historical contexts.</li>
</ul>
<h4 class=\"cross\">Cross-Curriculum Ideas:</h4>
<ul>
<li>Students can create digital campaigns advocating for environmental conservation using their art inspired by different cultures.</li>
<li>Integrate photography and editing tools to create impactful visual content that aligns with a cause they are passionate about.</li>
</ul>
<h2>Further Development of Cross-Curriculum Links</h2>
<p>To further strengthen cross-curricular links, more project-based learning opportunities can be introduced where students use digital tools to complement their artistic projects. For example, students might develop digital portfolios that compile their art and document the creative process from inspiration (via internet research) to final product. They could also create digital animations or interactive stories where both their programming and artistic skills are utilised. Encouraging the use of technology in documenting and presenting art projects would also allow students to see the practical applications of their computing skills in enhancing their artistic expression.</p>
</body>
"""

