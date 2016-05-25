Name:      onemetre-diskspace-server
Version:   1.3
Release:   4
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Disk usage server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick one-meter telescope.

diskspaced is a Pyro frontend for querying the current disk usage.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/diskspaced %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/diskspaced.service %{buildroot}%{_unitdir}

%pre
%service_add_pre diskspaced.service

%post
%service_add_post diskspaced.service
%fillup_and_insserv -f -y diskspaced.service

%preun
%stop_on_removal diskspaced.service
%service_del_preun diskspaced.service

%postun
%restart_on_update diskspaced.service
%service_del_postun diskspaced.service

%files
%defattr(0755,root,root,-)
%{_bindir}/diskspaced
%defattr(-,root,root,-)
%{_unitdir}/diskspaced.service

%changelog
