
Name:           ps_mem
Version:        3.6
Release:        9%{?dist}
Summary:        Memory profiling tool
Group:          Applications/System
License:        LGPLv2
URL:            https://github.com/pixelb/ps_mem

Source0:        https://raw.githubusercontent.com/pixelb/ps_mem/c80287d/ps_mem.py
Source1:        http://www.gnu.org/licenses/lgpl-2.1.txt
Source2:        ps_mem.1

BuildArch:      noarch

BuildRequires:  python3-devel

%description
The ps_mem tool reports how much core memory is used per program
(not per process). In detail it reports:
sum(private RAM for program processes) + sum(Shared RAM for program processes)
The shared RAM is problematic to calculate, and the tool automatically
selects the most accurate method available for the running kernel.


%prep
%setup -q -T -c %{name}-%{version}

cp -p %{SOURCE0} %{name}
cp -p %{SOURCE1} LICENSE
cp -p %{SOURCE2} %{name}.1

# use python3
sed -i "s|/usr/bin/env python|%{__python3}|" %{name}
touch -r %{SOURCE0} %{name}


%install
install -Dpm755 %{name}   %{buildroot}%{_bindir}/%{name}
install -Dpm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%doc LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Nov 05 2021 Jan Rybar <jrybar@redhat.com> - 3.6-9
- python-3.6 introduced changes in flush() sanitizing: gating fails
- Resolves: rhbz#1651769

* Thu Nov 04 2021 Jan Rybar <jrybar@redhat.com> - 3.6-8
- output is not redirected when ps_mem is killed
- Resolves: rhbz#1651769

* Tue Jun 30 2020 Jan Rybar <jrybar@redhat.com> - 3.6-7
- gating activated
- cmdline unwanted blank spaces fixed
- Resolves: rhbz#1780986

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.6-3
- Rebuild for Python 3.6

* Mon Jul 11 2016 Lumir Balhar <lbalhar@redhat.com> - 3.6-2
- Fixed missing BuildRequire

* Wed Jun 08 2016 Lumir Balhar <lbalhar@redhat.com> - 3.6-1
- Latest upstream release
- Package ported to Python3 with dependencies

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Pádraig Brady <pbrady@redhat.com> - 3.5-1
- Latest upstream
- Depend on default python implementation

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-4
- RH man page scan (#989490)

* Thu Jul 25 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-3
- Patching shebang to force python3 (#987036)

* Thu May 30 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-2
- Preserving file timestamps

* Wed May 29 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-1
- Initial package
