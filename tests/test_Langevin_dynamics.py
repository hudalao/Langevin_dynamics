#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_Langevin_dynamics
----------------------------------

Tests for `Langevin_dynamics` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from Langevin_dynamics import Langevin_dynamics
from Langevin_dynamics import cli
from Langevin_dynamics import PotEneGenSqu
import numpy as np

class TestLangevin_dynamics(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'Langevin_dynamics.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_input(self):
        input_test = [1.0, 0.0, 1.0, 1.0, 0.01, 10.0, 1.0]
        input_proj = Langevin_dynamics.Langevin_dynamics().tran_input_float('input1.txt')
        self.assertEqual(input_test, input_proj)

    def test_potential_output_length(self):
        size_assigned = int(8 / 0.001 + 1)
        inputpot = PotEneGenSqu.Pot_Energy_Gen(0.001, 8, 5, 1)
        pot = inputpot.pot()
        force = inputpot.force()
        size_pot = np.size(pot)
        size_force = np.size(force)
        self.assertEqual(size_assigned, size_pot)
        self.assertEqual(size_assigned, size_force)

    def test_energy_conservation(self):
        LdLd = Langevin_dynamics.Langevin_dynamics()
        inputdata = np.genfromtxt('potential_energy_squarex.txt')
        N = np.size(inputdata, 0)
        Fp = np.zeros(N)
        X_pot = np.zeros(N)
        for line in range(N):
            X_pot[line] = round (inputdata[line][1], 3)
            Fp[line] = inputdata[line][3]
        output_data = LdLd.dynamics(1.0, 0, 1.0, 0, 0.001, 10, 5, 8, X_pot, Fp, int(10 / 0.001 + 1))  #set damp to 0
        t_arr, X, V = output_data
        Energy = 5 * V ** 2 / 2 + (5 - (X - 4) ** 2) **2
        Energy_assigned = [16, 17]
        for ii in range(np.size(Energy, 0)):
            self.assertIn(round(Energy[ii]), Energy_assigned)
        

if __name__ == '__main__':
    sys.exit(unittest.main())
