Summary:	WebKit KDE browser
Name:		rekonq
Version:	0.7.0
Release:	1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	http://download.sourceforge.net/project/rekonq/%{version}/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	73de712f71ea4caf2e66a92c77505da8
URL:		http://rekonq.kde.org/
BuildRequires:	QtWebKit-devel
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.2
BuildRequires:	kde4-kdelibs-devel >= 4.4.0
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake >= 4.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rekonq is WebKit KDE browser.

%prep
%setup -q
rm -f i18n/rekonq_sr@ije*.po

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang rekonq	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rekonq.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO INSTALL
%attr(755,root,root) %{_bindir}/rekonq
%attr(755,root,root) %{_libdir}/libkdeinit4_rekonq.so

%{_iconsdir}/*/*/*/rekonq.png
%{_desktopdir}/kde4/rekonq.desktop
%{_datadir}/config.kcfg/rekonq.kcfg
%{_datadir}/apps/rekonq
