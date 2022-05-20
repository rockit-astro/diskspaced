Name:      clasp-diskspace-data
Version:   20220520
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Disk usage server.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/diskspaced/

%{__install} %{_sourcedir}/clasp1.json %{buildroot}%{_sysconfdir}/diskspaced/
%{__install} %{_sourcedir}/clasp2.json %{buildroot}%{_sysconfdir}/diskspaced/

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/clasp1.json
%{_sysconfdir}/diskspaced/clasp2.json

%changelog
