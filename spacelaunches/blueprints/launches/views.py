from flask import (
    Blueprint, 
    render_template,
    current_app
)


launches = Blueprint(
    'launches',
    __name__,
    template_folder='spaceluanches/templates',
)

@launches.route('/', methods=['GET'])
def main():
    launches = current_app.config['launchesAPI'].getLaunchesDetails()
    print(launches)
    return render_template('lastLaunch.html', missionName=launches['mission']['name'])


