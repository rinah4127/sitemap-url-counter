import xml.etree.ElementTree as ET

def count_locs(xml_text: str) -> int:
    root = ET.fromstring(xml_text)
    return sum(1 for el in root.iter() if el.tag.endswith("loc"))

if __name__ == "__main__":
    print(count_locs("<urlset><url><loc>https://example.com/</loc></url></urlset>"))
