step-1 sudo apt update && sudo apt upgrade -y
step-2 sudo apt install python3-pip python3-dev libpq-dev nginx curl python3-dev default-libmysqlclient-dev build-essential -y
step-3 sudo apt-get install python3-venv -y

database-related--> python3 manage.py dumpdata --exclude=contenttypes > datadump.json
                    python3 manage.py migrate
                    python3 manage.py loaddata datadump.json
