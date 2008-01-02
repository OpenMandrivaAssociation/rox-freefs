%define name rox-freefs
%define version 2.1.4
%define release %mkrel 3
%define oname FreeFS

Summary: ROX application to monitor file system usage
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.kerofin.demon.co.uk/rox/%{oname}-%{version}.tar.bz2
Patch: FreeFS-2.1.3-fstab-check.patch
License: GPL
Group: Graphical desktop/Other
Url: http://www.kerofin.demon.co.uk/rox/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: librox-c-devel >= 2.1.6

%description
Monitor free space on a file system. This runs as either a panel
applet or a separate window.

%prep
%setup -q -n %oname
%patch -p1
cd src
autoconf

%build
export LIBDIRPATH=%_libdir
./AppRun ||:

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_libdir/apps/
cp -r ../%oname %buildroot%_libdir/apps/
rm -rf %buildroot%_libdir/apps/%oname/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %_libdir/apps/%oname
%_libdir/apps/%oname/.DirIcon
%_libdir/apps/%oname/App*
%_libdir/apps/%oname/%oname.xml
%doc %_libdir/apps/%oname/Help
%_libdir/apps/%oname/Options.xml
%_libdir/apps/%oname/Resources
%_libdir/apps/%oname/Linux-*
%_libdir/apps/%oname/libdir
%_libdir/apps/%oname/choice_install
%_libdir/apps/%oname/gtkrc
%_libdir/apps/%oname/rox_run


