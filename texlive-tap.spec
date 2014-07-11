# revision 31731
# category Package
# catalog-ctan /macros/generic/tables/tap077.zip
# catalog-date 2012-06-22 13:21:57 +0200
# catalog-license pd
# catalog-version 0.77
Name:		texlive-tap
Version:	0.77
Release:	9
Summary:	TeX macros for typesetting complex tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/tables/tap077.zip
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a simple notation for pretty complex tables
(to Michael J. Ferguson's credit). With PostScript, the package
allows shaded/coloured tables, diagonal rules, etc. The package
is supposed to work with both Plain and LaTeX. An AWK converter
from ASCII semigraphic tables to TAP notation is included.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/tap/tap.tex
%doc %{_texmfdistdir}/doc/generic/tap/0README.TAP
%doc %{_texmfdistdir}/doc/generic/tap/0tapdoc.inf
%doc %{_texmfdistdir}/doc/generic/tap/circ.eps
%doc %{_texmfdistdir}/doc/generic/tap/circmag.eps
%doc %{_texmfdistdir}/doc/generic/tap/epsfx.tex
%doc %{_texmfdistdir}/doc/generic/tap/tapanch.100
%doc %{_texmfdistdir}/doc/generic/tap/tapanch.mp
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/0sampdos.inf
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/post1.tex
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/post2.tex
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/prea1.tex
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/prea2.tex
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/prea3.tex
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tapcv0.raw
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tapcv1.raw
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tapcv2.raw
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tapcv3.raw
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tapcv4.raw
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tapcv5.raw
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tapcv6.raw
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tcv.bat
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/sampdos/tcv_.bat
%doc %{_texmfdistdir}/doc/generic/tap/tapcv/tapcv.awk
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
