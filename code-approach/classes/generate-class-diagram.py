import xml.etree.ElementTree as ET

def add_class(parent, name, class_id):
    class_cell = ET.SubElement(parent, 'mxCell', id=class_id, value=name,
                               style="swimlane;html=1;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;swimlaneFillColor=#ffffff;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fillColor=none;fontFamily=Verdana;fontSize=12",
                               parent="1", vertex="1")
    ET.SubElement(class_cell, 'mxGeometry', x="20", y="100", width="160", height="100", as_="geometry")
    return class_id

def add_field(parent, class_id, name, type, field_id):
    field_cell = ET.SubElement(parent, 'mxCell', id=field_id, value=f"+ {name}: {type}",
                               style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;",
                               parent=class_id, vertex="1")
    ET.SubElement(field_cell, 'mxGeometry', y="26", width="140", height="20", as_="geometry")

def add_method(parent, class_id, signature, method_id):
    method_cell = ET.SubElement(parent, 'mxCell', id=method_id, value=f"+ {signature}",
                                style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;",
                                parent=class_id, vertex="1")
    ET.SubElement(method_cell, 'mxGeometry', y="50", width="140", height="20", as_="geometry")

def generate_drawio():
    mxfile = ET.Element('mxfile', host="app.diagrams.net",
                        agent="Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
                        version="26.0.11")
    diagram = ET.SubElement(mxfile, 'diagram', name="Page-1", id="example-id")
    mxGraphModel = ET.SubElement(diagram, 'mxGraphModel', dx="1424", dy="768", grid="1", gridSize="10", guides="1",
                                 tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1",
                                 pageWidth="1100", pageHeight="850", background="none", math="0", shadow="0")
    root = ET.SubElement(mxGraphModel, 'root')
    ET.SubElement(root, 'mxCell', id="0")
    ET.SubElement(root, 'mxCell', id="1", parent="0")

    class1 = add_class(root, "Classname", "2")
    add_field(root, class1, "field1", "Type", "3")
    add_field(root, class1, "field2", "Type", "4")
    add_method(root, class1, "method1(Type): Type", "5")
    add_method(root, class1, "method2(Type, Type): Type", "6")

    tree = ET.ElementTree(mxfile)
    tree.write('output.drawio', encoding='utf-8', xml_declaration=True)

generate_drawio()
