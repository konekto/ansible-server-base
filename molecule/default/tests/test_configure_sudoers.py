import os
from passlib.hash import sha512_crypt
import testinfra.utils.ansible_runner

runner = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE'])
testinfra_hosts = runner.get_hosts('all')


def test_check_sudoers_file(host):

    with host.sudo():

        f = host.file('/etc/sudoers.d/admins')

        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert 'admin ALL=(ALL) ALL' in f.content_string
