%global gem_name asciidoctor-diagram

Name: rubygem-%{gem_name}
Version: 2.0.5
Release: 1%{?dist}
Summary: Asciidoctor diagramming extension
License: MIT
URL: https://github.com/asciidoctor/asciidoctor-diagram
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: blockdiag
BuildRequires: ImageMagick
BuildRequires: graphviz-ruby
BuildRequires: gnuplot
BuildRequires: plantuml
BuildRequires: python-reportlab
BuildRequires: ditaa
BuildRequires: mscgen
#BuildRequires: nwdiag
#BuildRequires: seqdiag
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(prawn-svg)
BuildRequires: rubygem(asciidoctor-pdf)
BuildRequires: rubygem(bigdecimal)

BuildArch: noarch

%description
Asciidoctor Diagram is a set of Asciidoctor extensions that
enables you to add diagrams, which you describe using
plain text, to your AsciiDoc document.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

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
rspec -r asciidoctor-pdf --pattern "spec/blockdiag_spec.rb" \
                         --pattern "spec/test_helper.rb" \
                         --pattern "spec/ditaa_spec.rb" \
                         --pattern "spec/msc_spec.rb" \
                         --pattern "spec/plantuml_spec.rb" \
                         --pattern "spec/gnuplot_spec.rb" \
                         --pattern "spec/meme_spec.rb" \
                         --pattern "spec/graphviz_spec.rb"

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/testing
%exclude %{gem_instdir}/*.list

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/*.adoc
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/images
%doc %{gem_instdir}/spec


%changelog
* Fri Nov 13 2020 Christopher Brown <chris.brown@redhat.com> - 2.0.5-1
- 
