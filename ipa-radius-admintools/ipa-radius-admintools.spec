Name:           ipa-radius-admintools
Version:        0.6.0
Release:        1%{?dist}
Summary:        IPA authentication server - radius admin tools

Group:          System Environment/Base
License:        GPL
URL:            http://www.freeipa.org
Source0:        %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: 	noarch

Requires: python python-krbV ipa-python ipa-admintools

%description
IPA is a server for identity, policy, and audit.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir}

make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sbindir}/ipa*

%changelog
* Fri Dec 21 2007 Karl MacMillan <kmacmill@redhat.com> - 0.6.0-1
- Version bump for release

* Tue Dec 18 2007 Karl MacMillan <kmacmill@redhat.com> - 0.5.0
- Initial rpm version
