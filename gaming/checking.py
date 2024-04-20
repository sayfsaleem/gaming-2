import MySQLdb
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('shah1001'),
    ssh_username='shah1001', ssh_password='Safiya12@',
    remote_bind_address=('shah1001.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='shah1001',
        passwd='hell123@',
        host='shah1001.mysql.pythonanywhere-services.com', port=tunnel.local_bind_port,
        db='shah1001$default',
    )
    # Do stuff
    connection.close()
