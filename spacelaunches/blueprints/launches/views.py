from flask import (
    Blueprint, 
    render_template
)

launches = Blueprint(
    'launches',
    __name__,
    template_folder='spaceluanches/templates',
)

@launches.route('/', methods=['GET'])
def main():
    return 'ciao'


