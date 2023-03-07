import os

from paramiko import SSHClient, SFTPClient, AutoAddPolicy
from zipfile import ZipFile

def transfer_dir(ssh: SSHClient, dir: str):
    sftp = ssh.open_sftp()

    home_path = '/home/odroid/frc'

    local_zip = f'{os.path.basename(dir)}.zip'
    remote_zip = f'{home_path}/{os.path.basename(dir)}.zip'

    z = ZipFile(local_zip, 'x')
    for root, dirs, files in os.walk(dir):
        for f in files:
            z.write(f'{root}/{f}', f'{os.path.relpath(root, dir)}/{f}')
            #z.write(os.path.join(root, f), 
            #        os.path.relpath(os.path.join(root, f),
            #                        os.path.join(dir)))
            
    z.close()
    

    try:
        sftp.mkdir(home_path)
    except:
        pass

    try:
        sftp.remove(remote_zip)
    except:
        pass

    try:
        sftp.rmdir(f'{home_path}/{os.path.basename(dir)}')
    except:
        pass

    sftp.put(localpath=f'./{local_zip}', remotepath=remote_zip)
    sftp.close()
    
    os.remove(local_zip)

    stdin, stdout, stderr = ssh.exec_command(f'unzip {remote_zip} -d {home_path}/{os.path.basename(dir)}')
    stdout.read()

    ssh.exec_command(f'rm {remote_zip}')

def main(hostname: str = 'odroid.local', username: str = 'odroid', password: str = 'odroid'):
    with SSHClient() as ssh:

        print('Connecting to the odroid via ssh...')
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        print('Connected!')

        print('Deploying programs to the odroid...')
        transfer_dir(ssh, './python-server')
        transfer_dir(ssh, './react-server')
        print('Transfer completed!')

if __name__ == '__main__':
    main()