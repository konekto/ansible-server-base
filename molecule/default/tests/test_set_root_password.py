import os
from passlib.hash import sha512_crypt
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_password_match(host):

    with host.sudo():
        f = host.file('/home/admin/.root_password')

        user_root_password = host.user('root').password

        user_root_password_parts = user_root_password.split('$')

        password_hash = sha512_crypt.using(rounds=5000, salt=user_root_password_parts[2]).hash(f.content_string)

        assert f.exists
        assert user_root_password == password_hash

