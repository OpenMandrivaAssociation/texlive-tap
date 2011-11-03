# revision 15878
# category Package
# catalog-ctan /macros/generic/tables/tap077.zip
# catalog-date 2009-10-10 00:51:28 +0200
# catalog-license pd
# catalog-version 0.77
Name:		texlive-tap
Version:	0.77
Release:	1
Summary:	TeX macros for typesetting complex tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/tables/tap077.zip
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package offers a simple notation for pretty complex tables
(to Michael J. Ferguson's credit). With PostScript, the package
allows shaded/coloured tables, diagonal rules, etc. The package
is supposed to work with both Plain and LaTeX. An AWK converter
from ASCII semigraphic tables to TAP notation is included.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/tap/tap.tex
%doc %{_texmfdistdir}/doc/generic/tap/0README.TAP
%doc %{_texmfdistdir}/doc/generic/tap/0tabdoc.inf
%doc %{_texmfdistdir}/doc/generic/tap/circ.eps
%doc %{_texmfdistdir}/doc/generic/tap/circmag.eps
%doc %{_texmfdistdir}/doc/generic/tap/tapanch.100
%doc %{_texmfdistdir}/doc/generic/tap/tapanch.mp
%doc %{_texmfdistdir}/doc/generic/tap/tapdoc.tex
%doc %{_texmfdistdir}/doc/generic/tap/tapxamp1.tex
%doc %{_texmfdistdir}/doc/generic/tap/tapxamp2.tex
#- source
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/0sampdos.inf
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/post1.tex
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/post2.tex
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/prea1.tex
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/prea2.tex
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/prea3.tex
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tapcv0.raw
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tapcv1.raw
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tapcv2.raw
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tapcv3.raw
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tapcv4.raw
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tapcv5.raw
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tapcv6.raw
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tcv.bat
%doc %{_texmfdistdir}/source/generic/tap/tabcv/sampdos/tcv_.bat
%doc %{_texmfdistdir}/source/generic/tap/tabcv/tapcv.awk
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
