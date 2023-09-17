from flask import Blueprint
from flask import render_template

import games.adapters.repository as repo
import games.browse.services as services

# Configure Blueprint.
browse_blueprint = Blueprint(
    'games_bp', __name__)


@browse_blueprint.route('/browse', methods=['GET'])
def browse_games():
    num_games = services.get_number_of_games(repo.repo_instance)
    all_games = services.get_games(repo.repo_instance)
    return render_template(
        'browse.html',
        # Custom page title
        title=f'Browse Games | CS235 Game Library',
        # Page heading
        heading='Browse Games',
        games=all_games,
        num_games=num_games,
    )