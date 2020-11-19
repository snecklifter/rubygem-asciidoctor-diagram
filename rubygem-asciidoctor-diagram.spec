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
BuildRequires: ditaa
BuildRequires: gnuplot
BuildRequires: graphviz-ruby
BuildRequires: ImageMagick
BuildRequires: lilypond
BuildRequires: mscgen
BuildRequires: plantuml
BuildRequires: python-reportlab
BuildRequires: texlive-listingsutf8
BuildRequires: texlive-pgfplots
BuildRequires: texlive-standalone
BuildRequires: texlive-tcolorbox
BuildRequires: texlive-tkz-euclide
BuildRequires: tikzit
BuildRequires: TeXmacs
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(asciidoctor)
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
# Run the test excluding extensions which are not packaged yet
rspec --exclude-pattern 'spec/{a2s_spec.rb,bpmn_spec.rb,bytefield_spec.rb,dpic_spec.rb,
                         erd_spec.rb,mermaid_spec.rb,nomnoml_spec.rb,pikchr_spec.rb,
                         umlet_spec.rb,vega_spec.rb,syntrax_spec.rb,
                         shaape_spec.rb,smcat_spec.rb,svgbob_spec.rb,
                         symbolator_spec.rb,wavedrom_spec.rb}'

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
* Mon Nov 16 2020 Christopher Brown <chris.brown@redhat.com> - 2.0.5-1
- Initial build
