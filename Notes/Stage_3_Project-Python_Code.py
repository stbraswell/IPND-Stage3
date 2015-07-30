#Generates the complete html text for the current concept
def generate_html(stage,title,description,notes,example):
    html_stage = '''
<div id="''' + stage + '''">'''
    
    html_title = '''
    <h3>''' + title + '''</h3>'''
    
    html_description = '''
    <div>
        ''' + description + '''<br>'''
    
    html_note = '''
        <ul>
''' + notes + '''
    '''+ example

    html_end = '''
        </ul>
    </div>
</div>
'''
    full_html_text = html_stage + html_title + html_description + html_note + html_end
    return full_html_text

#Generates the text for the Table of Contents links
def get_toc_html(linklist):
    toc_html ='''<!-- TOC Links
    '''
    for e in linklist:
        toc_html = toc_html + '''
        '''+ e
    toc_html = toc_html +'''
    -->'''
    return toc_html

#Gets the text of the "Stage ID" from the current concept
def get_stage_id(concept):
    start_location = concept.find('STAGE:')
    end_location = concept.find('TITLE:')
    stage = concept[start_location+7 : end_location-1]
    stage = stage.lower()
    return stage

#Gets the text of the "Title" from the current concept
def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

#Gets the text of the "Description" from the current concept
def get_description(concept):
    if 'NOTE: ' in concept:
        start_location = concept.find('DESCRIPTION:')
        end_location = concept.find('NOTE:')
        description = concept[start_location+13 :end_location-1]
    else:
        if 'EXAMPLE:' in concept:
            start_location = concept.find('DESCRIPTION:')
            end_location = concept.find('EXAMPLE:')
            description = concept[start_location+13 :end_location-1]
    return description

# takes in the text of the current concept and creates "list_of_positions" which contains the positions of the text 'NOTE: '
def list_positions_in_string(text):
    i=0
    counter = 0
    list_of_positions = []
    number = ''
    while number != -1:
        number = text.find('NOTE: ',i)
        list_of_positions.append(number)
        i = number + 1
        counter += 1
    return list_of_positions

#takes in the text of the current concept and the output of list_positions_in_string, outputs the text string of each NOTE as an element of a list          
def stringlist(text,strings):
    i = 0
    textlist=[]
    length = len(strings) - 2
    while i< length:
        next_string = text[strings[i] + 6:strings[i + 1]]
        next_string = next_string.rstrip('\n')
        textlist.append(next_string)
        i += 1
    next_string = text[strings[i] + 6:text.find('EXAMPLE:')]
    next_string = next_string.rstrip('\n')
    textlist.append(next_string)
    return textlist

#formats the NOTE's in the current concept as a list
def get_notes(concept):
    if 'NOTE: ' not in concept:
        note_code = ''
    else:    
        position_of_notes = list_positions_in_string(concept)
        number_of_notes = len(position_of_notes) - 1
        note_list = stringlist(concept, position_of_notes)
        i = 0
        note_code = ''
        for e in note_list:
            note_code = note_code +'''            <li>''' + e + '''</li>''' + '\n'
        note_code = note_code.rstrip('\n')
    return note_code

#Gets the URL of the examples and returns the html code to genereate the link
def get_example_links(concept,title):
    if 'EXAMPLE:' not in concept:
        link_html = ''
    else:
        start_location = concept.find('EXAMPLE:')
        end_location = concept.find('STAGE:')
        link = concept[start_location+8 :end_location-1]
        link_html = '''        <li><a href="''' + link + '''"> Examples of ''' + title + '''</a></li>'''
    return link_html

#Takes in the full input text and which concept number is needed; outputs the text of only that specific concept
def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('STAGE:')
        next_concept_end   = text.find('STAGE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEST_TEXT = """STAGE: stage-3-1
TITLE: Structured Data: Definitions
DESCRIPTION: defs
NOTE: Class - A neatly packaged box that puts things together really well. A class is like a blueprint of a building - it can be used to build multiple buildings. A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
NOTE: Instance/Object - A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods. An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
NOTE: Constructor - When an instance is created, the classes constructor is called (__init__)
NOTE: Self - Used in the constructor, self is the instance
NOTE: Instance Variable - A variable associated with a specific instance
NOTE: Instance Method - A function defined in a class and associated with an instance.
EXAMPLE:
STAGE: stage-3-2
TITLE: Things to know about Python
DESCRIPTION: This section includes some random notes about python
NOTE: Classes are defined in a file.  For instance turtle.Turtle(), calls the class “Turtle”, which is located in the file “turtle”
NOTE: Python has a standard library which is very extensive, offering a wide range of facilities. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.
NOTE: There are many external libraries that provide additional modules, some can be found on the python website.
EXAMPLE: https://docs.python.org/2/library/
"""

# generates the full html code for the complete input text
def generate_all_html(text):
    text = text.replace('<','&lt;')
    text = text.replace('>','&gt;')
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    all_toc_links = []
    current_toc_link = ''
    while concept != '':
        stage = get_stage_id(concept)
        title = get_title(concept)
        description = get_description(concept)
        notes = get_notes(concept)
        example = get_example_links(concept,title)
        concept_html = generate_html(stage,title,description,notes,example)
        all_html = all_html + concept_html
        current_toc_link = '''<li><a href="#''' + stage + '''">''' + title + '''</a></li>'''
        all_toc_links.append(current_toc_link)
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    toc_links = get_toc_html(all_toc_links)
    all_html = all_html + toc_links
    return all_html


print generate_all_html(TEST_TEXT)

