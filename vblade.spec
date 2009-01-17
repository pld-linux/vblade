Summary:	vblade, virtual EtherDrive blade
Summary(pl.UTF-8):	vblade - wirtualny blade EtherDrive
Name:		vblade
Version:	19
Release:	1
License:	GPL v2
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/aoetools/%{name}-%{version}.tgz
# Source0-md5:	59d45caa6454388eea60441dcf6631db
URL:		http://aoetools.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vblade lets you export any block storage device as a AoE device.

%description -l pl.UTF-8
vblade pozwala eksportować dowolne urządzenie blokowe przechowujące
dane jako urządzenie AoE.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_sbindir}/vbladed
%attr(755,root,root) %{_sbindir}/vblade
%{_mandir}/man8/vblade.8*
