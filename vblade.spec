#
# TODO:
#		- add devices to static-dev
#		- vblade
#
Summary:	vblade, virtual EtherDrive blade
Name:		vblade
Version:	10
Release:	0.1
License:	GPL v2
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/aoetools/%{name}-%{version}.tar.gz
# Source0-md5:	c51783ee3235aba58a0c095bdf5fc35c
URL:		http://aoetools.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vblade lets you export any block storage device as a AoE device

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install vbladed $RPM_BUILD_ROOT%{_sbindir}
install vblade $RPM_BUILD_ROOT%{_sbindir}
install vblade.8 $RPM_BUILD_ROOT%{_mandir}/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/vbladed
%attr(755,root,root) %{_sbindir}/vblade
%{_mandir}/man8/*
