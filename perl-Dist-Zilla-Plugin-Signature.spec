%define upstream_name    Dist-Zilla-Plugin-Signature
%define upstream_version 1.252860

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Sign releases with Module::Signature
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/mikkoi/dist-zilla-plugin-signature
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIKKOI/Dist-Zilla-Plugin-Signature-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::chdir)
BuildRequires:	perl(Module::Signature)
BuildArch:	noarch

%description
This plugin will sign a distribution using Module::Signature

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

