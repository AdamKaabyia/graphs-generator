def analyze_relationships(data):
    # Example logic to find relationships based on field types or method parameters
    relationships = {}
    for path, info in data.items():
        for struct_name, struct_fields in info['structs']:
            for field in struct_fields:
                field_type = field.split()[1]  # Simplified extraction of field type
                if field_type in info['structs']:  # Check if field type is another struct
                    relationships[(struct_name, field_type)] = "composition"
    return relationships
