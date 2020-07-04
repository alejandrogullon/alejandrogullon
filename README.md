### Create new environment
```bash
virtualenv -p python3 testing_env 
```
### Init environment
```
source testing_env/bin/activate
```   
### Install packages
```
pip3 install -r requirements.txt
```
### Run server
```
python3 manage.py runserver 0:8000
```