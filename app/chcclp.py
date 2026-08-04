import subprocess
import tempfile

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

exit;
'''

    return execute(script)
