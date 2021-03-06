# -*- coding: utf-8
"""Steps for behavioral style tests are defined in this module.

Each step is defined by the string decorating it. This string is used
to call the step in "*.feature" file.

"""
from __future__ import unicode_literals

import wrappers
from behave import when, then
from textwrap import dedent


@when('we create table')
def step_create_table(context):
    """Send create table."""
    context.cli.sendline('create table a(x text);')


@when('we insert into table')
def step_insert_into_table(context):
    """Send insert into table."""
    context.cli.sendline('''insert into a(x) values('xxx');''')


@when('we update table')
def step_update_table(context):
    """Send insert into table."""
    context.cli.sendline('''update a set x = 'yyy' where x = 'xxx';''')


@when('we select from table')
def step_select_from_table(context):
    """Send select from table."""
    context.cli.sendline('select * from a;')


@when('we delete from table')
def step_delete_from_table(context):
    """Send deete from table."""
    context.cli.sendline('''delete from a where x = 'yyy';''')
    wrappers.expect_exact(
        context, 'You\'re about to run a destructive command.\r\nDo you want to proceed? (y/n):', timeout=2)
    context.cli.sendline('y')


@when('we drop table')
def step_drop_table(context):
    """Send drop table."""
    context.cli.sendline('drop table a;')
    wrappers.expect_exact(
        context, 'You\'re about to run a destructive command.\r\nDo you want to proceed? (y/n):', timeout=2)
    context.cli.sendline('y')


@then('we see table created')
def step_see_table_created(context):
    """Wait to see create table output."""
    wrappers.expect_pager(context, 'Query OK, 0 rows affected\r\n', timeout=2)


@then('we see record inserted')
def step_see_record_inserted(context):
    """Wait to see insert output."""
    wrappers.expect_pager(context, 'Query OK, 1 row affected\r\n', timeout=2)


@then('we see record updated')
def step_see_record_updated(context):
    """Wait to see update output."""
    wrappers.expect_pager(context, 'Query OK, 1 row affected\r\n', timeout=2)


@then('we see data selected')
def step_see_data_selected(context):
    """Wait to see select output."""
    wrappers.expect_pager(
        context, dedent("""\
            +-----+\r
            | x   |\r
            +-----+\r
            | yyy |\r
            +-----+\r
            1 row in set\r
            """), timeout=1)


@then('we see record deleted')
def step_see_data_deleted(context):
    """Wait to see delete output."""
    wrappers.expect_pager(context, 'Query OK, 1 row affected\r\n', timeout=2)


@then('we see table dropped')
def step_see_table_dropped(context):
    """Wait to see drop output."""
    wrappers.expect_pager(context, 'Query OK, 0 rows affected\r\n', timeout=2)
