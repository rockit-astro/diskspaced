Name:      observatory-diskspace-server
Version:   20230605
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Disk usage server.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-diskspace python3-warwick-observatory-common

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/diskspaced %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/diskspaced@.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/diskspaced
%defattr(-,root,root,-)
%{_unitdir}/diskspaced@.service

%changelog
