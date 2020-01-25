#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	SGML
%define		pnam	Grove
Summary:	SGML::Grove Perl module
Summary(cs.UTF-8):	Modul SGML::Grove pro Perl
Summary(da.UTF-8):	Perlmodul SGML::Grove
Summary(de.UTF-8):	SGML::Grove Perl Modul
Summary(es.UTF-8):	Módulo de Perl SGML::Grove
Summary(fr.UTF-8):	Module Perl SGML::Grove
Summary(it.UTF-8):	Modulo di Perl SGML::Grove
Summary(ja.UTF-8):	SGML::Grove Perl モジュール
Summary(ko.UTF-8):	SGML::Grove 펄 모줄
Summary(nb.UTF-8):	Perlmodul SGML::Grove
Summary(pl.UTF-8):	Moduł Perla SGML::Grove
Summary(pt.UTF-8):	Módulo de Perl SGML::Grove
Summary(pt_BR.UTF-8):	Módulo Perl SGML::Grove
Summary(ru.UTF-8):	Модуль для Perl SGML::Grove
Summary(sv.UTF-8):	SGML::Grove Perlmodul
Summary(uk.UTF-8):	Модуль для Perl SGML::Grove
Summary(zh_CN.UTF-8):	SGML::Grove Perl 模块
Name:		perl-SGML-Grove
Version:	2.03
Release:	12
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9764eaed3da0b4134224afe9b63a8966
Patch0:		%{name}-Simple-Spec.patch
URL:		http://search.cpan.org/dist/SGML-Grove/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Visitor
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq 'perl(SGML::SubDocEntity)'

%description
SGML::Grove provides an interface for accessing and manipulating SGML,
XML, HTML and other document instances after they've been built by a
parsing or grove building module like SGML::SPGroveBuilder,
Pod::GroveBuilder, etc.

%description -l pl.UTF-8
SGML::Grove umożliwia operowanie na dokumentach SGML, XML, HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a entities $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes ChangeLog README ToDo DOM
%{perl_vendorlib}/SGML
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
