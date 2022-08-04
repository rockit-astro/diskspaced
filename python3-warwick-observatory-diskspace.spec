Name:           python3-warwick-observatory-diskspace
Version:        20220804
Release:        0
License:        GPL3
Summary:        Common backend code for the disk space daemon
Url:            https://github.com/warwick-one-metre/diskspaced
BuildArch:      noarch

%description

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
