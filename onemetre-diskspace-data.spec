Name:      onemetre-diskspace-data
Version:   20210910
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Diskspace configuration for the W1m telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/diskspaced/

%{__install} %{_sourcedir}/onemetre.json %{buildroot}%{_sysconfdir}/diskspaced/
%files
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/onemetre.json

%changelog
