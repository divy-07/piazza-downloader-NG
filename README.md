

# Piazza-resources-downloader-NG

Provides a tool to download all resources linked in the Piazza resources panel.

## Improvements in this fork
As of April 09, 2025, this fork has been updated to work with the latest Piazza API changes. The following improvements have been made:

- Fixed login errors by adding CSRF support.
- Save files with correct filetype extension if not provided in the filename.
   - Supported filetypes: `pdf`, `jpg`, `png`, `zip`, `doc`, `docx`, `csv`, `json`, `mp3`.
   - Rest will default to no file extension (unless already specified in file name).

## Getting started

1. Have Python and Requests installed. You can do the latter through something like `pip install requests`.

2. Clone the repository.
```shell
git clone https://github.com/divy-07/piazza-downloader-NG.git
```

3. Go to Piazza resources page which has the resources you want to download.

4. Copy the code in `fetch_urls_and_names.js` and execute it in the console. All it does is query and print out the files you wish to download.

   * For example, if you are using Chrome, press `F12` and go to the `Console` tab. If you are using Firefox, got to `Developer > Debugger` and then `Console`.
   * Copy and paste the aforementioned code, then press `Enter`.

5. You should see outputs in your console with links and with names. Replace the contents of `resources_links.txt` with your links. Do the same with `resources_names.txt` and your file names.

6. Edit your login details in the Python code, and execute it.

```python
EMAIL = "test_email@gmail.com"
PASSWORD = "test_pass"
```

```bash
cd piazza-downloader-NG
python get_resources_files.py
```

## Acknowledgement

- This is a fork from [ClementTsang](https://github.com/ClementTsang/piazza-downloader-NG), which in turn is a fork of [tianjiaoding](https://github.com/tianjiaoding/piazza-downloader-NG)'s work, which in turn is based on work from [warmspringwinds](https://github.com/warmspringwinds/piazza_resources_downloader).

- A lot of the login code was inspired by [the unofficial piazza API client](https://github.com/hfaran/piazza-api/)
