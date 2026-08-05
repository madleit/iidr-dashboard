import subprocess
import tempfile
import time

CHCCLP_JAR = "/classic-chcclp/chcclp.jar"

def execute(script):
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".chcclp",
        delete=False
    ) as f:
        f.write(script)
        filename = f.name

    result = subprocess.run(
        [
            "java",
            "-jar",
            CHCCLP_JAR,
            "-f",
            filename
        ],
        capture_output=True,
        text=True
    )

    return result.stdout


def list_datastores():
    script = '''
chcclp session set to cdc;
connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";
list datastores;
exit;
'''
    return execute(script)


def list_subscriptions():
    script = '''
chcclp session set to cdc;
connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

list subscriptions;
exit;
'''
    return execute(script)


def monitor_replication():
    script = '''
chcclp session set to cdc;
connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

monitor replication;
exit;
'''
    return execute(script)


def monitor_latency():
    script = '''
chcclp session set to cdc;
connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select subscription name SYSLAB;

monitor subscription latency;
exit;
'''
    return execute(script)


def source_events():
    script = '''
chcclp session set to cdc;
connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select subscription name SYSLAB;

list subscription events type source count 50;
exit;
'''
    return execute(script)


def target_events():
    script = '''
chcclp session set to cdc;
connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select subscription name SYSLAB;

list subscription events type target count 50;
exit;
'''
    return execute(script)


def dashboard_data_raw():
    script = '''
chcclp session set to cdc;

connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

list datastores;

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

list subscriptions;

monitor replication;

select subscription name SYSLAB;

monitor subscription latency;

list subscription events type source count 10;

list subscription events type target count 10;

list table mappings;

show datastore name CDC_SRC;

show datastore name CDC_TGT;

select table mapping
sourceTable customers;

show table mapping;

exit;
'''

    return execute(script)

def start_mirroring():

    script = '''
chcclp session set to cdc;

connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select subscription name SYSLAB;

start mirroring;

exit;
'''

    execute(script)

    return {
        "action": "start_mirroring",
        "success": True,
        "message": "Command submitted"
    }

def end_replication():

    script = '''
chcclp session set to cdc;

connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select subscription name SYSLAB;

end replication;

exit;
'''

    execute(script)

    return {
        "action": "end_replication",
        "success": True,
        "message": "Command submitted"
    }

def show_datastore(name,context):

    script = f'''
chcclp session set to cdc;

connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";
connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select datastore
name { name }
context { context };

show datastore name {name};

exit;
'''

    return execute(script)

def datastore_health_raw():

    script = '''
chcclp session set to cdc;

connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select datastore
name CDC_SRC
context source;

show datastore name CDC_SRC;

select datastore
name CDC_TGT
context target;

show datastore name CDC_TGT;

exit;
'''

    return execute(script)

def table_mappings_raw():

    script = '''
chcclp session set to cdc;

connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select subscription
name SYSLAB;

list table mappings;

exit;
'''

    return execute(script)

def table_mapping_details_raw():

    script = '''
chcclp session set to cdc;

connect server hostname "192.168.56.104"
port 10101
username "admin"
password "2wh8wk2&";

connect datastore
name CDC_SRC
context source;

connect datastore
name CDC_TGT
context target;

select subscription
name SYSLAB;

select table mapping
sourceTable customers;

show table mapping;

exit;
'''

    return execute(script)