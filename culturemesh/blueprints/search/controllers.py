from flask import Blueprint, render_template, request
from culturemesh.client import Client
from culturemesh.blueprints.search.forms.search_forms import SearchForm
from culturemesh.utils import populate_network_with_location_names

from culturemesh.blueprints.search.utils import get_no_search_results_msg

search = Blueprint('search', __name__, template_folder='templates')

MAX_SUGGESTIONS = 5

@search.route("/", methods=['GET', 'POST'])
def render_search_page():

    if request.method == "GET":
        return render_template('search.html', form=SearchForm())

    # POST
    c = Client(mock=False)
    data = request.form

    if not SearchForm(data).validate():
        return render_template(
            'search.html',
            form=SearchForm(),
            msg="Could not process your search.  Did you leave a field blank?"
        )

    search_type = str(data.get('search_type'))

    language = None
    from_location = None

    if search_type == "location":
        from_location = data['origin_or_language']
        network_type_suggestions = c.location_autocomplete(from_location)
    elif search_type == "language":
        language = data['origin_or_language']
        network_type_suggestions = c.language_autocomplete(language)
    else:
        raise Exception("Invalid Search Type %s" % search_type)

    near_location = data['residence']
    current_location_suggestions = c.location_autocomplete(near_location)

    # Where there some suggestions?  If not tell the user.
    if not network_type_suggestions or not current_location_suggestions:
        msg = get_no_search_results_msg(
            search_type,
            network_type_suggestions,
            current_location_suggestions,
            data['origin_or_language'],
            data['residence']
        )

        return render_template(
            'search.html', form=SearchForm(), msg=msg
        )

    network_type_suggestions = network_type_suggestions[:min(
            MAX_SUGGESTIONS, len(network_type_suggestions)
    )]

    current_location_suggestions = current_location_suggestions[:min(
            MAX_SUGGESTIONS, len(current_location_suggestions)
    )]

    if search_type == "location":

        return render_template(
            'location_suggestions.html',
            location_suggestions=network_type_suggestions,
            current_location_suggestions=current_location_suggestions
        )
    elif search_type == "language":
        return render_template(
            'language_suggestions.html',
            language_suggestions=network_type_suggestions,
            current_location_suggestions=current_location_suggestions
        )
    else:
        raise Exception("Invalid Search Type %s" % search_type)


@search.route("/gotonetwork", methods=['POST'])
def go_to_network():
    print("HERE")
    return "hi"
    return str(request.form)
