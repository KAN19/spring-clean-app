import xml.etree.ElementTree as ET

dependencies_to_add = [
    {
        "groupId": "org.springdoc",
        "artifactId": "springdoc-openapi-starter-webmvc-ui",
        "version": "2.8.4",
    },
    {
        "groupId": "org.apache.commons",
        "artifactId": "commons-lang3",
        "version": "3.12.0",
    },
    {
        "groupId": "com.cosium.spring.data",
        "artifactId": "spring-data-jpa-entity-graph",
        "version": "3.2.2",
    },
]


def add_dependencies_to_pom(pom_file_path):
    """Modify an existing pom.xml file to add new dependencies without duplication."""

    # Parse the existing pom.xml file
    tree = ET.parse(pom_file_path)
    root = tree.getroot()

    # Define Maven's XML namespace (Spring Initializr-generated POMs use this)
    namespace = {"mvn": "http://maven.apache.org/POM/4.0.0"}
    ET.register_namespace("", namespace["mvn"])

    # Locate the <dependencies> section, or create one if it doesn't exist
    dependencies_section = root.find("mvn:dependencies", namespace)
    if dependencies_section is None:
        dependencies_section = ET.SubElement(root, "dependencies")

    # Add new dependencies only if they don't already exist
    for dep in dependencies_to_add:
        exists = any(
            d.find("mvn:groupId", namespace).text == dep["groupId"]
            and d.find("mvn:artifactId", namespace).text == dep["artifactId"]
            for d in dependencies_section.findall("mvn:dependency", namespace)
        )
        if not exists:
            dependency_element = ET.SubElement(dependencies_section, "dependency")
            ET.SubElement(dependency_element, "groupId").text = dep["groupId"]
            ET.SubElement(dependency_element, "artifactId").text = dep["artifactId"]
            ET.SubElement(dependency_element, "version").text = dep["version"]

    # Save the updated pom.xml file
    tree.write(pom_file_path, encoding="utf-8", xml_declaration=True)
    print(f"✅ Dependencies successfully added to {pom_file_path}")
