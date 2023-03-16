

# Piazza-resources-downloader-NG

Provides a tool to download all resources linked in the Piazza resources panel.  Updated to work as of April 28, 2022. Feel free to let me know if it's not working anymore.

## Getting started

1. Have Python and Requests installed. You can do the latter through something like `pip install requests`.

2. Clone the repository.
```shell
git clone https://github.com/ClementTsang/piazza-downloader-NG 
```

3. Go to Piazza resources page which has the resources you want to download.

4. Copy the code in `fetch_urls_and_names.js` and execute it in the console. All it does is query and print out the files you wish to download.

   * For example, if you are using Chrome, press `F12` and go to the `Console` tab. If you are using Firefox, got to `Developer > Debugger` and then `Console`.
   * Copy and paste the aforementioned code, then press `Enter`.

5. You should see outputs in your console with links and with names. Replace the contents of `resources_links.txt` with your links. Do the same with `resources_names.txt` and your file names.

6. Edit your login details in the Python code, and execute it.

```python
login_data = {"method": "user.login", "params": {"email": "test_email@gmail.com", "pass": "test_pass"}}
```

```bash
cd piazza-downloader-NG
python get_resources_files.py
```

## Acknowledgement

This is a fork from [tianjiaoding](https://github.com/tianjiaoding/piazza-downloader-NG)'s work, which in turn is based on work from [warmspringwinds](https://github.com/warmspringwinds/piazza_resources_downloader).
