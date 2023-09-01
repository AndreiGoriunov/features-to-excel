def parse_properties(file_path):
    properties = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):  # Skip comments and empty lines
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()
    return properties