import json

def load_data(file_path):
    """Load JSON file and return parsed data"""
    with open(file_path,"r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')


def serialize_animal(animal):
    """Generate HTML list item for a single animal."""
    output = "<li class='cards__item'>"
    output += f"<div class='card__title'>{animal.get('name')}<br/>\n</div>"
    output += "<p class='card__text'>"
    output += f"<strong>Diet:</strong> {animal.get('characteristics').get('diet')}<br/>\n"
    output += f"<strong>Location:</strong> {animal.get('locations')[0]}<br/>\n"
    output += f"<strong>Type:</strong> {animal.get('characteristics').get('type', '--')}<br/>\n"
    output += "</p>"
    output += "</li>"
    return output


def show_info(animals_data):
    """Generate HTML list items with animal information."""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    return output

animal_info = show_info(animals_data)

def load_html(file):
    """Reading the content of the HTML template file"""
    with open(file, "r", encoding="utf-8") as html:
        return html.read()

template_html = load_html("animals_template.html")
final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animal_info)


def write_html(file):
    """Writing the final HTML content to a file"""
    with open("animals.html", "w", encoding="utf-8") as html:
        html.write(final_html)

write_html("animals.html")



