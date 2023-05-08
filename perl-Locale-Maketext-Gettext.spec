#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Locale-Maketext-Gettext
Version  : 1.32
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/I/IM/IMACAT/Locale-Maketext-Gettext-1.32.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IM/IMACAT/Locale-Maketext-Gettext-1.32.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblocale-maketext-gettext-perl/liblocale-maketext-gettext-perl_1.28-2.debian.tar.xz
Summary  : 'Joins gettext and Maketext frameworks'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Locale-Maketext-Gettext-bin = %{version}-%{release}
Requires: perl-Locale-Maketext-Gettext-license = %{version}-%{release}
Requires: perl-Locale-Maketext-Gettext-man = %{version}-%{release}
Requires: perl-Locale-Maketext-Gettext-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Locale::Maketext::Gettext - Joins the gettext and Maketext frameworks
=====================================================================

%package bin
Summary: bin components for the perl-Locale-Maketext-Gettext package.
Group: Binaries
Requires: perl-Locale-Maketext-Gettext-license = %{version}-%{release}

%description bin
bin components for the perl-Locale-Maketext-Gettext package.


%package dev
Summary: dev components for the perl-Locale-Maketext-Gettext package.
Group: Development
Requires: perl-Locale-Maketext-Gettext-bin = %{version}-%{release}
Provides: perl-Locale-Maketext-Gettext-devel = %{version}-%{release}
Requires: perl-Locale-Maketext-Gettext = %{version}-%{release}

%description dev
dev components for the perl-Locale-Maketext-Gettext package.


%package license
Summary: license components for the perl-Locale-Maketext-Gettext package.
Group: Default

%description license
license components for the perl-Locale-Maketext-Gettext package.


%package man
Summary: man components for the perl-Locale-Maketext-Gettext package.
Group: Default

%description man
man components for the perl-Locale-Maketext-Gettext package.


%package perl
Summary: perl components for the perl-Locale-Maketext-Gettext package.
Group: Default
Requires: perl-Locale-Maketext-Gettext = %{version}-%{release}

%description perl
perl components for the perl-Locale-Maketext-Gettext package.


%prep
%setup -q -n Locale-Maketext-Gettext-1.32
cd %{_builddir}
tar xf %{_sourcedir}/liblocale-maketext-gettext-perl_1.28-2.debian.tar.xz
cd %{_builddir}/Locale-Maketext-Gettext-1.32
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Locale-Maketext-Gettext-1.32/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Locale-Maketext-Gettext
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Locale-Maketext-Gettext/24acf436c804a2a3bf2b0dde94aa8560a6e6d544
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/maketext

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Locale::Maketext::Gettext.3
/usr/share/man/man3/Locale::Maketext::Gettext::Functions.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Locale-Maketext-Gettext/24acf436c804a2a3bf2b0dde94aa8560a6e6d544

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/maketext.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
