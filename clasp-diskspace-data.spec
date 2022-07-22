Name:      clasp-diskspace-data
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Diskspace configuration for the CLASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/diskspaced/

%{__install} %{_sourcedir}/clasp.json %{buildroot}%{_sysconfdir}/diskspaced/


%files
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/clasp.json

%changelog
