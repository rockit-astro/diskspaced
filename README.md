## W1m disk usage daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/diskspaced.svg?branch=master)](https://travis-ci.org/warwick-one-metre/diskspaced)

Part of the observatory software for the Warwick one-meter telescope.

`diskspaced` is a Pyro frontend for querying the current disk usage.

`diskspace`  is a commandline utility that queries the disk space daemon.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

After installing `onemetre-diskspace-server`, the `diskspaced` must be enabled using:
```
sudo systemctl enable diskspaced.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start diskspaced.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9008/tcp --permanent
sudo firewall-cmd --reload
```
