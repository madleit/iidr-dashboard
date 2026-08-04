from app.chcclp import execute

SCRIPT = '''
chcclp session set to cdc;

connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

list datastores;

exit;
'''

print(
    execute(SCRIPT)
)
