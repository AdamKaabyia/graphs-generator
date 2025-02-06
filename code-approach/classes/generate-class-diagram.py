import xml.etree.ElementTree as ET

def create_element_with_text(parent, tag, text, **attributes):
    element = ET.SubElement(parent, tag, **attributes)
    element.text = text
    return element

def create_cell(parent, **attributes):
    return ET.SubElement(parent, 'mxCell', **attributes)

def create_geometry(parent, **attributes):
    return ET.SubElement(parent, 'mxGeometry', **attributes)

def add_class(parent, name, id, x, y, width, height):
    cell = create_cell(parent, id=id, value=name, vertex="1", parent="1",
                       style="swimlane;html=1;fontStyle=1;align=center;verticalAlign=top;"
                             "childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;"
                             "resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;"
                             "swimlaneFillColor=#ffffff;rounded=0;shadow=0;comic=0;"
                             "labelBackgroundColor=none;strokeWidth=1;fillColor=none;fontFamily=Verdana;fontSize=12")
    create_geometry(cell, x=str(x), y=str(y), width=str(width), height=str(height), as_="geometry")
    return cell

def add_field_or_method(parent, content, y_offset):
    cell = create_cell(parent, value=content, vertex="1", parent=parent.get('id'),
                       style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;"
                             "spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;"
                             "points=[[0,0.5],[1,0.5]];portConstraint=eastwest;")
    create_geometry(cell, y=str(y_offset), width="160", height="26", as_="geometry")

def generate_drawio():
    mxfile = ET.Element('mxfile', host="app.diagrams.net", version="26.0.11",
                        agent="Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0")
    diagram = create_element_with_text(mxfile, 'diagram', '', name="Page-1", id="unique-id-123")
    mxGraphModel = create_element_with_text(diagram, 'mxGraphModel', '', dx="1424", dy="768", grid="1",
                                            gridSize="10", guides="1", tooltips="1", connect="1", arrows="1",
                                            fold="1", page="1", pageScale="1", pageWidth="1100", pageHeight="850",
                                            background="none", math="0", shadow="0")
    root = create_element_with_text(mxGraphModel, 'root', '')
    create_cell(root, id="0")
    create_cell(root, id="1", parent="0")

    class1 = add_class(root, "Classname", "2", 20, 100, 300, 200)
    add_field_or_method(class1, "+ field1: Type", 30)
    add_field_or_method(class1, "+ field2: Type", 60)
    add_field_or_method(class1, "+ method1(Type): Type", 90)
    add_field_or_method(class1, "+ method2(Type, Type): Type", 120)

    tree = ET.ElementTree(mxfile)
    tree.write('example.drawio', encoding='utf-8', xml_declaration=True)

generate_drawio()
