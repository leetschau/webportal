import daemon
import portal

ROOT = 'https://www.newfairs.com'
PORT = 8000
logfile = 'server.log'

if __name__ == '__main__':
    logger = open(logfile, 'w+')
    with daemon.DaemonContext(stdout=logger, stderr=logger):
        portal.main(ROOT, PORT)
