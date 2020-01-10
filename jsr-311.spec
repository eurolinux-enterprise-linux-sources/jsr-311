Name: jsr-311
Version: 1.1.1
Release: 6%{?dist}
Summary: JAX-RS: Java API for RESTful Web Services
Group: Development/Libraries
License: CDDL
Url: http://jsr311.java.net

# svn export https://svn.java.net/svn/jsr311~svn/tags/jsr311-api-1.1.1 jsr-311-1.1.1
# tar cvzf jsr-311-1.1.1.tgz jsr-311-1.1.1
Source0: %{name}-%{version}.tgz

# Patch the POM:
Patch0: %{name}-pom.patch

BuildRequires: buildnumber-maven-plugin
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

BuildArch: noarch


%description
JAX-RS: Java API for RESTful Web Services


%package javadoc
Summary: Javadocs for %{name}


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0

%mvn_file : %{name}


%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8


%install
%mvn_install


%files -f .mfiles


%files javadoc -f .mfiles-javadoc


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.1-6
- Mass rebuild 2013-12-27

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-5
- Update to current packaging guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2011 Juan Hernandez <juan.hernandez@redhat.com> 1.1.1-1
- Adapted (mostly copied, in fact) from the corresponding package from Mageia
  (http://www.mageia.org) with support from Gil Cattaneo <puntogil@libero.it>.

