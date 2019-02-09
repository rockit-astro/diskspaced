Name:      rasa-diskspace-server
Version:   2.2.0
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Disk usage server for the RASA prototype telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the RASA prototype telescope.

diskspaced is a Pyro frontend for querying the current disk usage.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/diskspaced %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/rasa-diskspaced.service %{buildroot}%{_unitdir}

%post
%systemd_post rasa-diskspaced.service

%preun
%systemd_preun rasa-diskspaced.service

%postun
%systemd_postun_with_restart rasa-diskspaced.service

%files
%defattr(0755,root,root,-)
%{_bindir}/diskspaced
%defattr(-,root,root,-)
%{_unitdir}/rasa-diskspaced.service

%changelog
