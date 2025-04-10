import json
import os

import requests

# Replace with your Piazza credentials
EMAIL = "test_email@gmail.com"
PASSWORD = "test_pass"


def main():
    session = requests.Session()
    try:
        user_login(session, EMAIL, PASSWORD)
    except Exception as e:
        print(
            "Login failed. Check your login credentials in the Python script. Error: {}".format(
                e
            )
        )
        return

    resources_dir_name = "resources"

    # Create resources directory to save all resources to
    if not os.path.exists(resources_dir_name):
        os.mkdir(resources_dir_name)

    # Read file with links
    with open("resources_links.txt", "r") as url_file, open(
        "resources_names.txt", "r"
    ) as file_names_file:
        urls = list(filter(is_valid_line, url_file.readlines()))
        names = list(filter(is_valid_line, file_names_file.readlines()))

        for link, file_name in zip(urls, names):
            # Strip removes newlines and whitespaces on sides.
            file_name = os.path.join(resources_dir_name, file_name.strip())

            # Remove the new line symbol at the end
            link = link[:-1]
            print("downloading {}".format(file_name))
            r = session.get(link)
            file_name = append_file_extension(r, file_name)

            # Write to a file with specified name.
            # In case it exists, overwrite it.
            new_file = open(file_name, "wb")
            new_file.write(r.content)
            new_file.close()

            print("File {} was successfully saved".format(file_name))


def is_valid_line(line):
    s = line.strip()
    return not s.startswith("#") and not len(s) == 0


def append_file_extension(response, file_name):
    # Get the content type from the response headers
    content_type = response.headers.get("Content-Type", "")

    # Map the content type to a file extension
    mime_to_extension = {
        "application/pdf": ".pdf",
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "application/zip": ".zip",
        "application/msword": ".doc",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
        "text/csv": ".csv",
        "application/json": ".json",
        "audio/mpeg": ".mp3",
        # Add more MIME types as needed...
    }

    # Check if the content type is in the mapping
    extension = ""  # Default to no extension
    if content_type in mime_to_extension:
        extension = mime_to_extension[content_type]

    # Check if the file name already has an extension
    if not file_name.endswith(extension):
        file_name += extension

    return file_name


def user_login(session, email, password):
    # Inspired by https://github.com/hfaran/piazza-api/

    # Need to get the CSRF token first
    response = session.get("https://piazza.com/main/csrf_token")

    # Make sure a CSRF token was retrieved, otherwise bail
    if response.text.upper().find("CSRF_TOKEN") == -1:
        raise Exception("Could not get CSRF token")

    # Remove double quotes and semicolon (ASCI 34 & 59) from response string.
    # Then split the string on "=" to parse out the actual CSRF token
    csrf_token = response.text.translate({34: None, 59: None}).split("=")[1]

    # Log in using credentials and CSRF token and store cookie in session
    response = session.post(
        "https://piazza.com/class",
        data={
            "from": "/signup",
            "email": email,
            "password": password,
            "remember": "on",
            "csrf_token": csrf_token,
        },
    )

    # If non-successful http response, bail
    if response.status_code != 200:
        raise Exception(f"Could not authenticate.\n{response.text}")

    # Piazza might give a successful http response even if there is some other
    # kind of authentication problem. Need to parse the response html for error message
    pos = response.text.upper().find("VAR ERROR_MSG")
    errorMsg = None
    if pos != -1:
        end = response.text[pos:].find(";")
        errorMsg = (
            response.text[pos : pos + end].translate({34: None}).split("=")[1].strip()
        )

    if errorMsg is not None:
        raise Exception(f"Could not authenticate.\n{errorMsg}")


if __name__ == "__main__":
    main()
