from paramiko.client import SSHClient
from paramiko.client import SSHClient, AutoAddPolicy


class SshConnectivity:

    def __init__(self, hostname, port=2222, username='kali', password='kali'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.connection = SSHClient()
        self.connection.set_missing_host_key_policy(AutoAddPolicy())

    def __enter__(self):
        self.connection.connect(
            hostname=self.hostname,
            port=self.port,
            username=self.username,
            password=self.password)
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        return False

    def execute_command_at_host(self, command):
        stdin, stdout, stderr = self.connection.exec_command(command)
        return stdout.read().decode('utf-8')


if __name__ == "__main__":
    with SshConnectivity(hostname='127.0.0.1') as ssh:
        result = ssh.execute_command_at_host('pwd')
        print(result)
