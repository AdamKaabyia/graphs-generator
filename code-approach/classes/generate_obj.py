import xml.etree.ElementTree as ET

def generate_xml_elements(data):
    root = ET.Element('diagram')
    for path, info in data.items():
        for struct_name, _ in info['structs']:
            ET.SubElement(root, 'struct', name=struct_name)
        for interface_name, _ in info['interfaces']:
            ET.SubElement(root, 'interface', name=interface_name)
    return root


def add_relationships_to_xml(root, relationships):
    for (source, target), relation_type in relationships.items():
        ET.SubElement(root, 'relationship', source=source, target=target, type=relation_type)
