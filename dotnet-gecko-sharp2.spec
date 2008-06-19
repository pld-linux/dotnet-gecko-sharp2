%include	/usr/lib/rpm/macros.mono
Summary:	Gecko# - A Gtk# Mozilla binding
Summary(pl.UTF-8):	Gecko# - wiązanie Gtk# dla Mozilli
Name:		dotnet-gecko-sharp2
Version:	0.13
Release:	1
Epoch:		0
License:	LGPL v2.1/MPL v1.1
Group:		Libraries
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/gecko-sharp2/gecko-sharp-2.0-%{version}.tar.bz2
# Source0-md5:	f88eaa06e71f8d8fa34cf59a3e034a6b
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 1.9.3
BuildRequires:	gtk+2-devel >= 2:2.0.0
BuildRequires:	mono-csharp >= 1.1.0
BuildRequires:	monodoc >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildConflicts:	gecko-sharp < 0.2
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Requires:	libgtkembedmoz.so()(64bit)
%else
Requires:	libgtkembedmoz.so
%endif
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gecko# - A Gtk# Mozilla binding.

%description -l pl.UTF-8
Gecko# - wiązanie Gtk# dla Mozilli.

%package devel
Summary:	Gecko# development files
Summary(pl.UTF-8):	Pliki programistyczne Gecko#
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Gecko# development files.

%description devel -l pl.UTF-8
Pliki programistyczne Gecko#.

%prep
%setup -q -n gecko-sharp-2.0-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	monodocdir=%{_libdir}/monodoc/sources \
	pkgconfigdir=%{_pkgconfigdir}

if ! pkg-config --exists mono; then
	sed -i -e 's/exec mono/exec mint/' $RPM_BUILD_ROOT%{_bindir}/webshot
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_prefix}/lib/mono/gac/gecko-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gecko-sharp-2.0
%{_pkgconfigdir}/*
%{_libdir}/monodoc/sources/*
