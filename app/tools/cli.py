import logging
import os
import glob

from flask.cli import AppGroup
from flask import current_app

# CLI group 
log_cli = AppGroup('log', help='Log commands')


@log_cli.command("clean", help="Clean log")
def clean_log():
    logdir = current_app.config["LOG_DIR"]
    for filename in os.listdir(logdir):
        file_path = os.path.join(logdir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print(logdir + ' is clean')



@log_cli.command("archive", help="Archive in targz log dir")
def archive_log():
    print("TO DO")


