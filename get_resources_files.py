import requests
import json
import os


def main():
    # Replace with your email and password here
    login_data = {"method": "user.login", "params": {"email": "test_email@gmail.com", "pass": "test_pass"}}
    session = requests.Session()
    r = session.post(
        "https://piazza.com/logic/api",
        data=json.dumps(login_data),
    )

    # A simple proofchecker
    if r.json()["result"] not in ["OK"]:
        raise Exception(
            "Login failed. Check your login details in \
                        the Python script."
        )

    resources_dir_name = "resources"

    # Create resources directory to save all resources to
    if not os.path.exists(resources_dir_name):
        os.mkdir(resources_dir_name)

    # Read file with links
    with open("resources_links.txt", "r") as url_file, open("resources_names.txt", "r") as file_names_file:
        urls = list(filter(is_valid_line, url_file.readlines()))
        names = list(filter(is_valid_line, file_names_file.readlines()))

        for (link, file_name) in zip(urls, names):
            # Strip removes newlines and whitespaces on sides.
            file_name = os.path.join(resources_dir_name, file_name.strip())

            # Remove the new line symbol at the end
            link = link[:-1]
            print("downloading {}".format(file_name))
            r = session.get(link)

            # Write to a file with specified name.
            # In case it exists, overwrite it.
            new_file = open(file_name, "wb")
            new_file.write(r.content)
            new_file.close()

            print("File {} was successfully saved".format(file_name))


def is_valid_line(line):
    s = line.strip()
    return not s.startswith("#") and not len(s) == 0


if __name__ == "__main__":
    main()
