# Copyright 2020 AppScale Systems, Inc
# SPDX-License-Identifier: BSD-2-Clause
from awscli_plugin_logs_tail.tail import TailCommand

def awscli_initialize(cli):
    cli.register('building-command-table.logs', inject_tail_command)

def inject_tail_command(command_table, session, **kwargs):
    command_table['tail'] = TailCommand(session)
