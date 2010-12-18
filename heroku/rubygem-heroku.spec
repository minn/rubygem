# Generated from heroku-1.14.10.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname heroku
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global download_path http://rubygems.org/downloads/
%global rubyabi 1.8

Summary: Client library and CLI to deploy Rails apps on Heroku
Name: rubygem-%{gemname}
Version: 1.14.10
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/heroku/heroku
Source0: %{download_path}%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: rubygems
Requires: rubygem(rest-client) >= 1.4.0
Requires: rubygem(rest-client) < 1.7.0
Requires: rubygem(launchy) >= 0.3.2
Requires: rubygem(json_pure) >= 1.2.0
Requires: rubygem(json_pure) < 1.5.0
BuildRequires: rubygems
BuildRequires: ruby(abi) = %{rubyabi}
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Client library and command-line tool to manage and deploy Rails apps on
Heroku.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
%description doc
This package contains documentation for %{name}.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{_bindir}/heroku
%{geminstdir}/bin
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{geminstdir}/README.md

%files doc
%defattr(-, root, root, -)
%{gemdir}/doc/%{gemname}-%{version}
%{geminstdir}/spec
%{geminstdir}/.yardoc

%changelog
* Thu Dec 18 2010  <Minnikhanov@gmail.com> - 1.14.10-2
- Fix Comment 18 #661436 (Review Request)
- Set Release: 2
* Thu Dec 17 2010  <Minnikhanov@gmail.com> - 1.14.10-1
- Fix Comment 13 #661436 (Review Request)
* Thu Dec 16 2010  <Minnikhanov@gmail.com> - 1.14.10-1
- Initial package
* Wed Dec 15 2010  <Minnikhanov@gmail.com> - 1.14.9-1
- Initial package
* Mon Dec 13 2010  <Minnikhanov@gmail.com> - 1.14.8-1
- Fix Comment 4 #661436 (Review Request)
* Wed Dec 08 2010  <Minnikhanov@gmail.com> - 1.14.8-1
- Initial package
