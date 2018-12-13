import os
from passlib.hash import sha512_crypt
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_python_version(host):
    assert host.file('/usr/bin/python3.6').exists

def test_pip_packages(host):
    packages = host.pip_package.get_packages(pip_path='pip3.6')

    assert 'docker' in packages
    assert 'setuptools' in packages
