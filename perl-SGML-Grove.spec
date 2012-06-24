%define		_noautoreq "perl(SGML::SubDocEntity)"
%include	/usr/lib/rpm/macros.perl
Summary:	SGML-Grove perl module
Summary(pl):	Modu� perla SGML-Grove
Name:		perl-SGML-Grove
Version:	2.03
Release:	7
License:	distributable
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	�r�unart�l/Forritunarm�l/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	��ȯ/����/Perl
Group(no):	Utvikling/Programmeringsspr�k/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Spr�k/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/SGML/SGML-Grove-%{version}.tar.gz
Patch0:		%{name}-Simple-Spec.patch
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGML-Grove provides an interface for accessing and manipulating SGML,
XML, HTML and other document instances after they've been built by a
parsing or grove building module like SGML::SPGroveBuilder,
Pod::GroveBuilder, etc.

%description -l pl
SGML-Grove umo�liwia operowanie na dokumentach SGML, XML, HTML.

%prep
%setup -q -n SGML-Grove-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a entities $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes ChangeLog README ToDo DOM 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/SGML/*.pm
%{perl_sitelib}/SGML/Simple
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
