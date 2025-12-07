import os


def generate_invitations(template, attendees):
    """
    This module generates personalized invitation files
    from a template and a list of attendees.
    """

    # type checking (Input Validation)
    # it must ensure template is a string and attendees is a list of dicts.
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees provided is not a list of dictionaries.")
        return

    # empty input checks
    # check if the template string is empty (or just whitespace)
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # check if the list has zero items
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # process Each Attendee
    # enumerate(attendees, 1) gives us the index starting at 1 (1, 2, 3...)
    for index, attendee in enumerate(attendees, 1):

        # it starts with the raw template for this specific person
        content = template

        # it defines the placeholders we expect to find
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            # get the value from the dictionary.
            # .get(key) returns None if the key is missing entirely.
            value = attendee.get(key)

            # requirement: if value is missing (None)
            # or empty, replace with "N/A"
            if value is None or value == "":
                value = "N/A"

            # replace the placeholder {key} with the actual string value
            # example: "{name}" becomes "Alice"
            content = content.replace("{" + key + "}", str(value))

        # write to file
        # construct the filename: output_1.txt, output_2.txt, etc.
        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
