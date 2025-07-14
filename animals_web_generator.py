import json

def load_data(file_path):
    """Load JSON file"""
    with open(file_path,"r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')
#print(animals_data)
# print(f"Location: {", ".join(animal["locations"])}")    #split ist string → liste und join ist liste → string


def show_info(animals_data):

    output = ""  # define an empty string
    for animal in animals_data:
        output += "<li class='cards__item'>"
        output += f"<div class='card__title'>{animal.get('name')}<br/>\n</div>"
        output += "<p class='card__text'>"
        output += f"<strong>Diet:</strong> {animal.get('characteristics').get('diet')}<br/>\n"
        output += f"<strong>Location:</strong> {animal.get('locations')[0]}<br/>\n"
        output += f"<strong>Type:</strong> {animal.get('characteristics').get('type', '--')}<br/>\n"
        output += "\n"
        output += '</li>'
    return output

animal_info = show_info(animals_data)


def load_html(file):
    """Reading the content of the template"""
    with open(file, "r", encoding="utf-8") as html:
        return html.read()

template_html = load_html("animals_template.html")
final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animal_info)


def write_html(file):
    """Writing animal data to HTML file."""
    with open("animals.html", "w", encoding="utf-8") as html:
        html.write(final_html)

write_html("animals.html")
