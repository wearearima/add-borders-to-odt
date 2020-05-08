import sys
import shutil
import zipfile
import xml.etree.ElementTree as ET

if sys.version_info[0] != 3:
    print("Please run script with Python 3.x")
    sys.exit(1)

args = len(sys.argv)

if args < 2:
    print("Invalid number of arguments! (python", sys.argv[0], "<filename>")
    sys.exit(1)

src = str(sys.argv[1])
tmp_dir = "tmp_dir/"

if args >= 3:
    dst = str(sys.argv[2])
else:
    if '.' in src:
        src_arr = src.split('.')
        dst = src_arr[0] + "_new." + src_arr[1]
    else:
        dst = src + "_new"

# Extract contents from odt to directory
try:
    with zipfile.ZipFile(src, 'r') as zip_ref:
        zip_ref.extractall(tmp_dir)
except FileNotFoundError:
    print("Could not find", src)
    sys.exit(1)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

# Namespace declaration
ns = {'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
      'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
      'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
      'svg': 'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
      'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
      'loext': 'urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0',
      'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
      'draw': 'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
      'xlink': 'http://www.w3.org/1999/xlink',
      'officeooo': 'http://openoffice.org/2009/office',
      'grddl': 'http://www.w3.org/2003/g/data-view#',
      'xhtml': 'http://www.w3.org/1999/xhtml',
      'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
      'xsd': 'http://www.w3.org/2001/XMLSchema',
      'xforms': 'http://www.w3.org/2002/xforms',
      'dom': 'http://www.w3.org/2001/xml-events',
      'script': 'urn:oasis:names:tc:opendocument:xmlns:script:1.0',
      'form': 'urn:oasis:names:tc:opendocument:xmlns:form:1.0',
      'math': 'http://www.w3.org/1998/Math/MathML',
      'drawoo': 'http://openoffice.org/2010/draw',
      'calctext': 'urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0',
      'tableooo': 'http://openoffice.org/2009/table',
      'number': 'urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0'}

# Parse XML
for key in ns:
    ET.register_namespace(key, ns[key])

tree = ET.ElementTree()
tree.parse(tmp_dir + "content.xml")
root = tree.getroot()

for table_cell_style in root.findall(".//style:style[@style:family='table-cell']", ns):
    properties = table_cell_style.find("style:table-cell-properties", ns)
    properties.attrib['{%s}border' % ns['fo']] = "0.05pt solid #000000"

tree.write(tmp_dir + "content.xml")

# Compress tmp directory as odt
shutil.make_archive(dst, 'zip', tmp_dir)
shutil.move(dst + '.zip', dst)

# Remove tmp directory
shutil.rmtree(tmp_dir)

print("Successfully added borders to '", src, "'. File saved as '", dst, "'", sep="")
