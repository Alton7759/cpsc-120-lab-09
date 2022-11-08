#!/usr/bin/env python3
#
# Copyright 2021-2022 Michael Shafae
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
""" Check student's submission; requires the main file and the
    template file from the original repository. """
# pexpect documentation
#  https://pexpect.readthedocs.io/en/stable/index.html

# ex.
# .action/solution_check_p1.py  part-1 asgt

import difflib
import logging
import io
import math
import os
import os.path
import sys
import pexpect
from assessment import csv_solution_check_make, make
from logger import setup_logger


def run_p1(binary):
    """Run part-1"""
    logger = setup_logger()
    status = []
    error_values = (
        [None, 'error: you must give at least three scores'], # 0 arguments, too few
        ['1', 'error: you must give at least three scores'], # 1 argument, too few
        ['1', '2', 'error: you must give at least three scores'], # 2 arguments, too few
    )
    values = (
        [5, 5, 5, 5],  # all same
        [0, 0, 0, 0],  # zeroes
        [1, 2, 3, 2],  # 3 increasing
        [3, 2, 1, 2],  # 3 decreasing
        [5.1, 8.7, 9.0, 2.6, 1.9, 5.46667], # 5 floats

        # all 24 permutations of 3 5 7 8
        [3, 5, 7, 8, 6],
        [3, 5, 8, 7, 6],
        [3, 7, 5, 8, 6],
        [3, 7, 8, 5, 6],
        [3, 8, 5, 7, 6],
        [3, 8, 7, 5, 6],
        [5, 3, 7, 8, 6],
        [5, 3, 8, 7, 6],
        [5, 7, 3, 8, 6],
        [5, 7, 8, 3, 6],
        [5, 8, 3, 7, 6],
        [5, 8, 7, 3, 6],
        [7, 3, 5, 8, 6],
        [7, 3, 8, 5, 6],
        [7, 5, 3, 8, 6],
        [7, 5, 8, 3, 6],
        [7, 8, 3, 5, 6],
        [7, 8, 5, 3, 6],
        [8, 3, 5, 7, 6],
        [8, 3, 7, 5, 6],
        [8, 5, 3, 7, 6],
        [8, 5, 7, 3, 6],
        [8, 7, 3, 5, 6],
        [8, 7, 5, 3, 6],

        # minimum is duplicated, but should only be omitted once
        [3, 1, 1, 5, 2],

        # maximum is duplicated, but should only be omitted once
        [4, 2, 9, 9, 3, 5.33333],

    )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p1_error(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)

    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p1(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status

def _run_p1_error(binary, values):
    logger = setup_logger()
    status = False
    if values[0] is None:
        proc = pexpect.spawn(binary, timeout=1)
    else:
        argument_strings = list(map(str, values[:-1]))
        proc = pexpect.spawn(binary, timeout=1, args=argument_strings)

    expected = values[-1]

    with io.BytesIO() as log_stream:
        proc.logfile = log_stream
        try:
            regex = expected.replace(' ', '\\s+')
            proc.expect(
                fr'(?i).*{regex}.*'
            )
        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
            logger.error(f'Expected: "{expected}"')
            logger.error('Could not find expected output.')
            logger.error('Your output: "%s"', log_stream.getvalue().decode('utf-8'))
            logger.debug("%s", str(exception))
            logger.debug(str(proc))
            return status

        proc.expect(pexpect.EOF)
        proc.close()
        if proc.exitstatus == 0:
            logger.error("Expected: non-zero exit code.")
            logger.error(f'Exit code was {proc.exitstatus}.')
            logger.error("Program returned zero, but non-zero is required")
            logger.error('Your output: "%s"', log_stream.getvalue().decode('utf-8'))
            return status
    status = True
    return status    

def _run_p1(binary, values):
    """The actual test with the expected input and output"""
    logger = setup_logger()
    status = False
    argument_strings = list(map(str, values[:-1]))
    expected_float = values[-1]
    proc = pexpect.spawn(binary, timeout=1, args=argument_strings)
    # proc.logfile = sys.stdout.buffer

    with io.BytesIO() as log_stream:
        proc.logfile = log_stream
        try:

            match_index = proc.expect(r'(?i)\s*average\s*is\s*([-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?)\s*')

            token = proc.match.group(1).decode("utf-8") 
            actual = float(token)
            # 1% tolerance
            if not math.isclose(expected_float, actual, rel_tol=.01): 
                logging.error('actual numeric output is %f, which does not equal %f', actual, expected_float)
                return status

        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
            logger.error('Expected: "average is ' + str(expected_float) + '"')
            logger.error('Could not find expected output.')
            logger.error('Your output: "%s"', log_stream.getvalue().decode('utf-8'))
            logger.debug("%s", str(exception))
            logger.debug(str(proc))
            return status

        proc.expect(pexpect.EOF)
        proc.close()
        if proc.exitstatus != 0:
            logger.error("Expected: zero exit code.")
            logger.error(f'Exit code was {proc.exitstatus}.')
            logger.error("Program returned non-zero, but zero is required")
            logger.error('Your output: "%s"', log_stream.getvalue().decode('utf-8'))
            return status
        
    status = True
    return status

_120_ERRORS = '''Introduction
tasks,
programs;
programs;
assignment;
flow;
input/output;
functions;
Structured
object-oriented
methodologies.
'''

FOX_ERRORS = ''''''

LEOTA_ERRORS = '''Serpents
spiders,
rat,
spirits,
at!
Rap
-
respond.
Send
beyond...
Goblins
ghoulies
Halloween,
tambourine!
Creepies
crawlies,
pond,
beyond!
'''

LINCOLN_ERRORS = '''Four
continent,
nation,
Liberty,
equal.
Now
war,
nation,
dedicated,
endure.
We
battle-field
war.
We
field,
live.
It
this.
'''

def run_p2(binary):
    """Run part-2"""
    logger = setup_logger()
    status = []
    error_values = (
        [None, 'error: you must give a document filename'], # 0 arguments, too few
    )
    values = (
        ['120.txt', _120_ERRORS],
        ['fox.txt', FOX_ERRORS],
        ['leota.txt', LEOTA_ERRORS],
        ['lincoln.txt', LINCOLN_ERRORS]
    )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p1_error(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)

    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p2(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status


def _run_p2(binary, values):
    logger = setup_logger()
    status = False
    proc = pexpect.spawn(binary, timeout=1, args=[values[0]])
    expected_errors = values[1]
    expected_output = 'spelling errors:\n' + expected_errors

    with io.BytesIO() as log_stream:
        proc.logfile = log_stream
        try:
            regex = r'(?i).*spelling\s+errors\s*:\s*\n' + expected_errors.replace('\n', '\s+') + r'.*'
            proc.expect(regex)
        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
            logger.error(f'Expected: "{expected_output}"')
            logger.error('Could not find expected output.')
            logger.error('Your output: "%s"', log_stream.getvalue().decode('utf-8'))
            logger.debug("%s", str(exception))
            logger.debug(str(proc))
            return status

        proc.expect(pexpect.EOF)
        proc.close()
        if proc.exitstatus != 0:
            logger.error("Expected: zero exit code.")
            logger.error(f'Exit code was {proc.exitstatus}.')
            logger.error("Program returned non-zero, but zero is required")
            logger.error('Your output: "%s"', log_stream.getvalue().decode('utf-8'))
            return status
        
    status = True
    return status

tidy_opts = (
    '-checks="*,-misc-unused-parameters,'
    '-modernize-use-trailing-return-type,-google-build-using-namespace,'
    '-cppcoreguidelines-avoid-magic-numbers,-readability-magic-numbers,'
    '-fuchsia-default-arguments-calls,-clang-analyzer-deadcode.DeadStores,'
    '-bugprone-exception-escape"'
    ' -config="{CheckOptions: [{key: readability-identifier-naming.ClassCase, value: CamelCase}, '
    '{key: readability-identifier-naming.ClassMemberCase, value: lower_case}, '
    '{key: readability-identifier-naming.ConstexprVariableCase, value: CamelCase}, '
    '{key: readability-identifier-naming.ConstexprVariablePrefix, value: k}, '
    '{key: readability-identifier-naming.EnumCase, value: CamelCase}, '
    '{key: readability-identifier-naming.EnumConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.EnumConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.FunctionCase, value: CamelCase}, '
    '{key: readability-identifier-naming.GlobalConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.GlobalConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.StaticConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.StaticConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.StaticVariableCase, value: lower_case}, '
    '{key: readability-identifier-naming.MacroDefinitionCase, value: UPPER_CASE}, '
    '{key: readability-identifier-naming.MacroDefinitionIgnoredRegexp, value: \'^[A-Z]+(_[A-Z]+)*_$\'}, '
    '{key: readability-identifier-naming.MemberCase, value: lower_case}, '
    '{key: readability-identifier-naming.PrivateMemberSuffix, value: _}, '
    '{key: readability-identifier-naming.PublicMemberSuffix, value: \'\'}, '
    '{key: readability-identifier-naming.NamespaceCase, value: lower_case}, '
    '{key: readability-identifier-naming.ParameterCase, value: lower_case}, '
    '{key: readability-identifier-naming.TypeAliasCase, value: CamelCase}, '
    '{key: readability-identifier-naming.TypedefCase, value: CamelCase}, '
    '{key: readability-identifier-naming.VariableCase, value: lower_case}, '
    '{key: readability-identifier-naming.IgnoreMainLikeFunctions, value: 1}]}"'
)

if __name__ == '__main__':
    cwd = os.getcwd()
    repo_name = os.path.basename(os.path.dirname(cwd))

    if sys.argv[1] == 'part-1':
        csv_solution_check_make(
            csv_key=repo_name,
            target_directory=sys.argv[2],
            program_name=sys.argv[3],
            run=run_p1,
            # do_lint_check=False,
            tidy_options=tidy_opts,
        )
    elif sys.argv[1] == 'part-2':
        csv_solution_check_make(
            csv_key=repo_name,
            target_directory=sys.argv[2],
            program_name=sys.argv[3],
            run=run_p2,
            # do_lint_check=False,
            tidy_options=tidy_opts,
        )
    else:
        print('Error: no match.')
