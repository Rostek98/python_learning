from SSH_connection import SshConnectivity

class FileManager():
    def __init__(self, connection):
        self.connection = connection
        self.sftp = connection.open_sftp()

    def send_file_to_remote_host(self, localpath, remotepath):
        return self.sftp.put(localpath, remotepath)

with SshConnectivity(hostname='127.0.0.1') as ssh:
    fm = FileManager(connection=ssh.connection)
    fm.send_file_to_remote_host(localpath=r"D:\Python\python_knowledge_base\Connectivity\text.txt",
                                 remotepath='/home/kali/Downloads/new_file'
                                 )

