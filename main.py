from featuretohtml.utils import parse_properties
from os import path
import featuretohtml.parse_gherkin
properties = parse_properties(r".\config.properties")

print(properties)
print(path.abspath(path.curdir))