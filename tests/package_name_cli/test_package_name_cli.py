import subprocess

def test_package_name_cli_sanity():
    assert subprocess.run(["package_name_cli"]).returncode == 0
