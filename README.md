## Disk usage daemon

`diskspaced` is a Pyro frontend for querying the current disk usage.

`diskspace`  is a commandline utility that queries the disk space daemon.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the software architecture and instructions for developing and deploying the code.

### Configuration

Configuration is read from json files that are installed by default to `/etc/diskspaced`.
A configuration file is specified when launching the server, and the `diskspace` frontend will search this location when launched.

The configuration options are:
```python
{
  "daemon": "localhost_test2", # Run the server as this daemon. Daemon types are registered in `warwick.observatory.common.daemons`.
  "log_name": "diskspaced@test", # The name to use when writing messages to the observatory log.
  "data_root_path": "/home/ops" # The file system path to monitor.
}
```

### Initial Installation

The automated packaging scripts will push 6 RPM packages to the observatory package repository:

| Package                               | Description                                                           |
|---------------------------------------|-----------------------------------------------------------------------|
| observatory-diskspace-server          | Contains the `diskspaced` server and systemd service file.            |
| observatory-diskspace-client          | Contains the `diskspace` commandline utility for querying the server. |
| python3-warwick-observatory-diskspace | Contains the python module with shared code.                          |
| onemetre-diskspace-data               | Contains the json configuration for the W1m TCS.                      |
| halfmetre-diskspace-data              | Contains the json configuration for the half metre TCS.               |
| clasp-diskspace-data                  | Contains the json configuration for the CLASP TCS.                    |
| superwasp-diskspace-data              | Contains the json configuration for the SuperWASP TCS.                |

The `observatory-diskspace-server` and `observatory-diskspace-client` and `onemetre-diskspace-data` packages should be installed on the `onemetre-tcs` machine.

The `observatory-diskspace-server` and `observatory-diskspace-client` and `clasp-diskspace-data` packages should be installed on the `clasp-tcs` machine.

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now diskspaced@<config>
```

where `config` is the name of the json file for the appropriate telescope.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `warwick.observatory.common.daemons` for the daemon specified in the server config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart diskspaced@<config>
```

### Testing Locally

The camera server and client can be run directly from a git clone:
```
./diskspaced test.json
DISKSPACED_CONFIG_PATH=./test.json ./diskspace status
```
