"""
Contains utility routines for the search page.
"""

def get_no_search_results_msg(search_type,
                              network_type_suggestions,
                              current_location_suggestions,
                              network_type_query,
                              current_location_query):

    if search_type not in ['location', 'language']:
        raise ValueError

    if network_type_suggestions and current_location_suggestions:
        raise ValueError

    msg = "Your search for \"%s\" did not match any results. \
           Make sure you spelled things correctly, or try another \
           language/location."

    if not network_type_suggestions and not current_location_suggestions:
        if search_type == 'location':
            sub_msg = "people from %s in %s"
        else:
            sub_msg = "people who speak %s in %s"
        msg = msg % (sub_msg % (network_type_query, current_location_query))
    elif not network_type_suggestions:
        if search_type == 'location':
            sub_msg = "people from %s"
        else:
            sub_msg = "people who speak %s"
        msg = msg % (sub_msg % (network_type_query))
    elif not current_location_suggestions:
        sub_msg = "people in %s"
        msg = msg % (sub_msg % (current_location_query))

    return msg
