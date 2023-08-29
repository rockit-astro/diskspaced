Name:      rockit-diskspace
Version:   %{_version}
Release:   1
Summary:   Disk usage monitor.
Url:       https://github.com/rockit-astro/diskspaced
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/diskspaced/

%{__install} %{_sourcedir}/diskspaced %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/diskspace %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/diskspaced@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/diskspace %{buildroot}/etc/bash_completion.d/diskspace

%{__install} %{_sourcedir}/config/clasp.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/config/halfmetre.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/config/onemetre.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/config/superwasp_cam1.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/config/superwasp_cam2.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/config/superwasp_cam3.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/config/superwasp_cam4.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/config/warwick.json %{buildroot}%{_sysconfdir}/diskspaced/

%package server
Summary:  Disk usage server
Group:    Unspecified
Requires: python3-rockit-diskspace
%description server

%package client
Summary:  Disk usage client
Group:    Unspecified
Requires: python3-rockit-diskspace
%description client

%files server
%defattr(0755,root,root,-)
%{_bindir}/diskspaced
%defattr(-,root,root,-)
%{_unitdir}/diskspaced@.service

%files client
%defattr(0755,root,root,-)
%{_bindir}/diskspace
/etc/bash_completion.d/diskspace

%package data-clasp
Summary: Disk usage configuration for CLASP telescope
Group:   Unspecified
%description data-clasp

%files data-clasp
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/clasp.json

%package data-halfmetre
Summary: Disk usage configuration for the half metre telescope
Group:   Unspecified
%description data-halfmetre

%files data-halfmetre
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/halfmetre.json

%package data-onemetre
Summary: Disk usage configuration for the W1m telescope
Group:   Unspecified
%description data-onemetre

%files data-onemetre
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/onemetre.json

%package data-superwasp
Summary: Disk usage configuration for the SuperWASP telescope
Group:   Unspecified
%description data-superwasp

%files data-superwasp
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/superwasp_cam1.json
%{_sysconfdir}/diskspaced/superwasp_cam2.json
%{_sysconfdir}/diskspaced/superwasp_cam3.json
%{_sysconfdir}/diskspaced/superwasp_cam4.json

%package data-warwick
Summary: Disk usage configuration for the Windmill Hill observatory
Group:   Unspecified
%description data-warwick

%files data-warwick
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/warwick.json

%changelog
