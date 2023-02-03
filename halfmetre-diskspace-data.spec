Name:      halfmetre-diskspace-data
Version:   20230203
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Diskspace configuration for the half metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/diskspaced/

%{__install} %{_sourcedir}/halfmetre.json %{buildroot}%{_sysconfdir}/diskspaced/
%files
%defattr(0644,root,root,-)
%{_sysconfdir}/diskspaced/halfmetre.json

%changelog
