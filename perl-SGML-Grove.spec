%include	/usr/lib/rpm/macros.perl
Summary:	SGML-Grove perl module
Summary(pl):	Modu³ perla SGML-Grove
Name:		perl-SGML-Grove
Version:	2.03
Release:	3
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/SGML/SGML-Grove-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGML-Grove provides an interface for accessing and manipulating SGML,
XML, HTML and other document instances after they've been built by a
parsing or grove building module like SGML::SPGroveBuilder,
Pod::GroveBuilder, etc.

%description -l pl
SGML-Grove umo¿liwia operowanie na dokumentach SGML, XML, HTML.

%prep
%setup -q -n SGML-Grove-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}
cp -a entities $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/SGML/Grove
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes ChangeLog README ToDo DOM 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,ChangeLog,README,ToDo,DOM}.gz

%{perl_sitelib}/SGML/*.pm
%{perl_sitelib}/SGML/Simple
%{perl_sitearch}/auto/SGML/Grove

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}-%{version}
