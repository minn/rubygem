# Generated from launchy-0.3.7.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname launchy
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Launchy is helper class for launching cross-platform applications
Name: rubygem-%{gemname}
Version: 0.3.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://copiousfreetime.rubyforge.org/launchy/
Source0: %{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: rubygem(rake) >= 0.8.1
Requires: rubygem(configuration) >= 0.0.5
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Launchy is helper class for launching cross-platform applications in a
fire and forget manner.
There are application concepts (browser, email client, etc) that are
common across all platforms, and they may be launched differently on
each platform.  Launchy is here to make a common approach to launching
external application from within ruby programs.


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

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/launchy
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/HISTORY
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/lib/launchy/application.rb
%doc %{geminstdir}/lib/launchy/browser.rb
%doc %{geminstdir}/lib/launchy/command_line.rb
%doc %{geminstdir}/lib/launchy/paths.rb
%doc %{geminstdir}/lib/launchy/version.rb
%doc %{geminstdir}/lib/launchy.rb
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Dec 02 2010 <Minnikhanov@gmail.com> - 0.3.7-1
- Initial package
