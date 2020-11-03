%global gem_name asciidoctor-diagram

Name: rubygem-%{gem_name}
Version: 2.0.5
Release: 1%{?dist}
Summary: Asciidoctor diagramming extension
License: MIT
URL: https://github.com/asciidoctor/asciidoctor-diagram
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: blockdiag
BuildRequires: ImageMagick
BuildRequires: graphviz-ruby
BuildRequires: gnuplot
BuildRequires: plantuml
BuildRequires: plantuml-javadoc
BuildRequires: ditaa
BuildRequires: mscgen
BuildRequires: nwdiag
BuildRequires: seqdiag
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(asciidoctor)
BuildRequires: rubygem(asciidoctor-pdf)
BuildRequires: rubygem(bigdecimal)

BuildArch: noarch

%description
Asciidoctor Diagram is a set of Asciidoctor extensions that
enables you to add diagrams, which you describe using
plain text, to your AsciiDoc document.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
rspec -rasciidoctor-diagram spec

%files
%dir %{gem_instdir}
%{_bindir}/%{gem_name}
%{_bindir}/%{gem_name}-optimize
%license %{gem_instdir}/LICENSE.adoc
%doc %{gem_instdir}/README.adoc
%{gem_instdir}/bin
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Tue Oct 27 2020 Christopher Brown <chris.brown@redhat.com> - 2.0.5-1
- 
