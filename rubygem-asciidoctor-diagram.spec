%global gem_name asciidoctor-diagram
# Many dependencies are not packaged in Fedora, mostly nodejs,
# so this bcond can test with enabling those if they are
# available in future.
%bcond_with missing_test_dependencies

Name: rubygem-%{gem_name}
Version: 2.0.5
Release: 1%{?dist}
Summary: Asciidoctor diagramming extension
License: MIT
URL: https://github.com/asciidoctor/asciidoctor-diagram
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: %{_bindir}/blockdiag
BuildRequires: %{_bindir}/convert
BuildRequires: %{_bindir}/ditaa
BuildRequires: %{_bindir}/gnuplot
BuildRequires: %{_libdir}/graphviz/ruby
BuildRequires: %{_bindir}/identify
BuildRequires: %{_bindir}/lilypond
BuildRequires: %{_bindir}/mscgen
BuildRequires: %{_bindir}/plantuml
BuildRequires: %{_bindir}/ruby
BuildRequires: %{_bindir}/texmacs
BuildRequires: %{_bindir}/tikzit
BuildRequires: %{py3_dist reportlab}
BuildRequires: %{_datadir}/texlive/texmf-dist/tex/latex/listingsutf8
BuildRequires: %{_datadir}/texlive/texmf-dist/tex/latex/tkz-euclide
BuildRequires: %{_datadir}/texlive/texmf-dist/tex/latex/pgfplots
BuildRequires: %{_datadir}/texlive/texmf-dist/tex/latex/standalone
BuildRequires: %{_datadir}/texlive/texmf-dist/tex/latex/tcolorbox
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(asciidoctor)
BuildRequires: rubygem(bigdecimal)
# Not packaged in Fedora.
%if %{with missing_test_dependencies}
BuildRequires: %{_bindir}/a2s
BuildRequires: %{_bindir}/bpmn
BuildRequires: %{_bindir}/bytefield
BuildRequires: %{_bindir}/dpic
BuildRequires: %{_bindir}/erd
BuildRequires: %{_bindir}/mermaid
BuildRequires: %{_bindir}/nomnoml
BuildRequires: %{_bindir}/pikchr
BuildRequires: %{_bindir}/umlet
BuildRequires: %{_bindir}/vega
BuildRequires: %{_bindir}/syntrax
BuildRequires: %{_bindir}/shaape
BuildRequires: %{_bindir}/smcat
BuildRequires: %{_bindir}/svgbob
BuildRequires: %{_bindir}/symbolator
BuildRequires: %{_bindir}/wavedrom
%endif

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
%if %{with missing_test_dependencies}
rspec spec
%else
# Run the test excluding extensions which are not packaged yet
rspec --exclude-pattern 'spec/{a2s_spec.rb,bpmn_spec.rb,bytefield_spec.rb,dpic_spec.rb,
                         erd_spec.rb,mermaid_spec.rb,nomnoml_spec.rb,pikchr_spec.rb,
                         umlet_spec.rb,vega_spec.rb,syntrax_spec.rb,
                         shaape_spec.rb,smcat_spec.rb,svgbob_spec.rb,
                         symbolator_spec.rb,wavedrom_spec.rb}'
%endif

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
