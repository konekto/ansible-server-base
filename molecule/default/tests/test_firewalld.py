import os
from passlib.hash import sha512_crypt
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_firewalld_installed(host):

    assert host.package('firewalld').is_installed


def test_firewalld_running_and_enabled(host):

    f = host.service('firewalld')

    assert f.is_running
    assert f.is_enabled


def test_firewalld_configuration(host):

    with host.sudo():

        firewalldconf = host.file('/etc/firewalld/firewalld.conf')

        assert firewalldconf.exists
        assert 'DefaultZone=public' in firewalldconf.content_string

        publiczone = host.file('/etc/firewalld/zones/public.xml')

        assert publiczone.exists

        assert '<service name="ssh"/>' in publiczone.content_string
        assert '<service name="http"/>' in publiczone.content_string
        assert '<service name="https"/>' in publiczone.content_string


def test_fail2ban_running_and_enabled(host):

    f = host.service('fail2ban')

    assert f.is_running
    assert f.is_enabled

