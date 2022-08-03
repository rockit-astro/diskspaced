Name:      superwasp-diskspace-data
Version:   20220803
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Diskspace configuration for the SuperWASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/diskspaced/

%{__install} %{_sourcedir}/superwasp_cam1.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/superwasp_cam2.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/superwasp_cam3.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/superwasp_cam4.json %{buildroot}%{_sysconfdir}/diskspaced/

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/superwasp_cam1.json
%{_sysconfdir}/diskspaced/superwasp_cam2.json
%{_sysconfdir}/diskspaced/superwasp_cam3.json
%{_sysconfdir}/diskspaced/superwasp_cam4.json

%changelog
