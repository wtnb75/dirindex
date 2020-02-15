import os
import unittest
from click.testing import CliRunner
from dirindex._cli import cli
from dirindex.version import VERSION


class Test1(unittest.TestCase):
    def test1(self):
        self.assertFalse(False, "False is False")
        # self.assertTrue(False, "not Implemented")

    def testUsage(self):
        result = CliRunner().invoke(cli)
        self.assertIn("Usage", result.output)
        self.assertIn("make", result.output)
        self.assertIn("read-resource", result.output)

    def testVersion(self):
        result = CliRunner().invoke(cli, args=["--version"])
        self.assertIn("dirindex", result.output)
        self.assertIn("version", result.output)
        self.assertIn(VERSION, result.output)

    def testmake1(self):
        result = CliRunner().invoke(cli, args=["make", "--help"])
        self.assertIn("Usage", result.output)
        self.assertIn("make", result.output)
        self.assertIn("template", result.output)
        self.assertIn("hide", result.output)
        self.assertIn("filename", result.output)

    def testreadrsc1(self):
        result = CliRunner().invoke(cli, args=["read-resource", "apache"])
        self.assertIn("Index", result.output)

    def testreadrsc2(self):
        result = CliRunner().invoke(cli, args=["read-resource", ".gitignore"])
        self.assertIn("lib", result.output)
        self.assertIn("cover", result.output)

    def testmake2(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("test.txt", "w") as f:
                f.write("hello world\n")
            os.mkdir("testdir")
            with open("testdir/test2.txt", "w") as f:
                f.write("hello world\n")
            with open("testdir/ignore.txt", "w") as f:
                f.write("hello world\n")
            runner.invoke(
                cli, args=["make", "--template", "ls-l", "--filename", "lsl", "."])
            with open("lsl") as f:
                output = f.read()
                self.assertIn("-rw-r--r--", output)
                self.assertIn("test.txt", output)
                self.assertIn("testdir", output)
            runner.invoke(
                cli, args=["make", "--template", "ls-l", "--filename", "lsl", ".", "--recursive"])
            with open("testdir/lsl") as f:
                output = f.read()
                self.assertIn("-rw-r--r--", output)
                self.assertIn("test2.txt", output)
            runner.invoke(
                cli, args=["make", "--template", "ls-l", "--filename", "lsl", ".", "--recursive", "--single"])
            with open("lsl") as f:
                output = f.read()
                self.assertIn("-rw-r--r--", output)
                self.assertIn("test.txt", output)
                self.assertIn("testdir", output)
                self.assertIn("testdir/test2.txt", output)
            runner.invoke(
                cli, args=["make", "--template", "ls-l", "--filename", "lsl", ".", "--recursive", "--single", "--hide", "ignore.*"])
            with open("lsl") as f:
                output = f.read()
                self.assertIn("-rw-r--r--", output)
                self.assertIn("test.txt", output)
                self.assertIn("testdir", output)
                self.assertIn("testdir/test2.txt", output)
                self.assertNotIn("ignore", output)
            runner.invoke(
                cli, args=["make", "--template", "ls-l", "--filename", "lsl", ".", "--recursive", "--single", "--hide", "ignore.*", "--pattern", "*.txt", "--pattern", "testdir"])
            with open("lsl") as f:
                output = f.read()
                self.assertIn("-rw-r--r--", output)
                self.assertIn("test.txt", output)
                self.assertIn("testdir", output)
                self.assertIn("testdir/test2.txt", output)
                self.assertNotIn("ignore", output)
