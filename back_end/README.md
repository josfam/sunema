# sunema backend

---

## How to manually install and run the backend

1. If you have not already, clone this repository and navigate into it

```sh
git clone https://github.com/josfam/sunema && cd sunema
```

2. If a .env file is not present in the root of the directory, create one

```sh
touch .env && echo "TMDB_API_KEY=\"\"\nOPENWEATHER_MAP_API_KEY=\"\"\n" > .env
```

If you have TMDB and OpenWeatherMap API keys put those between the respective quotation marks in this `.env` file.
\
\
📌 The application still works even if you do not yet have API keys ([see this note](../README.md#note-about-api-keys))

3. Create a python virtual environment, and install dependencies

```sh
python3 -m venv venv-sunema \
&& source venv-sunema/bin/activate \
&& pip install -r requirements.txt
```

4. Start the backend flask server in a separate terminal

- On a linux computer

```sh
gnome-terminal -- bash -c "python3 -m back_end.api.v1.app"
```

- On a Mac

```sh
open -a Terminal "python3 -m back_end.api.v1.app"
```
\
\
**Output**: The terminal that opens should have output similar to this

```sh
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 807-382-903
```

---

You can now go on to run the frontend

---
