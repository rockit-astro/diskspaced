Name:      observatory-diskspace-client
Version:   2.2.1
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Disk space client for the Warwick one-metre and RASA prototype telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common

%description
Part of the observatory software for the Warwick one-meter and RASA prototype telescopes.

diskspace is a commandline utility that queries the disk space daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/diskspace %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/diskspace %{buildroot}/etc/bash_completion.d/diskspace

%files
%defattr(0755,root,root,-)
%{_bindir}/diskspace
/etc/bash_completion.d/diskspace

%changelog
