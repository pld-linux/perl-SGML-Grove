%include	/usr/lib/rpm/macros.perl
%define		pdir	SGML
%define		pnam	Grove
Summary:	SGML::Grove Perl module
Summary(cs):	Modul SGML::Grove pro Perl
Summary(da):	Perlmodul SGML::Grove
Summary(de):	SGML::Grove Perl Modul
Summary(es):	Módulo de Perl SGML::Grove
Summary(fr):	Module Perl SGML::Grove
Summary(it):	Modulo di Perl SGML::Grove
Summary(ja):	SGML::Grove Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	SGML::Grove ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul SGML::Grove
Summary(pl):	Modu³ Perla SGML::Grove
Summary(pt):	Módulo de Perl SGML::Grove
Summary(pt_BR):	Módulo Perl SGML::Grove
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl SGML::Grove
Summary(sv):	SGML::Grove Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl SGML::Grove
Summary(zh_CN):	SGML::Grove Perl Ä£¿é
Name:		perl-SGML-Grove
Version:	2.03
Release:	11
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9764eaed3da0b4134224afe9b63a8966
Patch0:		%{name}-Simple-Spec.patch
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq "perl(SGML::SubDocEntity)"

%description
SGML::Grove provides an interface for accessing and manipulating SGML,
XML, HTML and other document instances after they've been built by a
parsing or grove building module like SGML::SPGroveBuilder,
Pod::GroveBuilder, etc.

%description -l pl
SGML::Grove umo¿liwia operowanie na dokumentach SGML, XML, HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a entities $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes ChangeLog README ToDo DOM
%{perl_vendorlib}/SGML
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
