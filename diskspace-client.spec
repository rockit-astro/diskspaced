Name:      onemetre-diskspace-client
Version:   1.1
Release:   1
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Disk space client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3

%description
Part of the observatory software for the Warwick one-meter telescope.

diskspace is a commandline utility that queries the disk space daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/diskspace %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/diskspace %{buildroot}/etc/bash_completion.d/diskspace

# Install python dependencies
# This is horrible, but it seems to be the only way that actually works!
pip3 install Pyro4

%files
%defattr(0755,root,root,-)
%{_bindir}/diskspace
/etc/bash_completion.d/diskspace

%changelog
