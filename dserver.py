import daemon
import portal

logfile = 'server.log'

if __name__ == '__main__':
    logger = open(logfile, 'a')
    with daemon.DaemonContext(stdout=logger, stderr=logger):
        portal.main()
