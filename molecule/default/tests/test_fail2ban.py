import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fail2ban_installed(host):

    assert host.package('fail2ban-firewalld').is_installed


def test_fail2ban_sshd_fail_active(host):

    with host.sudo():
        status_sshd = host.command('fail2ban-client status sshd')
        assert 'sshd' in status_sshd.stdout

