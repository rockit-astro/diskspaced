## Disk usage daemon

`diskspaced` is a Pyro frontend for querying the current disk usage.

`diskspace`  is a commandline utility that queries the disk space daemon.

### Configuration

Configuration is read from json files that are installed by default to `/etc/diskspaced`.
A configuration file is specified when launching the server, and the `diskspace` frontend will search this location when launched.

The configuration options are:
```python
{
  "daemon": "localhost_test2", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "diskspaced@test", # The name to use when writing messages to the observatory log.
  "data_root_path": "/home/ops" # The file system path to monitor.
}
```

### Initial Installation

The automated packaging scripts will push 8 RPM packages to the observatory package repository:

| Package                         | Description                                                           |
|---------------------------------|-----------------------------------------------------------------------|
| rockit-diskspace-server         | Contains the `diskspaced` server and systemd service file.            |
| rockit-diskspace-client         | Contains the `diskspace` commandline utility for querying the server. |
| rockit-diskspace-data-clasp     | Contains the json configuration for the CLASP DAS machine.            |
| rockit-diskspace-data-halfmetre | Contains the json configuration for the half metre TCS.               |
| rockit-diskspace-data-onemetre  | Contains the json configuration for the W1m TCS.                      |
| rockit-diskspace-data-sting     | Contains the json configuration for the STING DAS machines.           |
| rockit-diskspace-data-warwick   | Contains the json configuration for the Windmill Hill TCS.            |
| python3-rockit-diskspace        | Contains the python module with shared code.                          |

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
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the server config.

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
./diskspaced config/test.json
DISKSPACED_CONFIG_PATH=./config/test.json ./diskspace status
```
