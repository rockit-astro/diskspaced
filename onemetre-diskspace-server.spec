Name:      onemetre-diskspace-server
Version:   2.1.1
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Disk usage server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick one-metre telescope.

diskspaced is a Pyro frontend for querying the current disk usage.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/diskspaced %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/diskspaced.service %{buildroot}%{_unitdir}

%post
%systemd_post diskspaced.service

%preun
%systemd_preun diskspaced.service

%postun
%systemd_postun_with_restart diskspaced.service

%files
%defattr(0755,root,root,-)
%{_bindir}/diskspaced
%defattr(-,root,root,-)
%{_unitdir}/diskspaced.service

%changelog
