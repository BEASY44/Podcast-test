import xml.etree.ElementTree as xml_tree
import yaml

with open('feed.yaml', 'r') as f:
    yaml_data = yaml.safe_load(f)

rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
})

channel_element = xml_tree.SubElement(rss_element, 'channel')
xml_tree.SubElement(channel_element, 'title').text = yaml_data.get('title', '')
xml_tree.SubElement(channel_element, 'format').text = yaml_data.get('format', '')
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data.get('subtitle', '')
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data.get('author', '')
xml_tree.SubElement(channel_element, 'description').text = yaml_data.get('description', '')

if 'image' in yaml_data:
    xml_tree.SubElement(channel_element, 'itunes:image', {'href': yaml_data['image']})

xml_tree.SubElement(channel_element, 'language').text = yaml_data.get('language', '')
xml_tree.SubElement(channel_element, 'link').text = yaml_data.get('link', '')

if 'category' in yaml_data:
    xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']})

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
